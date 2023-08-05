import asyncio
import os
from asyncio import Future
from unittest import mock
from unittest.mock import MagicMock

import pytest
from faker import Faker

from wtfix.apps.admin import HeartbeatApp
from wtfix.apps.parsers import RawMessageParserApp
from wtfix.apps.sessions import ClientSessionApp
from wtfix.apps.wire import EncoderApp, DecoderApp
from wtfix.conf import settings, ConnectionSettings
from wtfix.message.admin import HeartbeatMessage
from wtfix.message.message import generic_message_factory
from wtfix.pipeline import BasePipeline
from wtfix.protocol.contextlib import connection, connection_manager


@asyncio.coroutine
def mock_coroutine():
    return None


@pytest.fixture
def base_pipeline():
    """
    Basic mock pipeline that can be used to instantiate new apps in tests.

    :return: A pipeline mock with a client session initialized.
    """
    with connection_manager() as conn:
        pipeline = MagicMock(BasePipeline)
        pipeline.settings = ConnectionSettings(conn.name)

        client_session = ClientSessionApp(pipeline, new_session=True)
        client_session.sender = pipeline.settings.SENDER
        client_session.target = pipeline.settings.TARGET

        pipeline.apps = {ClientSessionApp.name: client_session}

        # Mock a future message that will allow us to await pipeline.send and pipeline.receive.
        # Only useful in situations where we are not interested in the actual message result :(
        mock_future_message = MagicMock(return_value=Future())
        mock_future_message.return_value.set_result({})

        pipeline.send = mock_future_message
        pipeline.receive = MagicMock(return_value=mock_coroutine())

        # Simulate the pipeline shutting down
        pipeline.stop = MagicMock(return_value=mock_coroutine())

        yield pipeline

        try:
            os.remove(client_session._sid_path)
        except FileNotFoundError:
            # File does not exist - skip deletion
            pass


@pytest.fixture
def encoder_app(base_pipeline):
    return EncoderApp(base_pipeline)


@pytest.fixture
def decoder_app(base_pipeline):
    return DecoderApp(base_pipeline)


@pytest.fixture
def raw_msg_parser_app(base_pipeline):
    return RawMessageParserApp(base_pipeline)


class ZeroDelayHeartbeatTestApp(HeartbeatApp):
    """Heartbeat app with all delays set low for faster tests."""

    def __init__(self, pipeline, *args, **kwargs):
        super().__init__(pipeline, *args, **kwargs)

        self.seconds_to_next_check = mock.MagicMock()
        self.seconds_to_next_check.return_value = 0

    @property
    def heartbeat_interval(self):
        return 0.1

    @property
    def test_request_response_delay(self):
        return 0.1


@pytest.fixture
def zero_heartbeat_app(base_pipeline):
    return ZeroDelayHeartbeatTestApp(base_pipeline)


@pytest.fixture
def failing_server_heartbeat_app(base_pipeline):
    """Simulates the server failing after responding to three test requests."""
    app = ZeroDelayHeartbeatTestApp(base_pipeline)
    num_responses = 0

    async def simulate_heartbeat_response(message):
        nonlocal num_responses

        if num_responses < 3:
            await app.on_heartbeat(HeartbeatMessage(str(message.TestReqID)))
        num_responses += 1

    app.pipeline.send.side_effect = simulate_heartbeat_response

    return app


@pytest.fixture
def user_notification_message():
    faker = Faker()

    return generic_message_factory(
        (connection.protocol.Tag.MsgType, connection.protocol.MsgType.UserNotification),
        (connection.protocol.Tag.MsgSeqNum, 1),
        (
            connection.protocol.Tag.SenderCompID,
            settings.CONNECTIONS[connection.name]["SENDER"],
        ),
        (connection.protocol.Tag.SendingTime, "20181206-10:24:27.018"),
        (
            connection.protocol.Tag.TargetCompID,
            settings.CONNECTIONS[connection.name]["TARGET"],
        ),
        (connection.protocol.Tag.NoLinesOfText, 1),
        (connection.protocol.Tag.Text, "abc"),
        (connection.protocol.Tag.EmailType, 0),
        (connection.protocol.Tag.Subject, "Test message"),
        (connection.protocol.Tag.EmailThreadID, faker.pyint()),
    )


@pytest.fixture
def messages(user_notification_message):
    messages = []

    for idx in range(1, 6):
        next_message = user_notification_message.copy()
        next_message.seq_num = idx
        messages.append(next_message)

    return messages

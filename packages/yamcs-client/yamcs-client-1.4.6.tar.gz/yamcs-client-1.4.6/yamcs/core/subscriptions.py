from __future__ import absolute_import

import logging
import ssl
import threading

import websocket

from yamcs.api import websocket_pb2 as websocket_v2_pb2
from yamcs.core.exceptions import ConnectionFailure
from yamcs.protobuf.web import websocket_pb2


class WebSocketSubscriptionManager(object):
    def __init__(self, client, resource, options=None):
        self._client = client
        self._resource = resource
        self._options = options

        self._websocket = None
        self._callback = None
        self._response_callbacks = []
        self._close_callbacks = []

        self._closing = threading.Lock()
        self._closed = False
        """True if this manager has already been closed."""

        self._request_counter = 0
        self._request_counter_lock = threading.Lock()

        # Thread created in ``.open()``
        self._consumer = None

    def add_response_callback(self, callback):
        """
        Schedules a callable when a response was received.
        """
        self._response_callbacks.append(callback)

    def add_close_callback(self, callback):
        """
        Schedules a callable when the manager closes.
        """
        self._close_callbacks.append(callback)

    def open(self, callback, instance=None, processor=None):
        """
        Begin consuming messages.

        :param string instance: (Optional) instance to use in the WebSocket URL
        :param string processor: (Optional) processor to use in the WebSocket URL
        """
        assert not self._closed

        if self._client.credentials:
            self._client.credentials.before_request(
                self._client.session, self._client.auth_root
            )

        ws_url = self._client.ws_root
        if instance:
            ws_url += "/" + instance
            if processor:
                ws_url += "/" + processor

        self._callback = callback
        self._websocket = websocket.WebSocketApp(
            ws_url,
            on_open=self._on_websocket_open,
            on_message=self._on_websocket_message,
            on_error=self._on_websocket_error,
            subprotocols=["protobuf"],
            header=[
                "{}: {}".format(k, self._client.session.headers[k])
                for k in self._client.session.headers
            ],
        )

        kwargs = {}
        if not self._client.session.verify:
            kwargs["sslopt"] = {"cert_reqs": ssl.CERT_NONE}

        self._consumer = threading.Thread(
            target=self._websocket.run_forever, kwargs=kwargs
        )

        # Running this as a daemon thread improves possibilities for consumers
        # of our API to control shutdown. For example can can just use
        # time.sleep on the main thread instead of blocking on the future.
        self._consumer.daemon = True

        self._consumer.start()

    def close(self, reason=None):
        """
        Stop consuming messages and perform an orderly shutdown.

        If ``reason`` is None, then this is considered a regular close.
        """
        with self._closing:
            if self._closed:
                return

            self._websocket.close()

            self._consumer.join()
            self._consumer = None

            self._websocket = None
            self._closed = True
            for cb in self._close_callbacks:
                cb(self, reason)

    def send(self, operation, options=None):
        message = websocket_pb2.WebSocketClientMessage()
        message.protocolVersion = 1
        message.sequenceNumber = self._next_sequence_number()
        message.resource = self._resource
        message.operation = operation

        if options:
            data = options.SerializeToString()
            message.data = data

        frame_data = message.SerializeToString()
        self._websocket.send(frame_data, websocket.ABNF.OPCODE_BINARY)

    def _on_websocket_open(self, ws):
        self.send("subscribe", self._options)

    def _on_websocket_message(self, ws, message):
        try:
            pb2_message = websocket_pb2.WebSocketServerMessage()
            pb2_message.ParseFromString(message)

            if pb2_message.type == pb2_message.REPLY:
                for cb in self._response_callbacks:
                    cb(self, reply=pb2_message.reply)
            elif pb2_message.type == pb2_message.EXCEPTION:
                for cb in self._response_callbacks:
                    cb(self, exception=pb2_message.exception)
            self._callback(pb2_message)
        except Exception as e:
            logging.exception("Problem while processing message. Closing connection")
            self._close_async(reason=e)

    def _on_websocket_error(self, ws, error):
        logging.exception("WebSocket error")

        # Generate our own exception.
        # (the default message is misleading 'connection is already closed')
        if isinstance(error, websocket.WebSocketConnectionClosedException):
            error = ConnectionFailure("Connection closed")

        self._close_async(reason=error)

    def _close_async(self, reason):
        # Close async. This is to not get stuck in the above ``join()``.
        closer = threading.Thread(target=self.close, kwargs={"reason": reason})
        closer.daemon = True
        closer.start()

    def _next_sequence_number(self):
        with self._request_counter_lock:
            self._request_counter += 1
            return self._request_counter


class WebSocketSubscriptionManagerV2(object):
    def __init__(self, client, topic, options=None):
        self._client = client
        self._topic = topic
        self._options = options

        self._websocket = None
        self._callback = None
        self._response_callbacks = []
        self._close_callbacks = []

        self._closing = threading.Lock()
        self._closed = False
        """True if this manager has already been closed."""

        self._request_counter = 0
        self._request_counter_lock = threading.Lock()

        # Thread created in ``.open()``
        self._consumer = None

    def add_response_callback(self, callback):
        """
        Schedules a callable when a response was received.
        """
        self._response_callbacks.append(callback)

    def add_close_callback(self, callback):
        """
        Schedules a callable when the manager closes.
        """
        self._close_callbacks.append(callback)

    def open(self, callback):
        """
        Begin consuming messages.
        """
        assert not self._closed

        if self._client.credentials:
            self._client.credentials.before_request(
                self._client.session, self._client.auth_root
            )

        self._callback = callback
        self._websocket = websocket.WebSocketApp(
            self._client.ws_root_v2,
            on_open=self._on_websocket_open,
            on_message=self._on_websocket_message,
            on_error=self._on_websocket_error,
            subprotocols=["protobuf"],
            header=[
                "{}: {}".format(k, self._client.session.headers[k])
                for k in self._client.session.headers
            ],
        )

        kwargs = {}
        if not self._client.session.verify:
            kwargs["sslopt"] = {"cert_reqs": ssl.CERT_NONE}

        self._consumer = threading.Thread(
            target=self._websocket.run_forever, kwargs=kwargs
        )

        # Running this as a daemon thread improves possibilities for consumers
        # of our API to control shutdown. For example can can just use
        # time.sleep on the main thread instead of blocking on the future.
        self._consumer.daemon = True

        self._consumer.start()

    def close(self, reason=None):
        """
        Stop consuming messages and perform an orderly shutdown.

        If ``reason`` is None, then this is considered a regular close.
        """
        with self._closing:
            if self._closed:
                return

            self._websocket.close()

            self._consumer.join()
            self._consumer = None

            self._websocket = None
            self._closed = True
            for cb in self._close_callbacks:
                cb(self, reason)

    def send(self, options=None):
        message = websocket_v2_pb2.ClientMessage()
        message.type = self._topic
        message.id = self._next_sequence_number()
        if options:
            getattr(message, "options").Pack(options)

        frame_data = message.SerializeToString()
        self._websocket.send(frame_data, websocket.ABNF.OPCODE_BINARY)

    def _on_websocket_open(self, ws):
        self.send(self._options)

    def _on_websocket_message(self, ws, message):
        try:
            pb2_message = websocket_v2_pb2.ServerMessage()
            pb2_message.ParseFromString(message)

            type_ = getattr(pb2_message, "type")
            if type_ == "reply":
                reply = websocket_v2_pb2.Reply()
                getattr(pb2_message, "data").Unpack(reply)
                if reply.HasField("exception"):
                    for cb in self._response_callbacks:
                        cb(self, exception=getattr(reply, "exception"))
                else:
                    for cb in self._response_callbacks:
                        cb(self)
            else:
                data = getattr(pb2_message, "data")
                self._callback(data)
        except Exception as e:
            logging.exception("Problem while processing message. Closing connection")
            self._close_async(reason=e)

    def _on_websocket_error(self, ws, error):
        logging.exception("WebSocket error")

        # Generate our own exception.
        # (the default message is misleading 'connection is already closed')
        if isinstance(error, websocket.WebSocketConnectionClosedException):
            error = ConnectionFailure("Connection closed")

        self._close_async(reason=error)

    def _close_async(self, reason):
        # Close async. This is to not get stuck in the above ``join()``.
        closer = threading.Thread(target=self.close, kwargs={"reason": reason})
        closer.daemon = True
        closer.start()

    def _next_sequence_number(self):
        with self._request_counter_lock:
            self._request_counter += 1
            return self._request_counter

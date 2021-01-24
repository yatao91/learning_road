# -*- coding: utf-8 -*-
"""New Redis transport with correct ack emulation"""

from kombu.transport.redis import logger, dumps
from kombu.transport.redis import Channel as BaseChannel
from kombu.transport.redis import Transport as BaseTransport


class Channel(BaseChannel):

    def _do_restore_message(self, payload, exchange, routing_key, client=None):
        with self.conn_or_acquire(client) as client:
            try:
                try:
                    payload['headers']['redelivered'] = True
                except KeyError:
                    pass
                for queue in self._lookup(exchange, routing_key):
                    client.rpush(queue, dumps(payload))
            except Exception:
                logger.critical('Could not restore message: %r', payload, exc_info=True)


class Transport(BaseTransport):
    Channel = Channel

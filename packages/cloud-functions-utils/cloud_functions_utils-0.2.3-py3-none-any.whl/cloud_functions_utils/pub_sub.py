"""
This module provides helper functions for Google Pub/Sub.
"""

import base64
import json
import os


def decode(data, b64decode=True):
    """
    Decodes data coming from Pub/Sub.

    Args:
        data (str): The data you want to decode.
        b64decode (bool, optional): Whether to base64 decode the data.

    Returns:
        dict: The decoded message.
    """
    decoded = data
    if b64decode:
        decoded = base64.b64decode(decoded)
    return json.loads(decoded.decode("utf-8"))


def _encode(data, b64decode=False):
    encoded = json.dumps(data).encode("ascii")
    if b64encode:
        encoded = base64.b64encode(encoded)
    return encoded


def to_topic(messages, topic=None, b64encode=False):
    """
    Publishes messages to a Pub/Sub topic.

    Args:
        messages (list[dict]): The messages.
        topic (str, optional): The topic. If not provided, defaults to
            `os.environ["GCF_UTILS_PUBSUB_TOPIC"]`.
        b64encode (bool, optional): Whether to base64 encode the messages.
            This is done automatically for Google Cloud Functions.
    """
    # pylint: disable=import-outside-toplevel
    from google.cloud import pubsub_v1

    # pylint: enable=import-outside-toplevel

    publisher = pubsub_v1.PublisherClient()
    topic = topic or os.environ["GCF_UTILS_PUBSUB_TOPIC"]

    futures = [publisher.publish(topic, _encode(data, b64encode)) for data in messages]
    _ = [future.result() for future in futures]

import json
import time

from syntropy_sdk import MetadataNetworkType
from syntropy_sdk.exceptions import *

TAKE_MAX_ITEMS_PER_CALL = 2048
MAX_PAYLOAD_SIZE = 99 * 1024
MAX_QUERY_FIELD_SIZE = 2 * 1024

ALLOWED_NETWORK_TOPOLOGIES = (
    MetadataNetworkType.P2P,
    MetadataNetworkType.P2M,
    MetadataNetworkType.MESH,
)


class WithRetry:
    """Call api method several times in case of an error. Implements exponential back-off without jitter.

    Example:
        WithRetry(auth_api.login)("username", "password")
    """

    def __init__(self, func, retry_count=7, base=15, exponent=1, cap=180):
        self.func = func
        self.retry_count = retry_count
        self.base = base
        self.exponent = exponent
        self.cap = cap

    def __call__(self, *args, **kwargs):
        for attempt in range(self.retry_count):
            try:
                return self.func(*args, **kwargs)
            except ApiException as err:
                if err.status not in (500, 502, 503, 504, 408, 429):
                    raise
                # NOTE: This check is specifically for attempting to create connections just after the network was created.
                # In such a case the network ID is returned by the create_network api call, however, it is not yet being seen
                # by subsequent create_connections call if it is made too quickly.
                if err.status == 400 and attempt:
                    raise
                if attempt >= self.retry_count - 1:
                    raise
                delay = min(self.cap, self.base * 2 ** (attempt * self.exponent))
                time.sleep(delay)


def _default_translator(field):
    def translator(body, data):
        if data is None:
            return body[field]
        else:
            return {
                **body,
                field: data,
            }

    return translator


class BatchedRequest:
    """Executes requests in batches in order to circumvent payload/field size limit.
    Assumes that the batchable parameter is a list/tuple and api call returns a list.

    Translator must be provided for requests that have "body" as a kwarg. The translator
    is a callable that accepts the body as first argument and batch data as the second argument.
    It must return the list if the second argument is None and the payload body otherwise.
    It must not modify the body.

    Example translator:
        def translator(body, data):
            if data is None:
                return body["data"]
            else:
                return {
                    **body,
                    "data": data,
                }

    Example usage:
        BatchedRequest(
            api.update_connection_services,
            max_payload_size=MAX_PAYLOAD_SIZE,
            translator=_default_translator("changes"),
        )(body=body)
    """

    def __init__(
        self,
        func,
        max_payload_size,
        translator=_default_translator("data"),
    ):
        self.func = func
        self.max_payload_size = max_payload_size
        self.translator = translator

    def __call__(self, *args, **kwargs):
        if "body" in kwargs:
            return self._call_with_body(*args, **kwargs)
        else:
            return self._call_with_query(*args, **kwargs)

    def _call_with_body(self, *args, **kwargs):
        body = kwargs.pop("body")
        data = self.translator(body, None)
        return self._call(body, data, *args, **kwargs)

    def _call_with_query(self, *args, **kwargs):
        query = args[0]
        args = args[1:]
        return self._call(None, query, *args, **kwargs)

    def _calculate_payload_size(self, data):
        if isinstance(data, list):
            return len(",".join(str(i) for i in data))
        else:
            return len(json.dumps(data))

    def _determine_batch_size(self, body, data, batch_size):
        while batch_size:
            data = data[:batch_size]
            batch = self.translator(body, data) if body is not None else data
            if self._calculate_payload_size(batch) > self.max_payload_size:
                batch_size //= 2
            else:
                return batch_size, batch
        raise SyntropyError("Batch size could not be determined")

    def _generate_batches(self, body, data):
        batch_size = len(data)
        while data:
            batch_size, batch = self._determine_batch_size(body, data, batch_size)
            data = data[batch_size:]
            yield batch

    def _call(self, body, data, *args, **kwargs):
        result = []
        for batch in self._generate_batches(body, data):
            # TODO: What to do with errors in result?
            func = WithRetry(self.func)
            if body is None:
                response = func(batch, *args, **kwargs)
            else:
                response = func(body=batch, *args, **kwargs)
            if isinstance(response, dict) and "data" in response:
                result += response["data"]
            else:
                result.append(response)
        # NOTE: Undesirable side effect: will transform non-list responses to {"data": data}
        return {"data": result}

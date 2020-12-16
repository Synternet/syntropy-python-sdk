import json
from unittest import mock

import pytest

import syntropy_sdk as sdk
from syntropy_sdk import utils
from syntropy_sdk.rest import ApiException


def test_with_retry__success():
    assert utils.WithRetry(lambda x: x)(42) == 42


def test_with_retry__fail_retry():
    func = mock.Mock(side_effect=[ApiException(status=502), ApiException(status=503)])
    func.__name__ = "test func"
    with pytest.raises(utils.ApiException):
        utils.WithRetry(func, retry_count=2, cap=0.1)(42)
    assert func.call_args_list == [mock.call(42) for _ in range(2)]


def test_with_retry__fail():
    func = mock.Mock(side_effect=ValueError)
    with pytest.raises(ValueError):
        utils.WithRetry(func, retry_count=2, cap=0.1)(42)
    func.assert_called_once_with(42)


def test_determine_batch_size():
    request = utils.BatchedRequest(lambda x: x, max_payload_size=5)
    assert request._determine_batch_size(None, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == (
        2,
        [0, 1],
    )


def test_determine_batch_size__fail():
    request = utils.BatchedRequest(lambda x: x, max_payload_size=5)
    with pytest.raises(utils.SyntropyError):
        request._determine_batch_size(
            None,
            [102400, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000],
            10,
        )


def test_batched_request__query():
    func = mock.Mock(return_value={"data": [1, 2, 3]})
    assert utils.BatchedRequest(func, max_payload_size=5)(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ) == {"data": [i + 1 for _ in range(5) for i in range(3)]}
    assert func.call_args_list == [
        mock.call([0, 1]),
        mock.call([2, 3]),
        mock.call([4, 5]),
        mock.call([6, 7]),
        mock.call([8, 9]),
    ]


def test_batched_request__query_full():
    func = mock.Mock(return_value={"data": [1, 2, 3]})
    assert utils.BatchedRequest(func, max_payload_size=20)(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ) == {
        "data": [1, 2, 3],
    }
    assert func.call_args_list == [
        mock.call([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ]


def test_batched_request__body():
    func = mock.Mock(return_value={"data": [1, 2, 3]})
    assert utils.BatchedRequest(func, max_payload_size=30)(
        body={"data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, param="param"
    ) == {"data": [1, 2, 3, 1, 2, 3]}
    assert func.call_args_list == [
        mock.call(body={"data": [0, 1, 2, 3, 4]}, param="param"),
        mock.call(body={"data": [5, 6, 7, 8, 9]}, param="param"),
    ]


def test_batched_request__body_full():
    func = mock.Mock(return_value={"data": [1, 2, 3]})
    assert utils.BatchedRequest(func, max_payload_size=100)(
        body={"data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, param="param"
    ) == {"data": [1, 2, 3]}
    assert func.call_args_list == [
        mock.call(body={"data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, param="param"),
    ]


def test_batched_request__body_empty_result():
    func = mock.Mock(return_value=None)
    assert utils.BatchedRequest(
        func, translator=utils._default_translator("smth"), max_payload_size=100
    )(body={"id": 123, "smth": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, param="param") == {
        "data": [None]
    }
    assert func.call_args_list == [
        mock.call(
            body={"id": 123, "smth": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, param="param"
        ),
    ]

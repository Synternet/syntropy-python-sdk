import json
from unittest import mock

import pytest

import syntropy_sdk as sdk
from syntropy_sdk import models, utils
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


@pytest.mark.parametrize(
    "effect, skip, take, max_take, expect",
    (
        ([1, 2, 3, 4, 5], 0, 3, 3, {"data": [1, 2, 3]}),
        ([1, 2, 3, 4, 5], 1, 3, 3, {"data": [2, 3, 4]}),
        ([1, 2, 3, 4, 5], 1, 3, 5, {"data": [2, 3, 4]}),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0, 5, {"data": [1, 2, 3, 4, 5, 6, 7, 8, 9]}),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 0, 5, {"data": [2, 3, 4, 5, 6, 7, 8, 9]}),
    ),
)
def test_with_pagination(effect, skip, take, max_take, expect):
    def fn(skip=0, take=0):
        return {"data": effect[skip : skip + take]}

    result = utils.WithPagination(fn, max_take=max_take)(skip=skip, take=take)
    assert result == expect


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
    assert utils.BatchedRequestQuery(func, max_query_size=5)(
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
    assert utils.BatchedRequestQuery(func, max_query_size=20)(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ) == {
        "data": [1, 2, 3],
    }
    assert func.call_args_list == [
        mock.call([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ]


def test_batched_request__body():
    func = mock.Mock(return_value={"data": [1, 2, 3]})
    assert utils.BatchedRequestBody(func, max_payload_size=30)(
        body={"data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, param="param"
    ) == {"data": [1, 2, 3, 1, 2, 3]}
    assert func.call_args_list == [
        mock.call(body={"data": [0, 1, 2, 3, 4]}, param="param"),
        mock.call(body={"data": [5, 6, 7, 8, 9]}, param="param"),
    ]


def test_batched_request__body_full():
    func = mock.Mock(return_value={"data": [1, 2, 3]})
    assert utils.BatchedRequestBody(func, max_payload_size=100)(
        body={"data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, param="param"
    ) == {"data": [1, 2, 3]}
    assert func.call_args_list == [
        mock.call(body={"data": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, param="param"),
    ]


def test_batched_request__body_empty_result():
    func = mock.Mock(return_value=None)
    assert utils.BatchedRequestBody(
        func, translator=utils._default_translator("smth"), max_payload_size=100
    )(body={"id": 123, "smth": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, param="param") == {
        "data": [None]
    }
    assert func.call_args_list == [
        mock.call(
            body={"id": 123, "smth": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, param="param"
        ),
    ]


def test_batched_request__filter_partial():
    func = mock.Mock(return_value={"data": [1, 2, 3]})
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert utils.BatchedRequestFilter(func, max_query_size=4, filter_data=data[:5])(
        filter=data[5:]
    ) == {"data": [i + 1 for _ in range(5) for i in range(3)]}
    assert func.call_args_list == [
        mock.call(filter="0,1"),
        mock.call(filter="2,3"),
        mock.call(filter="4,5"),
        mock.call(filter="6,7"),
        mock.call(filter="8,9"),
    ]


def test_batched_request__filter():
    func = mock.Mock(return_value={"data": [1, 2, 3]})
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert utils.BatchedRequestFilter(func, max_query_size=200, filter_data=data[:5])(
        filter=data[5:]
    ) == {
        "data": [1, 2, 3],
    }
    assert func.call_args_list == [
        mock.call(filter="0,1,2,3,4,5,6,7,8,9"),
    ]


def test_login_with_access_token():
    with mock.patch.object(
        sdk.AuthApi,
        "v1_network_auth_access_token_login",
        autospec=True,
        return_value=models.V1NetworkAuthAccessTokenLoginResponse(
            {
                "access_token": "token",
                "token_type": "bearer",
                "expires_in": "whenever",
                "refresh_token": "refresh token",
            }
        ),
    ) as the_mock:
        assert "token" == utils.login_with_access_token("the url", "access token")
        the_mock.assert_called_once()

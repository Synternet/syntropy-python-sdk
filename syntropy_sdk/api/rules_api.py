# coding: utf-8

"""
    Syntropy network API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@syntropynet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from syntropy_sdk.api_client import ApiClient


class RulesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def rules_connection_point_to_tag_update(self, body, **kwargs):  # noqa: E501
        """Upsert point-to-tag  # noqa: E501

        Simultaneously adds, removes, replaces point-to-tags Rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_connection_point_to_tag_update(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ConnectionsPointtotagBody] body: Operations list (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rules_connection_point_to_tag_update_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.rules_connection_point_to_tag_update_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def rules_connection_point_to_tag_update_with_http_info(self, body, **kwargs):  # noqa: E501
        """Upsert point-to-tag  # noqa: E501

        Simultaneously adds, removes, replaces point-to-tags Rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rules_connection_point_to_tag_update_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ConnectionsPointtotagBody] body: Operations list (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rules_connection_point_to_tag_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `rules_connection_point_to_tag_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt']  # noqa: E501

        return self.api_client.call_api(
            '/v1/network/rules/connections/point-to-tag', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_network_rules_connections_point_to_tag_create(self, body, **kwargs):  # noqa: E501
        """Create point-to-tag  # noqa: E501

        Creates point to tag Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_network_rules_connections_point_to_tag_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1RulesPointToTag body: (required)
        :return: V1NetworkRulesConnectionsPointToTagCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_network_rules_connections_point_to_tag_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_network_rules_connections_point_to_tag_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1_network_rules_connections_point_to_tag_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create point-to-tag  # noqa: E501

        Creates point to tag Rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_network_rules_connections_point_to_tag_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1RulesPointToTag body: (required)
        :return: V1NetworkRulesConnectionsPointToTagCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_network_rules_connections_point_to_tag_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_network_rules_connections_point_to_tag_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt']  # noqa: E501

        return self.api_client.call_api(
            '/v1/network/rules/connections/point-to-tag', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1NetworkRulesConnectionsPointToTagCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_network_rules_connections_point_to_tag_get_one(self, agent_id, **kwargs):  # noqa: E501
        """Get point-to-tag  # noqa: E501

        Retrieve point-to-tag Rules by `agent_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_network_rules_connections_point_to_tag_get_one(agent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdNumber agent_id: (required)
        :return: V1NetworkRulesConnectionsPointToTagGetOneResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_network_rules_connections_point_to_tag_get_one_with_http_info(agent_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_network_rules_connections_point_to_tag_get_one_with_http_info(agent_id, **kwargs)  # noqa: E501
            return data

    def v1_network_rules_connections_point_to_tag_get_one_with_http_info(self, agent_id, **kwargs):  # noqa: E501
        """Get point-to-tag  # noqa: E501

        Retrieve point-to-tag Rules by `agent_id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_network_rules_connections_point_to_tag_get_one_with_http_info(agent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdNumber agent_id: (required)
        :return: V1NetworkRulesConnectionsPointToTagGetOneResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['agent_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_network_rules_connections_point_to_tag_get_one" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'agent_id' is set
        if ('agent_id' not in params or
                params['agent_id'] is None):
            raise ValueError("Missing the required parameter `agent_id` when calling `v1_network_rules_connections_point_to_tag_get_one`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'agent_id' in params:
            path_params['agent_id'] = params['agent_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt']  # noqa: E501

        return self.api_client.call_api(
            '/v1/network/rules/connections/point-to-tag/{agent_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1NetworkRulesConnectionsPointToTagGetOneResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_network_rules_connections_point_to_tag_search(self, body, **kwargs):  # noqa: E501
        """Search point-to-tag Rules  # noqa: E501

        Gets list of point-to-tag Rules by given criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_network_rules_connections_point_to_tag_search(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1NetworkRulesConnectionsPointToTagSearchRequest body: Search request (required)
        :return: V1NetworkRulesConnectionsPointToTagSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_network_rules_connections_point_to_tag_search_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_network_rules_connections_point_to_tag_search_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1_network_rules_connections_point_to_tag_search_with_http_info(self, body, **kwargs):  # noqa: E501
        """Search point-to-tag Rules  # noqa: E501

        Gets list of point-to-tag Rules by given criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_network_rules_connections_point_to_tag_search_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1NetworkRulesConnectionsPointToTagSearchRequest body: Search request (required)
        :return: V1NetworkRulesConnectionsPointToTagSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_network_rules_connections_point_to_tag_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_network_rules_connections_point_to_tag_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt']  # noqa: E501

        return self.api_client.call_api(
            '/v1/network/rules/connections/point-to-tag/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1NetworkRulesConnectionsPointToTagSearchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_network_rules_search(self, **kwargs):  # noqa: E501
        """Search Rules  # noqa: E501

        Gets list of Rules by given criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_network_rules_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1NetworkRulesSearchRequest body:
        :return: V1NetworkRulesSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_network_rules_search_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_network_rules_search_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_network_rules_search_with_http_info(self, **kwargs):  # noqa: E501
        """Search Rules  # noqa: E501

        Gets list of Rules by given criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_network_rules_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1NetworkRulesSearchRequest body:
        :return: V1NetworkRulesSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_network_rules_search" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt']  # noqa: E501

        return self.api_client.call_api(
            '/v1/network/rules/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1NetworkRulesSearchResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_rules_connection_point_to_tag_remove(self, body, **kwargs):  # noqa: E501
        """Remove point-to-tag  # noqa: E501

        Removes point-to-tag Rules by given criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_rules_connection_point_to_tag_remove(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1RulesPointToTag body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_rules_connection_point_to_tag_remove_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_rules_connection_point_to_tag_remove_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def v1_rules_connection_point_to_tag_remove_with_http_info(self, body, **kwargs):  # noqa: E501
        """Remove point-to-tag  # noqa: E501

        Removes point-to-tag Rules by given criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_rules_connection_point_to_tag_remove_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1RulesPointToTag body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_rules_connection_point_to_tag_remove" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_rules_connection_point_to_tag_remove`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['jwt']  # noqa: E501

        return self.api_client.call_api(
            '/v1/network/rules/connections/point-to-tag/remove', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
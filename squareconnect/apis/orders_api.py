# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class OrdersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def batch_retrieve_orders(self, location_id, body, **kwargs):
        """
        BatchRetrieveOrders
        Retrieves a set of [Order](#type-order)s by their IDs.  If a given Order ID does not exist, the ID is ignored instead of generating an error.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.batch_retrieve_orders(location_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str location_id: The ID of the orders' associated location. (required)
        :param BatchRetrieveOrdersRequest body: An object containing the fields to POST for the request.  See the corresponding object definition for field details. (required)
        :return: BatchRetrieveOrdersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method batch_retrieve_orders" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'location_id' is set
        if ('location_id' not in params) or (params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `batch_retrieve_orders`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `batch_retrieve_orders`")


        resource_path = '/v2/locations/{location_id}/orders/batch-retrieve'.replace('{format}', 'json')
        path_params = {}
        if 'location_id' in params:
            path_params['location_id'] = params['location_id']

        query_params = {}

        header_params = {}
        header_params['Square-Version'] = "2018-12-05"
        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BatchRetrieveOrdersResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

    def create_order(self, location_id, body, **kwargs):
        """
        CreateOrder
        Creates an [Order](#type-order) that can then be referenced as `order_id` in a request to the [Charge](#endpoint-charge) endpoint. Orders specify products for purchase, along with discounts, taxes, and other settings to apply to the purchase.  To associate a created order with a request to the Charge endpoint, provide the order's `id` in the `order_id` field of your request.  You cannot modify an order after you create it. If you need to modify an order, instead create a new order with modified details.  To learn more about the Orders API, see the [Orders API Overview](/products/orders/overview).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_order(location_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str location_id: The ID of the business location to associate the order with. (required)
        :param CreateOrderRequest body: An object containing the fields to POST for the request.  See the corresponding object definition for field details. (required)
        :return: CreateOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['location_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_order" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'location_id' is set
        if ('location_id' not in params) or (params['location_id'] is None):
            raise ValueError("Missing the required parameter `location_id` when calling `create_order`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_order`")


        resource_path = '/v2/locations/{location_id}/orders'.replace('{format}', 'json')
        path_params = {}
        if 'location_id' in params:
            path_params['location_id'] = params['location_id']

        query_params = {}

        header_params = {}
        header_params['Square-Version'] = "2018-12-05"
        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CreateOrderResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        

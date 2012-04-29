#!/usr/bin/env python
# coding: utf-8

from django.utils.html import strip_spaces_between_tags as short

__all__ = ['SpacelessMiddleware']


class SpacelessMiddleware(object):
    def process_response(self, request, response):
        if 'text/html' in response['Content-Type']:
            response.content = short(response.content)
        return response

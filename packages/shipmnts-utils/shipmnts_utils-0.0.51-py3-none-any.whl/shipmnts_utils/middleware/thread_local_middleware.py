# coding: utf-8

"""
    threadlocals middleware
    ~~~~~~~~~~~~~~~~~~~~~~~
    make the request object everywhere available (e.g. in model instance).
    based on: http://code.djangoproject.com/wiki/CookBookThreadlocalsAndUser
    Put this into your settings:
    --------------------------------------------------------------------------
        MIDDLEWARE_CLASSES = (
            ...
            'django_tools.middlewares.ThreadLocal.ThreadLocalMiddleware',
            ...
        )
    --------------------------------------------------------------------------
    Usage:
    --------------------------------------------------------------------------
    from django_tools.middlewares import ThreadLocal
    # Get the current request object:
    request = ThreadLocal.get_current_request()
    # You can get the current user directly with:
    user = ThreadLocal.get_current_user()
    --------------------------------------------------------------------------
    :copyleft: 2009-2017 by the django-tools team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""
import json
import logging
import base64

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object  # fallback for Django < 1.10


_thread_locals = local()


def get_current_request():
    """ returns the request object for this thread """
    return getattr(_thread_locals, "request", None)


def get_current_user():
    """ returns the current user, if exist, otherwise returns None """
    request = get_current_request()
    if request:
        return getattr(request, "user", None)


def get_job_id():
    """ returns the current user, if exist, otherwise returns None """
    request = get_current_request()
    if request:
        return getattr(request, "job_id", None)

local = local()


class ThreadLocalMiddleware(MiddlewareMixin):
    """ Simple middleware that adds the request object in thread local storage."""

    def process_request(self, request):
        job_id = None
        if request.method == 'POST':
            if request.body and request.content_type == 'application/json':
                data = json.loads(request.body.decode('utf-8'))
                if 'message' in data:
                    if 'messageId' in data['message']:
                        published_data = json.loads(
                        base64.b64decode(
                            data["message"]["data"]).decode("utf-8")
                    )   
                        print(published_data, 'published_datapublished_data')
                        if 'job_id' in published_data:
                            job_id = published_data['job_id']
                        if 'master_document_id' in published_data:
                            master_document_id = published_data['master_document_id']
                            print(master_document_id, 'master_document_idmaster_document_idmaster_document_id')
                            setattr(local, 'master_document_id', master_document_id)
                            print(local, 'locaaaaas')
                        if 'page_id' in published_data:
                            page_id = published_data['page_id']
                            setattr(local, 'page_id', page_id)

                if 'job_id' in data:
                    job_id = data['job_id']
        elif request.method == 'GET':
            uri = request.path.split('/')
            if 'job' in uri:
                index_of_job = uri.index('job')
                job_id = uri[index_of_job+1]

        setattr(local, 'job_id', job_id)

    def process_response(self, request, response):
        setattr(local, 'job_id', None)
        return response

class JobIdFilter(logging.Filter):
    def filter(self, record):
        record.job_id = getattr(local, 'job_id', None)
        return True

class MasterDocumentIdFilter(logging.Filter):
    def filter(self, record):
        print(record, 'recordddddd')
        record.master_document_id = getattr(local, 'master_document_id', None)
        print(record, 'after recordddddd')
        return True

class PageIdFilter(logging.Filter):
    def filter(self, record):
        record.page_id = getattr(local, 'page_id', None)
        return True
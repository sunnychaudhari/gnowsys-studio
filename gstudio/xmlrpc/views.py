"""Uses SimpleXMLRPCServer's SimpleXMLRPCDispatcher to serve XML-RPC requests

Authors::
    Graham Binns
    Reza Mohammadi
    Julien Fache

Credit must go to Brendan W. McAdams <brendan.mcadams@thewintergrp.com>, who
posted the original SimpleXMLRPCDispatcher to the Django wiki:
http://code.djangoproject.com/wiki/XML-RPC

New BSD License
===============
Copyright (c) 2007, Graham Binns http://launchpad.net/~codedragon

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the name of the <ORGANIZATION> nor the names of its contributors
      may be used to endorse or promote products derived from this software
      without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import sys

import django
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse, HttpResponseServerError
from gstudio.xmlrpc.metaweblog import *
from django.utils.datastructures import SortedDict
try:
    from django.views.decorators.csrf import csrf_exempt
except ImportError:
    from django.contrib.csrf.middleware import csrf_exempt

from dispatcher import DjangoXMLRPCDispatcher
from decorators import xmlrpc_func


# We create a local DEBUG variable from the data in settings.
DEBUG = hasattr(settings, 'XMLRPC_DEBUG') and settings.XMLRPC_DEBUG

# Declare xmlrpcdispatcher correctly depending on our python version
if sys.version_info[:3] >= (2, 5,):
    xmlrpcdispatcher = DjangoXMLRPCDispatcher(allow_none=True, encoding=None)
else:
    xmlrpcdispatcher = DjangoXMLRPCDispatcher()


def request_datas(request):
    if django.VERSION[1] > 3:
        return request.body
    return request.raw_post_data


@xmlrpc_func(returns='string', args=['string'])
def test_xmlrpc(text):
    """Simply returns the args passed to it as a string"""
    return "Here's a response! %s" % str(text)


@csrf_exempt
def handle_xmlrpc(request):
    """Handles XML-RPC requests. All XML-RPC calls should be forwarded here

    request
        The HttpRequest object that carries the XML-RPC call. If this is a
        GET request, nothing will happen (we only accept POST requests)
    """
    if request.method == "POST":
        if DEBUG:
            print request_datas(request)
        try:
            response = HttpResponse(content_type='text/xml')
            response.write(
                xmlrpcdispatcher._marshaled_dispatch(request_datas(request)))
            if DEBUG:
                print response
            return response
        except:
            return HttpResponseServerError()
    else:
        methods = xmlrpcdispatcher.system_listMethods()
        method_list = []

        for method in methods:
            sig_ = xmlrpcdispatcher.system_methodSignature(method)
            sig = {
                'returns': sig_[0],
                'args': ", ".join(sig_[1:]),
            }

            # this just reads your docblock, so fill it in!
            method_help = xmlrpcdispatcher.system_methodHelp(method)

            method_list.append((method, sig, method_help))

        if hasattr(settings, 'XMLRPC_GET_TEMPLATE'):
            # This behaviour is deprecated
            if settings.DEBUG:
                print "Use of settings.XMLRPC_GET_TEMPLATE is deprecated " \
                    + "Please update your code to use django_xmlrpc/templates"
            template = settings.XMLRPC_GET_TEMPLATE
        else:
            template = 'xmlrpc_get.html'
        return render_to_response(template, {'methods': method_list},
                                  context_instance=RequestContext(request))


# Load up any methods that have been registered with the server in settings
if hasattr(settings, 'XMLRPC_METHODS'):
    for path, name in settings.XMLRPC_METHODS:
        # if "path" is actually a function, just add it without fuss
        if callable(path):
            xmlrpcdispatcher.register_function(path, name)
            continue

        # Otherwise we try and find something that we can call
        i = path.rfind('.')
        module, attr = path[:i], path[i + 1:]

        try:
            mod = __import__(module, globals(), locals(), [attr])
        except ImportError, ex:
            raise ImproperlyConfigured("Error registering XML-RPC method: " \
                + "module %s can't be imported" % module)

        try:
            func = getattr(mod, attr)
        except AttributeError:
            raise ImproperlyConfigured('Error registering XML-RPC method: ' \
                + 'module %s doesn\'t define a method "%s"' % (module, attr))

        if not callable(func):
            raise ImproperlyConfigured('Error registering XML-RPC method: ' \
                + '"%s" is not callable in module %s' % (attr, module))

        #xmlrpcdispatcher.register_function(func, name)
# Registration for Gnowsys-studio XMLRPC functions
	xmlrpcdispatcher.register_function(getNodetype,'getNodetype')
        xmlrpcdispatcher.register_function(nidExists,'nidExists')
	xmlrpcdispatcher.register_function(getinfoFromSSID,'getinfoFromSSID')
	xmlrpcdispatcher.register_function(getNeighbourhood,'getNeighbourhood')
        xmlrpcdispatcher.register_function(get_nbh,'get_nbh')
	xmlrpcdispatcher.register_function(getAll,'getAll')
        xmlrpcdispatcher.register_function(getDatatype,'getDatatype')
        xmlrpcdispatcher.register_function(getAttributevalues,'getAttributevalues')
        xmlrpcdispatcher.register_function(getSubjecttypes,'getSubjecttypes')
        xmlrpcdispatcher.register_function(getAttributeType,'getAttributeType')
	xmlrpcdispatcher.register_function(getRoles,'getRoles')
        xmlrpcdispatcher.register_function(getSubtypes,'getSubtypes')
        xmlrpcdispatcher.register_function(getAllSubtypes,'getAllSubtypes')
        xmlrpcdispatcher.register_function(getRestrictions,'getRestrictions')
        xmlrpcdispatcher.register_function(getlatestSSID,'getlatestSSID')
        xmlrpcdispatcher.register_function(getAllSnapshots,'getAllSnapshots')
        xmlrpcdispatcher.register_function(setAttributetype,'setAttributetype')
        xmlrpcdispatcher.register_function(setRelationtype,'setRelationtype')
        xmlrpcdispatcher.register_function(setObjecttype,'setObjecttype')
        xmlrpcdispatcher.register_function(setObject,'setObject')
        xmlrpcdispatcher.register_function(setAttribute,'setAttribute')
        xmlrpcdispatcher.register_function(setRelation,'setRelation')
        xmlrpcdispatcher.register_function(getGbobjectNeighbourhood,'getGbobjectNeighbourhood')
	
	

        


# Finally, register the introspection and multicall methods with the XML-RPC
# namespace
xmlrpcdispatcher.register_introspection_functions()
xmlrpcdispatcher.register_multicall_functions()

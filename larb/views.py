from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):

    return render_to_response("larb/index.html",
                              RequestContext(request))

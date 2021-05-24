from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def notfound(request, exception):
    template = loader.get_template('404.html')
    context = Context({
        'message': 'All: %s' % request,
        })
    return HttpResponse(content=template.render(context),content_type='text/html; charset=utf-8', status=404)
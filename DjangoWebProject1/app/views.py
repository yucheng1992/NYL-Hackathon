"""
Definition of views.
"""

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from . import models

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    if request.POST:
        for each in models.MasterTable.objects.all():
            each.delete()
        models.load_data('table.xls')
    zipcode = request.GET.get('zip','')
    gender = request.GET.get('gender','')
    esda = request.GET.get('esda','')
    rows = models.MasterTable.objects.all()

    if gender:
        gender = True if gender == 'M' else False
    if zipcode:
        rows = rows.filter(zipcode=zipcode)
    if gender in [True, False]:
        rows = rows.filter(is_male=gender)
    if esda:
        rows = rows.filter(esda=esda)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'rows': rows,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

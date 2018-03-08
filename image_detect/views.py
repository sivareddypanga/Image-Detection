# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def model (request):
	return render(request, "image_detect/model.html" )

def image_upload (request):
	return render(request, "image_detect/image_upload.html" )

def result(request):
	return render(request, "image_detect/results.html" )

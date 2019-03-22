from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse
from django import forms
from django.db import connection
#cursor = DjangoWebLogin.settings.cnxn.cursor()
from django.db import models
from django.shortcuts import render
from django.db import connection
from django.urls import reverse
import json
import re

def index(request):
       return HttpResponse('<h1>test</h1>')

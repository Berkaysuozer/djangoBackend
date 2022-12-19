from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Members
from django.urls import reverse
from django.template import loader

# Create your views here.

def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['username']
  y = request.POST['tweet']
  member = Members(username=x, tweet=y)
  member.save()
  return HttpResponseRedirect(reverse(index))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse(index))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  username = request.POST['username']
  tweet = request.POST['tweet']
  member = Members.objects.get(id=id)
  member.username = username
  member.tweet = tweet
  member.save()
  return HttpResponseRedirect(reverse(index))

def testing(request):
  mydata = Members.objects.all()
  template = loader.get_template('test.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
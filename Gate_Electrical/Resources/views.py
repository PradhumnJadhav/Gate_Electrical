 
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def sayHelo(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def resources(request):
  template = loader.get_template('resources.html')
  return HttpResponse(template.render())

def resources_machines(request):
  template = loader.get_template('machines.html')
  return HttpResponse(template.render())


def resources_machines_lecture(request):
  template = loader.get_template('machine_lecture.html')
  return HttpResponse(template.render())

def resources_system_lecture(request):
  template = loader.get_template('system_lecture.html')
  return HttpResponse(template.render())


def resources_pe_lecture(request):
  template = loader.get_template('power_elec.html')
  return HttpResponse(template.render())
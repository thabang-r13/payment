from django.http import HttpResponse
from django.template import loader

# Create your views here.
def user_portal(request):
  template = loader.get_template('user_portal.html')
  return HttpResponse(template.render())
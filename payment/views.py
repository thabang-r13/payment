from django.http import HttpResponse
from django.template import loader

# Create your views here.
def payment(request):
  template = loader.get_template('payment.html')
  return HttpResponse(template.render())
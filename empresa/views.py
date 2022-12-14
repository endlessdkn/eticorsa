from django.http import Http404, HttpResponse
from django.template import loader
from empresa.models import Empresa

# Create your views here
def index(request):
  myempresa = Empresa.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'myempresa': myempresa,
  }
  return HttpResponse(template.render(context, request))
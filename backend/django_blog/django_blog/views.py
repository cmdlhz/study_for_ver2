from django.http import HttpResponse

def homepage(request):
  return HttpResponse('HOMEPAGE')
  
def about(request):
  return HttpResponse('ABOUT')
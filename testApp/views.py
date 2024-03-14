from django.shortcuts import render
from django.http import HttpResponse
from .testing.main import run_queries
from urllib.parse import urlparse
import requests

def valid_url(url):
    try:
        response = requests.head(url)
        return 200 <= response.status_code < 300
    except:
        return False


# Create your views here.
def home(request):
    # return HttpResponse("This is the graphql testing application, just getting a simple start")
    return render(request,'test.html')

def homeRequest(request):
    return HttpResponse("The application start is as healthy as the development machine")
def requestTest(request):
    # resp = run_queries('http://localhost/graphql',forced_scan=True)
    return HttpResponse("running")

def requestHandler(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        result = ''
        context = {}
        if not urlparse(user_input).scheme:
            result = "Urls Missing scheme (http:// lor https://). Ensure url contains some scheme. "
            error = True
            context['result'] = result
            context['error'] = error

        elif not valid_url(user_input):
             result = "Enter a valid URL"
             context['result'] = result
             error = True
            
        else:
            result = run_queries(user_input,forced_scan=True)
            context['result'] = result
            
        print('here are your results',result)

        return render(request,'test.html',context=context)
    else:
        return HttpResponse("invalid Query")
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib.parse import urlparse
from django.http.response import HttpResponse
import sys
import requests
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework import status
from testApp.testing.main import run_queries,testCSRF,testDDOs,testInfodisclosure

def valid_url(url):
    try:
        response = requests.head(url)
        print(response)
        return 200 <= response.status_code < 300
    except:
        return False


# from testing.main import run_queries

@api_view(['GET'])
def getRoutes(request):
    routes =[
        'GET /api/request',
        'GET /api/request[url]',
    ]
    print(sys.path)
    return Response(routes)

@api_view(['GET','POST'])
def generalTest(request):
    url = request.data.get('url')
    finalResult = {
         'resultx':"",
        'error':False
    }
    print("url is",url)
    finalResult['resultx'] = ''
    finalResult['error'] = False
    if not urlparse(url=url).scheme:
        finalResult['resultx'] = "Urls Missing scheme (http:// lor https://). Ensure url contains some scheme. "
        finalResult['error'] = True
    # elif not valid_url(url=url):
    #          finalResult['resultx'] = f"We could not reach your endpoint.The server might be receiving too many request or you have entered a wrong url. You provide \"{url}\" as your url"
    #          finalResult['error'] = True
            
    else:
        finalResult['resultx'] = run_queries(url=url,forced_scan=True)
    
    print("Results",finalResult['resultx'])
    
    if finalResult['resultx'] == "":
         finalResult['resultx']="application seems not vulnerable to any attack"


    return Response(finalResult)

@api_view(['GET','POST'])
def testDDOS(request):
    url = request.data.get('url')
    finalResult = {
         'resultx':"",
        'error':False
    }
    print("url is",url)
    finalResult['resultx'] = ''
    finalResult['error'] = False
    if not urlparse(url=url).scheme:
        finalResult['resultx'] = "Urls Missing scheme (http:// lor https://). Ensure url contains some scheme. "
        finalResult['error'] = True
    # elif not valid_url(url=url):
    #          finalResult['resultx'] = f"An error occured please check the value of your url. You provide \"{url}\" as your url"
    #          finalResult['error'] = True
            
    else:
        finalResult['resultx'] = testDDOs(url=url,forced_scan=True)
    
    print("Results",finalResult['resultx'])
    if finalResult['resultx'] == "":
         finalResult['resultx']="application seems not vulnerable to ddos attack"

    return Response(finalResult)

@api_view(['GET','POST'])
def testInfoDisclosure(request):
    url = request.data.get('url')
    finalResult = {
         'resultx':"",
        'error':False
    }
    print("url is",url)
    finalResult['resultx'] = ''
    finalResult['error'] = False
    if not urlparse(url=url).scheme:
        finalResult['resultx'] = "Urls Missing scheme (http:// lor https://). Ensure url contains some scheme. "
        finalResult['error'] = True
    # elif not valid_url(url=url):
    #          finalResult['resultx'] = f"An error occured please check the value of your url. You provide \"{url}\" as your url"
    #          finalResult['error'] = True
            
    else:
        finalResult['resultx'] = testInfodisclosure(url=url,forced_scan=True)
    
    print("Results",finalResult['resultx'])
    
    if finalResult['resultx'] == "":
        finalResult['resultx']="application seems not vulnerable to information disclosure"
  


    return Response(finalResult)

@api_view(['GET','POST'])
def testCsrf(request):
    url = request.data.get('url')
    finalResult = {
         'resultx':"",
        'error':False
    }
    print("url is",url)
    finalResult['resultx'] = ''
    finalResult['error'] = False
    if not urlparse(url=url).scheme:
        finalResult['resultx'] = "Urls Missing scheme (http:// lor https://). Ensure url contains some scheme. "
        finalResult['error'] = True
    # elif not valid_url(url=url):
    #          finalResult['resultx'] = f"An error occured please check the value of your url. You provide \"{url}\" as your url"
    #          finalResult['error'] = True
            
    else:
        finalResult['resultx'] = testCSRF(url=url,forced_scan=True)
    
    print("Results",finalResult['resultx'])
    if finalResult['resultx'] == "":
         finalResult['resultx']="application seems not vulnerable to CSRF attack"
    return Response(finalResult)


@api_view(['POST','GET'])
def obtainJwtToken(request):
     email = request.data.get('email')
     password = request.data.get('password')

     if email is None or password is None:
          return JsonResponse({'error':'please provide both email and password'})
     user = authenticate(email=email,password=password)

     if user is None:
          return JsonResponse({'error':'Invalid credentials'},status=400)
     refresh = RefreshToken.for_user(user)
     access_token = str(refresh.access_token)
     return JsonResponse({'error':'','access_token':access_token})

@api_view(['POST'])
def registration(request):
     serializer = UserSerializer(data=request.data)

     if serializer.is_valid():
          serializer.save()
          return JsonResponse({"data":serializer.data,'status':status.HTTP_201_CREATED})
     return JsonResponse({'data':serializer.errors,'status':status.HTTP_400_BAD_REQUEST})
     
from django.shortcuts import render, HttpResponse
from pgn_db.settings import INCLUDE_KEYS
from models import User
import urllib
import requests
# Create your views here

def search_view(request):
    user = User.objects.get(first_name="Darius")
    return render(request, 'search.html', {"member": user})

def login_view(request):
    return render(request, 'login.html')

def create_user(request):
    data = request.POST['data']
    (status, user_data) = User.sync(data)
    if status == "success":
        user = User(**user_data)
        user.save()
        render(request, 'search.html')
    else:
        return HttpResponse("Not a PGN Member, if this is in error please contact the chapter.")



def register_view(request):

    url = 'https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id='+INCLUDE_KEYS['LinkedIn']['API_KEY']+'&redirect_uri='+urllib.quote('http://127.0.0.1:8000/auth/linkedin/callback',"")+'&state='+INCLUDE_KEYS['CSRF']+'&scope=r_basicprofile'
    return render(request, 'twitter_auth.html', {"twitter_redirect":url})

def linkedin_callback(request):
    if 'code' in request.GET:
        if request.GET['state'] == INCLUDE_KEYS['CSRF']:
            code = request.GET['code']

            data = {
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": "http://127.0.0.1/auth/linkedin/callback",
                "client_id": INCLUDE_KEYS['LinkedIn']['API_KEY'],
                "client_secret": INCLUDE_KEYS["LinkedIn"]['API_SECRET']
            }
            requests.post("https://www.linkedin.com/uas/oauth2/accessToken", headers={"Content-Type": "application/x-www-form-urlencoded"}, params=data)
        else:
            return HttpResponse("Unauthorized", status=401)
    elif 'access_token' in request.GET:
        return render(request, 'register.html', {"access_token": request.GET['access_token']})
    else:
        return HttpResponse("Page Not Found", status=404)
    return render(request, 'search.html')
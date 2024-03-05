# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
# from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...
@csrf_exempt
def logout_request(request):
    # data = json.loads(request.body)
    # print(f"logout request data: {data}")
    username = ""
    return JsonResponse({"username": username})


# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
# ...
# @csrf_exempt
# def registration(request):
#     data=json.loads(request.data)
#     username = data["userName"]
#     password: data["password"],
#     first_name: data["firstName"],
#     last_name: data["lastName"],
#     email: data["email"]
#     username_exist = false
#     email_exist = false
#     try: 
#         User.objects.get(email=email)
#         email_exist=true
#         User.objects.get(username=username)
#         username_exist = true

#     except:
#         logger.debug("{} is new user".format(username))

#     if not email_exist and not username_exist:
#         user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
#         login(request, user)
#         data = {"userName":username,"status":"Authenticated"}
#         return JsonResponse(data)
#     else:
#         data = {"userName": username, "error": "Username or Email already exists" }
#         return JsonResponse(data)
    
@csrf_exempt
def registration(request):
    context = {}

    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    email_exist = False
    try:
        # Check if user already exists
        User.objects.get(username=username)
        username_exist = True
    except:
        # If not, simply log this is a new user
        logger.debug("{} is new user".format(username))

    # If it is a new user
    if not username_exist:
        # Create user in auth_user table
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password, email=email)
        # Login the user and redirect to list page
        login(request, user)
        data = {"userName":username,"status":"Authenticated"}
        return JsonResponse(data)
    else :
        data = {"userName":username,"error":"Already Registered"}
        return JsonResponse(data)
# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...

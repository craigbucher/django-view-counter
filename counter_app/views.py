from django.shortcuts import render
from django.http import HttpResponse
import random

users = {}

def index(request):
    # check for exsiting cookie/session
    user_id = request.COOKIES.get('user_id')
    user = users.get(user_id)

    # if no cookie, generate a random value for the user_id
    if not user: 
        user_id = str(random.randint(10000000, 99999999))

        users[user_id] = {
            # set the count to 1
            'count': 1
        }
    else:
        # if the user has an existing session, increment the count by 1
        users[user_id]['count'] += 1

    #return the response, setting the cookie for the user)id
    response = render(request, 'counter_app/index.html', users[user_id])
    response.set_cookie('user_id', user_id)
    return response
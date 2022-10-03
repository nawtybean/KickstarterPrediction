import pickle
import pandas as pd
import numpy as np
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, JSONParser

from kickstarter.models import Category, Country

from system_management.utilities import *

from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()

def landing(request):
    context = {}
    return render(request, "kickstarter/kickstarter.html", context)


def api(request):
    context = {}
    return render(request, "kickstarter/api.html", context)


class Kickstarter(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (JSONParser, MultiPartParser )

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':

            category = list(Category.objects.all().values())
            category = select_data(category, 'name')
            country = list(Country.objects.all().values())
            country = select_data(country, 'name')

            data = {
                "category": category,
                "country": country
            }
            return Response(data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # initialize varibles
            backers_count = 0
            campaign_duration_days = 0
            char_count = 0
            country_theUnitedKingdom = 0
            country_theUnitedStates = 0
            goal_usd = 0
            parent_category_Comics = 0
            parent_category_Crafts = 0
            parent_category_Design = 0
            parent_category_Fashion = 0
            parent_category_FilmandVideo = 0
            parent_category_Food = 0
            parent_category_Games = 0
            parent_category_Journalism = 0
            parent_category_Music = 0
            parent_category_Photography = 0
            parent_category_Publishing = 0
            parent_category_Technology = 0
            staff_pick_True = 0

            # get the data
            backers_count = int(request.data['backers'])
            campaign_duration_days = int(request.data['campaign'])
            char_count = request.data['description']
            char_count = len(char_count)
            goal_usd = int(request.data['goal'])
            category = int(request.data['category'])
            country = int(request.data['country'])

            if country == 1:
                country_theUnitedStates = 1
            elif country == 2:
                country_theUnitedKingdom = 1
            else:
                country_theUnitedKingdom = 0
                country_theUnitedStates = 0

            if category == 1:
                parent_category_Comics = 1
            elif category == 2:
                parent_category_Crafts = 1
            elif category == 3:
                parent_category_Design = 1
            elif category == 4:
                parent_category_Fashion = 1
            elif category == 5:
                parent_category_FilmandVideo = 1
            elif category == 6:
                parent_category_Food = 1
            elif category == 7:
                parent_category_Games = 1
            elif category == 8:
                parent_category_Journalism = 1
            elif category == 9:
                parent_category_Music = 1
            elif category == 10:
                parent_category_Photography = 1
            elif category == 12:
                parent_category_Publishing = 1
            elif category == 12:
                parent_category_Technology = 1

            try:
                staff_pick_True = request.data['staff_pick']
                print(staff_pick_True)
                if staff_pick_True == 'on':
                    staff_pick_True = 1
                else:
                    staff_pick_True = 0
            except:
                staff_pick_True = 0
            
            # assign the variables
            country_theUnitedKingdom = country_theUnitedKingdom
            country_theUnitedStates = country_theUnitedStates
            parent_category_Comics = parent_category_Comics
            parent_category_Crafts = parent_category_Crafts
            parent_category_Design = parent_category_Design
            parent_category_Fashion = parent_category_Fashion
            parent_category_FilmandVideo = parent_category_FilmandVideo
            parent_category_Food = parent_category_Food
            parent_category_Games = parent_category_Games
            parent_category_Journalism = parent_category_Journalism
            parent_category_Music = parent_category_Music
            parent_category_Photography = parent_category_Photography
            parent_category_Publishing = parent_category_Publishing
            parent_category_Technology = parent_category_Technology
            staff_pick_True = staff_pick_True

            # build the data object
            data = [{'backers_count': backers_count,
                    'campaign_duration_days': campaign_duration_days,
                    'char_count': char_count,
                    'country_the United Kingdom': country_theUnitedKingdom,
                    'country_the United States': country_theUnitedStates,
                    'goal_usd': goal_usd,
                    'parent_category_Comics': parent_category_Comics,
                    'parent_category_Crafts': parent_category_Crafts,
                    'parent_category_Design': parent_category_Design,
                    'parent_category_Fashion': parent_category_Fashion,
                    'parent_category_Film & Video': parent_category_FilmandVideo,
                    'parent_category_Food': parent_category_Food,
                    'parent_category_Games': parent_category_Games,
                    'parent_category_Journalism': parent_category_Journalism,
                    'parent_category_Music': parent_category_Music,
                    'parent_category_Photography': parent_category_Photography,
                    'parent_category_Publishing': parent_category_Publishing,
                    'parent_category_Technology': parent_category_Technology,
                    'staff_pick_True': staff_pick_True }]

            # create a dataframe
            df = pd.DataFrame(data)
            # load the model
            with open(settings.BASE_DIR + '\\kickstarter\\model\\svc_model.pkl', 'rb') as f:
                model = pickle.load(f)
            # scale
            X = df
            X[['backers_count', 'campaign_duration_days', 'char_count', 'goal_usd']] = \
                np.log10(X[['backers_count', 'campaign_duration_days', 'char_count', 'goal_usd']])
            
            prediction = model.predict(X)[0]
            if prediction == 0:
                prediction = 'Fail'
            else:
                prediction = 'Successful'
            data = {
                "prediction": prediction,
                "character_count": char_count,
                "two_part_title": 'yes'
            }
            return Response(data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
from django.urls import path
from kickstarter import views
from kickstarter.views import (
    Kickstarter
)


urlpatterns = [
    path('landing', views.landing, name='landing'),
    path('api', views.api, name='api'),
    path('kickstarter/', Kickstarter.as_view(), name='kickstarter'),

]

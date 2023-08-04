"""
URL configuration for MyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from MyApp.Apis import TopicRestApi,ContentRestApi,PostCategoriesRestApi,StatesRestApi,CitysRestApi,LocationRestApi

urlpatterns = [
                     # Topic Apis

    path('api/topic', TopicRestApi.TopicApis.as_view()),  # GET AND POST data in apis/topic
    path('api/topic/udatedelete/<int:pk>/', TopicRestApi.TopicApiUpdateDeleteApi.as_view()), # update/delete/ data in apis/topic

                     # Content Apis

    path('api/content', ContentRestApi.contentApis.as_view()),  # GET AND POST data in apis/content
    path('api/content/udatedelete/<int:pk>/', ContentRestApi.ContentApiUpdateDeleteApi.as_view()), # update/delete/ data in apis/content

                      # Post Category Api
    path('api/postcateger', PostCategoriesRestApi.PostCateApi.as_view()),
    path('api/postcateger/<int:pk>', PostCategoriesRestApi.PostCateApi.as_view()), 

                     # State Apis
    path('api/states', StatesRestApi.StateApi.as_view()),
    path('api/states', StatesRestApi.StateUpdateDeleteApi.as_view()), 
                      

                     # City Apis
    path('api/states', CitysRestApi.CityApi.as_view()),
    path('api/states/<int:pk>/', CitysRestApi.CityUpdateDeleteApi.as_view()),  
    
                     #  Locations API  
                     
    path('api/locations', LocationRestApi.LocationApi.as_view()),
    path('api/locations/<int:pk>/', LocationRestApi.LocationUpdateDeleteApi.as_view()),  
                      
 
                     
                     
    # path('api/Image', ImageRestApi.ImageApi.as_view()),
    
        
]

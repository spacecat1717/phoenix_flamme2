from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views



app_name = 'main'
urlpatterns = [
    #basic urls
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('categories/category/<item_id>/', views.item, name="item"),
    path('categories/<category_id>/collections', views.collections, name='collections'),
    path('categories/category/<collection_id>', views.collection, name='collection'),
    
    path('contacts/', views.contacts, name='contacts'),
    path('info/', views.info, name='info'),
    path('policy/', views.policy, name='policy'),
    #topics urls
    path('topics/', views.topics, name='topics'),
    path('topics/<topic_id>/', views.topic, name='topic'),
    #feedback urls
    path('feedbacks/', views.feedback_list, name='feedback_list'),
    path('feedbacks/new_feedback/', views.add_feedback, name='add_feedback'),
   
]
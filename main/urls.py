from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views



app_name = 'main'
urlpatterns = [
    #basic urls
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('categories/<category_id>/', views.category, name='category'),
    path('categories/category/<item_id>/', views.item, name="item"),
    path('contacts/', views.contacts, name='contacts'),
    #topics urls
    path('topics/', views.topics, name='topics'),
    #feedback urls
    path('feedbacks/', views.feedback_list, name='feedback_list'),
    path('feedbacks/new_feedback/', views.add_feedback, name='add_feedback'),
   
]
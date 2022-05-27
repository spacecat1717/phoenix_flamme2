from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('categories/<category_id>/', views.category, name='category'),
    path('topics/', views.topics, name='topics'),
    path('categories/category/<item_id>/', views.item, name="item"),
    path('categories/category/item/change_quan/<item_id>/', views.change_quantity, name='change_quan')
    
    



]
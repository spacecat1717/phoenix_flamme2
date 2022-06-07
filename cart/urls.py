from django.conf.urls import url
from . import views

app_name = 'cart'
urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<item_id>\d+)/$', views.cart_add, name='cart_add'),
    url('^remove/(?P<item_id>\d+)?$', views.cart_remove, name='cart_remove'),
    

]
from django.urls import path, include
from . import views


app_name='cart'

    #добавить ф-цию очистки корзины
    #path('cart/<int:pk>/delete/', views.DeleteCart.as_view(), name='delete-cart'),


urlpatterns = [
    path('cart/', views.DetailCart.as_view(), name='detail_cart'),
    #path('cartitem/create/', views.CreateCartItem.as_view(), name='create-cartitem'),
    #path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(), name='delete-cartitem'),
]
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from main.views import (HomeView, AboutView, ContactView, ProductView, Single_ProductView, ShoppingCartTemplateView,
                         IncrementCountAPIView, DecrementCountAPIView, ChangeCountAPIView, AddProductView, CommentView, OrderView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('products', ProductView.as_view(), name='products'),
    path('single-product', Single_ProductView.as_view(), name='single-product'),
    path('checkout', OrderView.as_view(), name='checkout'),
    path('cart', ShoppingCartTemplateView.as_view(), name='cart'),
    path('add-product', AddProductView.as_view(), name='add-product'),
    # API
    path('increment', csrf_exempt(IncrementCountAPIView.as_view()), name='increment'),
    path('decrement', csrf_exempt(DecrementCountAPIView.as_view()), name='decrement'),
    path('change', csrf_exempt(ChangeCountAPIView.as_view()), name='change'),
]












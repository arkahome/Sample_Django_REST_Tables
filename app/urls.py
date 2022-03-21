from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()

router.register(r'order', views.OrderViewSet)
router.register(r'order_details', views.OrderDetailViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'factory_table', views.FtyTableViewSet)



urlpatterns = [
    path('', views.home, name="home"),
    path('login/',views.app_login, name="login"),
    path('logout/',views.app_logout, name="logout"),
    path('register/',views.register, name="register"),
    path('sample_page/',views.sample_page, name="sample_page"),
    path('order_details/',views.order_details, name="order_details"),
    # path('update_order/<str:pk>/', views.updateOrder, name="update_order"), 
    
    
    path('order/', views.show_order, name="show_order"),
    path('order/update/<str:pk>/', views.update_order, name="update_order"),

    path('product/', views.show_product, name="show_product"),
    path('product/update/<str:pk>/', views.update_product, name="update_product"),

    path('factory_table/create/', views.create_fty_table, name="create_factory_table"), 
    path('factory_table/', views.show_fty_table, name="show_factory_table"),
    path('api/',include(router.urls)),
]
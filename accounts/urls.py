
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('users/', views.users_profile, name="users"),
    path('setting/', views.setting_profile, name="setting"),
    path('customers/<str:pk>/', views.customers, name="customers"),
    path('order_create/', views.order_create, name="order_create"),
    path('customer_order/', views.customer_order, name="customer_order"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

]

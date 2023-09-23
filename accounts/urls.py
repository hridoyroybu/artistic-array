from django.urls import path, include
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    # path('', views.dashboard, name='dashboard'),

    # path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    # path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    # path('resetPassword/', views.resetPassword, name='resetPassword'),

    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('change_password/', views.change_password, name='change_password')


]
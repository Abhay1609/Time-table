
from django.urls import path,include
from  account.views import RegisterView,LoginAPIView,LogoutAPIView, VerifyEmail,PasswordTokenCheckAPI,RequestPasswordRestEmail,SetNewPasswordAPIView
from . import views

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('email-verify/', VerifyEmail.as_view(),name='email-verify'),
    path('login/', LoginAPIView.as_view(),name='login'),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('request-reset-email/', RequestPasswordRestEmail.as_view(), name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    path('lecture',views.lecture_create),
    path('view/<int:pkyear>/<str:pk>/<int:pki>/',
         views.lecture_view),
    path('view_teacher/<str:teacher>',
         views.teacher_view)


]


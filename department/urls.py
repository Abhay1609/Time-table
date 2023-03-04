
from django.urls import path,include
from department import views



urlpatterns = [
    path('lecture', views.lecture_create),
    path('view/<int:pkyear>/<str:pk>/<int:pki>/',
         views.lecture_view),
    path('view_teacher/<str:teacher>',
         views.teacher_view)

]
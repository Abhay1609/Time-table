






from django.urls import path,include
from .views import *



urlpatterns = [
    path('lecture', lecture_create),
    # path('view/<int:pkyear>/<str:pk>/<int:pki>/',lecture_view),
    path('view_teacher/<str:teacher>',teacher_view),
    path('view-time-table/<str:class_id>',Time_Table_Data.as_view()),
    path('view-time-table1/<str:class_id>',TimeTableData),
    path('view_day/<int:day>/<str:class_id>',Time_Table_day),
    path('view_period/',period_view),
    path('create_table/',CreateTable),

]







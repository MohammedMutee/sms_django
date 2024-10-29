from django.urls import path, include
from . import views

urlpatterns =[
     path('', views.projecthomepage, name='projecthomepage'),
     path('printpagecall/', views.printpagecall, name='printpagecall'),
     path('printpagelogic/', views.printpagelogic, name='printpagelogic'),
     path('exceptionpagelogic/', views.exceptionpagelogic, name='exceptionpagelogic'),
     path('exceptionpagecall/', views.exceptionpagecall, name='exceptionpagecall'),
     path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
     path('UserRegistercall/', views.UserRegistercall, name='UserRegistercall'),
     path('add_task/', views.add_task, name='add_task'),
     path('<int:pk>/delete_task/', views.delete_task, name='delete_task'),

     path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
     path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
     path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
     path('logout/', views.logout, name='logout'),
     path('student_list/', views.student_list, name='student_list'),
     path('add_students/', views.add_students, name='add_students'),
     path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
     path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
     path('randomlogic/', views.randomlogic, name='randomlogic'),
     path('randompagecall/', views.randompagecall, name='randompagecall'),
     path('calculatorcall/', views.calculatorcall, name='calculatorcall'),
     path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
     path('csv_to_pie_chart/', views.csv_to_pie_chart, name='csv_to_pie_chart'),
     path('chartpagecall/', views.chartpagecall, name='chartpagecall'),
     path('manage_contacts/', views.manage_contacts, name='manage_contacts'),

]
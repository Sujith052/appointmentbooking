from django.urls import path
from users import views

# url patterns
urlpatterns = [
    path('index', views.index,name='index'),
    path('', views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
    path('signupaction', views.signup_action,name='signupaction'),
    path('signinaction', views.signin_action,name='signinaction'),
    path('appointment', views.appointment,name='appointment'),
    path('gettimeslot/', views.gettimeslot, name='gettimeslot'),
    path('appointment_action', views.appointment_action,name='appointment_action'),
    path('booking_details', views.booking_details,name='booking_details'),
    path('user_logout/', views.user_logout, name='user_logout'),

]
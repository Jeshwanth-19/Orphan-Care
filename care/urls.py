from django.urls import path
from . import views
urlpatterns = [
    path('donor/', views.donor),
     path('services/', views.services),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('signup/', views.signup),
    path('Aboutus/',views.Aboutus),
    path('addregistration.html/',views.addregistration),
    path('details_list/',views.all_list,name="list-events"),
]

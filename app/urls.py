from django.urls import path

from app.views import *

urlpatterns = [

    # //////////////////////////// ADMIN //////////////////////////////////
    path('', LoginPage.as_view(), name="login"),
    path('viewcomplaints', Viewcomplaints.as_view(), name="complaint"),
    path('ManageNGO', ManageNGO.as_view(), name="addnmanageNGO"),
    path('admindashboard', adminDashboard.as_view(), name="dashboard"),
    path('ViewDonation', ViewDonation.as_view(), name="Donation"),
    path('resource', ViewResource.as_view(), name="resource"),
    path('volunteer', ViewVolunteers.as_view(), name="volunteer"),
    path('user', ViewUser.as_view(), name="user"),
    path('disasterupdate', ViewDisasterupdate.as_view(), name="updates"),
    path('addnmanageskill', Addnmanageskill.as_view(), name="addnmanageskill"),
    path('addskill', Addskill.as_view(), name="addskill"),

    # //////////////////////////// NGO //////////////////////////////////

    path('logout', logout.as_view(), name="logout"),
    path('Donationtransaction', Donationtransaction.as_view(), name="Donationtransaction"),
    path('ngodashboard', ngodashboard.as_view(), name="dashboard"),
    path('Viewdisasterdata', Viewdisaster.as_view(), name="viewdisaster"),
    path('Viewresource', ViewResources.as_view(), name="resources"),
    path('volunteerstatus', ViewVolunteerStatus.as_view(), name="volunteerstatus"),
   
]

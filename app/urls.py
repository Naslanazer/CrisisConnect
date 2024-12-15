from django.urls import path

from app.views import *

urlpatterns = [

    # //////////////////////////// ADMIN //////////////////////////////////
    path('', LoginPage.as_view(), name="login"),
    path('viewcomplaints', Viewcomplaints.as_view(), name="complaint"),
    path('ManageNGO', ManageNGO.as_view(), name="addnmanageNGO"),
    path('delete_ngo/<int:id>', DeleteNgo.as_view(), name="delete_ngo"),
    path('admindashboard', adminDashboard.as_view(), name="dashboard"),
    path('ViewDonation', ViewDonation.as_view(), name="Donation"),
    path('delete_donation/<int:id>', DeleteDonation.as_view(), name="delete_Donation"),
    path('resource', ViewResource.as_view(), name="resource"),
    path('dlt_resource/<int:id>', DltResource.as_view(), name="resource"),
    path('editresource/<int:id>', editresource.as_view(), name="Editresource"),
    path('volunteer', ViewVolunteers.as_view(), name="volunteer"),
    path('delete_user/<int:id>', Dltvolunteer.as_view(), name="delete_vltr"),
    path('user', ViewUser.as_view(), name="user"),
    path('dlt_user/<int:id>', DltUser.as_view(), name="dlt_user"),
    path('disasterupdate', ViewDisasterupdate.as_view(), name="updates"),
    path('addisaster', AddDisaster.as_view(), name="Addupdates"),
    path('editDisaster/<int:id>', editDisaster.as_view(), name="Editupdates"),
    path('disasterdelete/<int:id>', DisasterDelete.as_view(), name="disasterdelete"),
    path('addnmanageskill', Addnmanageskill.as_view(), name="addnmanageskill"),
    path('delete_skill/<int:id>', DltSkill.as_view(), name="delete_skill"),
    path('addskill', Addskill.as_view(), name="addskill"),
    path('editSkill/<int:id>', editSkill.as_view(), name="EditSkill"),

    # //////////////////////////// NGO //////////////////////////////////

    path('logout', logout.as_view(), name="logout"),
    path('Donationtransaction', Donationtransaction.as_view(), name="Donationtransaction"),
    path('ngodashboard', ngodashboard.as_view(), name="dashboard"),
    path('Viewdisasterdata', Viewdisaster.as_view(), name="viewdisaster"),
    path('Viewresource', ViewResources.as_view(), name="resources"),
    path('volunteerstatus', ViewVolunteerStatus.as_view(), name="volunteerstatus"),
   
]

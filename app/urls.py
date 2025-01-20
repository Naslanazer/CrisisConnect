from django.urls import path

from app.views import *

urlpatterns = [

    # //////////////////////////// ADMIN //////////////////////////////////
    path('', home.as_view(), name="home"),
    path('logout', Logout.as_view(), name="logout"),
    path('signup', signup.as_view(), name="signup"),
    path('login', LoginPage.as_view(), name="login"),
    path('viewcomplaints', Viewcomplaints.as_view(), name="complaint"),
    path('ManageNGO', ManageNGO.as_view(), name="addnmanageNGO"),
    path('delete_ngo/<int:id>', DeleteNgo.as_view(), name="delete_ngo"),
    path('admindashboard', adminDashboard.as_view(), name="dashboard"),
    path('ViewDonation', ViewDonation.as_view(), name="Donation"),
    path('delete_donation/<int:id>', DeleteDonation.as_view(), name="delete_Donation"),
    path('myresource', MyResource.as_view(), name="myresource"),
    path('resource', ViewResource.as_view(), name="resource"),
    path('dlt_resource/<int:id>', DltResource.as_view(), name="resource"),
    path('editresource/<int:id>', editresource.as_view(), name="Editresource"),
    path('volunteer', ViewVolunteers.as_view(), name="volunteer"),
    path('delete_user/<int:id>', Dltvolunteer.as_view(), name="delete_vltr"),
    path('user', ViewUser.as_view(), name="user"),
    path('dlt_user1/<int:id>', DltUser1.as_view(), name="dlt_user"),
    path('disasterupdate', ViewDisasterupdate.as_view(), name="updates"),
    path('addisaster', AddDisaster.as_view(), name="Addupdates"),
    path('editDisaster/<int:id>', editDisaster.as_view(), name="Editupdates"),
    path('disasterdelete/<int:id>', DisasterDelete.as_view(), name="disasterdelete"),
    path('addnmanageskill', Addnmanageskill.as_view(), name="addnmanageskill"),
    path('delete_skill/<int:id>', DltSkill.as_view(), name="delete_skill"),
    path('addskill', Addskill.as_view(), name="addskill"),
    path('editSkill/<int:id>', editSkill.as_view(), name="EditSkill"),
    path('reply/<int:id>', reply.as_view(), name="Reply"), 
    path('viewtask', viewtask.as_view(), name="viewtask"),
    path('admin_task_delete/<int:id>',admin_task_delete.as_view(), name="admin_task_delete"),
    path('addtask', addtask.as_view(), name="addtask"),



    # //////////////////////////// NGO //////////////////////////////////

    path('Donationtransaction', Donationtransaction.as_view(), name="Donationtransaction"),
    path('delete_donation_ngo/<int:id>', Dlt_Donationtransaction.as_view(), name="delete_donation_ngo"),
    path('ngodashboard', ngodashboard.as_view(), name="dashboard"),
    path('Viewdisasterdata', Viewdisaster.as_view(), name="viewdisaster"),
    path('disaster_delete/<int:id>',Dlt_disaster.as_view(), name="disaster_delete"),
    path('edit_ngoDisaster/<int:id>', editNGODisaster.as_view(), name="edit_ngoDisaster"),
     path('addngodisaster', AddNGODisaster.as_view(), name="Addngoupdates"),
    path('Viewresource', ViewResources.as_view(), name="resources"),
    path('addResource', addResources.as_view(), name="addResource"),
    path('dlt_resource/<int:id>', Dlt_Resources.as_view(), name="dlt_resource"),
    path('edit_ngoResource/<int:id>', editNGOresource.as_view(), name="edit_ngoResource"),
    path('volunteerstatus', ViewVolunteerStatus.as_view(), name="volunteerstatus"),
    path('active_volunteer/<int:id>', active_VolunteerStatus.as_view(), name="active_volunteer"),
    path('inactive_volunteer/<int:id>', inactive_VolunteerStatus.as_view(), name="inactive_volunteer"),
    path('view_task_ngo', view_task_ngo.as_view(), name="view_task_ngo"),
    path('task_delete/<int:id>',task_delete.as_view(), name="task_delete"),
    path('view_volunteer/<int:id>',view_volunteer.as_view(), name="view_volunteer"),
    path('assign_task/<int:id>',assign_task.as_view(), name="assign_task"),
    ################################api################################

    path('LoginAPI', LoginAPI.as_view(), name="LoginAPI"),
    path('UserAPI/<int:id>', UserAPI.as_view(), name="UserAPI"),
    path('profileupdateAPI/<int:id>', profileupdateAPI.as_view(),name="profileupdateAPI"),
    path('DonationAPI/<int:lid>/', DonationAPI.as_view(), name="DonationAPI"),
    path('ComplaintAPI', ComplaintAPI.as_view(), name="ComplaintAPI"),
    path('NGOAPI', NGOAPI.as_view(), name="NGOAPI"),
    path('ResourceAPI',ResourceAPI.as_view(), name="ResourceAPI"),
    path('DisasterAPI', DisasterAPI.as_view(), name="DisasterAPI"),
    path('SkillAPI', SkillAPI.as_view(), name="SkillAPI"),
    path('userregister', userregister.as_view(), name="userregister"),
    path('TaskAPI', TaskAPI.as_view(), name="TaskAPI"),
]
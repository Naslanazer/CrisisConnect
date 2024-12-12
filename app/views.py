
from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from app.models import *

# Create your views here.

# ///////////////////////////////////// ADMIN ////////////////////////////////////

class LoginPage(View):
    def get(self, request):
        return render(request, "login.html")
    def post(self,request):
        username= request.POST['username']
        password= request.POST['password']
        login_obj= LoginTable.objects.get(Username=username, Password=password)
        if login_obj.Type =="admin": 
            return HttpResponse('''<script>alert("Logged in successfully");window.location="/admindashboard"</script>''')
        elif login_obj.Type =="ngo": 
            return HttpResponse('''<script>alert("Logged in successfully");window.location="/ngodashboard"</script>''')
        
class Viewcomplaints(View):
    def get(self, request):
        obj=ComplaintTable.objects.all()
        return render(request, "admin/Viewcomplaints.html",{'val':obj})
    
class ManageNGO(View):
    def get(self, request):
        obj=NGOTable.objects.all()
        return render(request, "admin/AddnManageNGO.html",{'val':obj})
    
class adminDashboard(View):
    def get(self, request):
        obj=DisasterTable.objects.all()
        return render(request, "admin/admindashboard.html",{'val':obj})

    
class ViewDonation(View):
    def get(self, request):
        obj=DonationTable.objects.all()
        return render(request, "admin/ViewDonation.html",{'val':obj})
    
class ViewResource(View):
    def get(self, request):
        obj=ResourceTable.objects.all()
        return render(request, "admin/ViewResources.html",{'val':obj})
    
class ViewVolunteers(View):
    def get(self, request):
        obj=UserTable.objects.filter(Type='volunteer')
        return render(request, "admin/ViewVolunteers.html",{'val':obj})
    
class ViewUser(View):
    def get(self, request):
        obj=UserTable.objects.filter(Type='user')
        return render(request, "admin/ViewUser.html",{'val':obj})
    
class ViewDisasterupdate(View):
    def get(self, request):
        obj=DisasterTable.objects.all() 
        return render(request, "admin/ViewDisasterupdate.html",{'val':obj})
class Addnmanageskill(View):
    def get(self, request):
        obj=SkillTable.objects.all() 
        return render(request, "admin/addnmanageskill.html",{'val':obj})
class Addskill(View):
    def get(self, request):
        obj=SkillTable.objects.all() 
        return render(request, "admin/add_skill.html",{'val':obj})
  

    # //////////////////////////// NGO //////////////////////////////////
    
class logout(View):
    def get(self, request):
        return render(request, "ngo/Logout.html")
    
class Donationtransaction(View):
    def get(self, request):
        return render(request, "ngo/Donationandtransaction.html")
    
class ngodashboard(View):
    def get(self, request):
        return render(request, "ngo/ngodashboard.html")
    
class Viewdisaster(View):
    def get(self, request):
        return render(request, "ngo/Viewdisasterdata.html")
    
    
class ViewResources(View):
    def get(self, request):
        return render(request, "ngo/ViewResourceAvailabilty.html")
    
class ViewVolunteerStatus(View):
    def get(self, request):
        return render(request, "ngo/ViewVolunteerStatus.html")
    

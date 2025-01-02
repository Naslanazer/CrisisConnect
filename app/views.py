
from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import logout

from app.models import *
from.forms import *

# Create your views here.

# ///////////////////////////////////// ADMIN ////////////////////////////////////

class home(View):
    def get(self,request):
        return render(request,"home.html")


class Logout(View):
    def get(self, request):
        # Flush the session data
        request.session.flush()
        # Log out the user
        logout(request)
        # Redirect to the login page
        return redirect("login")
    
class signup(View):
    def get(self, request):
        return render(request, "signup.html")
    def post(self, request):
        form = NGORegForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print("username")
        try:
            obj = LoginTable.objects.get(Username=username,Password=password)
            return HttpResponse('''<script>alert("user already exist");window.location="/"</script>''')

        except:
            if form.is_valid():
                f=form.save(commit=False)
                obj = LoginTable.objects.create(
                Username=request.POST['username'],
                Password=request.POST['password'],
                Type="ngo")
                f.LOGIN=obj
                f.save()
                return HttpResponse('''<script>alert("registered successfully");window.location="/"</script>''')

   
    

class LoginPage(View):
    def get(self, request):
        return render(request, "login.html")
    def post(self,request):
        username= request.POST['username']
        password= request.POST['password']
        login_obj= LoginTable.objects.get(Username=username, Password=password)
        request.session["loginid"]=login_obj.id

        if login_obj.Type =="admin": 
            return HttpResponse('''<script>alert("Logged in successfully");window.location="/admindashboard"</script>''')
        elif login_obj.Type =="ngo": 
            request.session['login_id']=login_obj.id
            return HttpResponse('''<script>alert("Logged in successfully");window.location="/ngodashboard"</script>''')
        
class Viewcomplaints(View):
    def get(self, request):
        obj = ComplaintTable.objects.filter(Reply__isnull=True)  # For NULL values
        return render(request, "administrator/Viewcomplaints.html", {'val': obj})
    
class ManageNGO(View):
    def get(self, request):
        obj=NGOTable.objects.all()
        return render(request, "administrator/AddnManageNGO.html",{'val':obj})

class DeleteNgo(View):
    def get(self, request, id):
        obj = LoginTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/ManageNGO"</script>''')


class adminDashboard(View):
    def get(self, request):
        obj=DisasterTable.objects.all()
        return render(request, "administrator/admindashboard.html",{'val':obj})

    
class ViewDonation(View):
    def get(self, request):
        obj=DonationTable.objects.all()
        return render(request, "administrator/ViewDonation.html",{'val':obj})
class DeleteDonation(View):
    def get(self, request, id):
        obj = DonationTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/ViewDonation"</script>''')
    
class DltResource(View):
    def get(self, request, id):
        obj = ResourceTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/resource"</script>''')     
    
class MyResource(View):
    def get(self, request):
        obj=ResourceTable.objects.filter(LOGIN_id=request.session['login_id'])
        return render(request, "administrator/ViewResource.html",{'val':obj})
class ViewResource(View):
    def get(self, request):
        obj=ResourceTable.objects.all()
        return render(request, "administrator/ViewResources.html",{'val':obj})

class editresource(View):
    def get(self, request,id):
        c= ResourceTable.objects.get(id=id)
        print(c)
        return render(request, "administrator/edit_resource.html",{'c':c, 'date': str(c.Date)})
    def post(self, request,id):
        obj = ResourceTable.objects.get(id=id)
        form = resourcesForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("added successfully");window.location="/resource"</script>''')
   
    
class ViewVolunteers(View):
    def get(self, request):
        obj=UserTable.objects.filter(Type='volunteer')
        return render(request, "administrator/ViewVolunteers.html",{'val':obj})

class Dltvolunteer(View):
    def get(self, request, id):
        obj = LoginTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/volunteer"</script>''')

class ViewUser(View):
    def get(self, request):
        obj=UserTable.objects.filter(Type='user')
        return render(request, "administrator/ViewUser.html",{'val':obj})
class DltUser1(View):
    def get(self, request, id):
        obj = LoginTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/user"</script>''')
    
    
class ViewDisasterupdate(View):
    def get(self, request):
        obj=DisasterTable.objects.all() 
        return render(request, "administrator/ViewDisasterupdate.html",{'val':obj})
    
class AddDisaster(View):
    def get(self, request):
        return render(request, "administrator/add_disaster.html")
    def post(self, request):
        form= disasterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("successfully");window.location="/disasterupdate"</script>''')
        return render(request, "administrator/add_disaster.html")

class editDisaster(View):
    def get(self, request,id):
        c= DisasterTable.objects.get(id=id)
        return render(request, "administrator/edit_disaster.html",{'c':c})
    def post(self, request,id):
        c= DisasterTable.objects.get(id=id)
        form= disasterForm(request.POST, request.FILES,instance=c)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert(" successfully");window.location="/disasterupdate"</script>''')
        return render(request, "administrator/add_disaster.html")

class DisasterDelete(View):
    def get(self, request, id):
        obj = DisasterTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/disasterupdate"</script>''')

class Addnmanageskill(View):
    def get(self, request):
        obj=SkillTable.objects.all() 
        return render(request,"administrator/addnmanageskill.html",{'val':obj})

class DltSkill(View):
    def get(self, request, id):
        obj = SkillTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/addnmanageskill"</script>''')
class Addskill(View):
    def get(self, request):
        return render(request, "administrator/add_skill.html")
    def post(self, request):
        skill = request.POST['skill']
        obj = SkillTable()
        obj.skill=skill
        obj.save()
        return HttpResponse('''<script>alert("added successfully");window.location="/addnmanageskill"</script>''')
   
class editSkill(View):
    def get(self, request,id):
        c= SkillTable.objects.get(id=id)
        print(c)
        return render(request, "administrator/edit_skill.html",{'c':c})

    def post(self, request,id):
        skill = request.POST['skill']
        obj = SkillTable.objects.get(id=id)
        obj.skill=skill
        obj.save()
        return HttpResponse('''<script>alert("added successfully");window.location="/addnmanageskill"</script>''')
   
class reply(View):
    def get(self, request,id):
        c= ComplaintTable.objects.get(id=id)
        print(c)
        return render(request, "administrator/reply.html",{'c':c})

    def post(self, request,id):
        reply = request.POST['reply']
        obj = ComplaintTable.objects.get(id=id)
        obj.Reply=reply
        obj.save()
        return HttpResponse('''<script>alert("added successfully");window.location="/viewcomplaints"</script>''')
   
  
  

    # //////////////////////////// NGO //////////////////////////////////
    
class Donationtransaction(View):
    def get(self, request):
        obj=DonationTable.objects.all()
        return render(request, "ngo/Donationandtransaction.html",{'val':obj})
class Dlt_Donationtransaction(View):
    def get(self, request, id):
        obj = DonationTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/Donationtransaction"</script>''')

    
class ngodashboard(View):
    def get(self, request):
        obj=DonationTable.objects.all()
        return render(request, "ngo/ngodashboard.html")
    
class Viewdisaster(View):
    def get(self, request):
        obj=DisasterTable.objects.all()
        return render(request, "ngo/Viewdisasterdata.html",{'val':obj})
class AddNGODisaster(View):
    def get(self, request):
        return render(request, "ngo/add_disaster1.html")
    def post(self, request):
        form= disasterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert(" successfully");window.location="/disasterupdate"</script>''')
        return render(request, "ngo/add_disaster1.html")

class Dlt_disaster(View):
    def get(self, request, id):
        obj = DisasterTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/Viewdisasterdata"</script>''')
class editNGODisaster(View):
    def get(self, request,id):
        c= DisasterTable.objects.get(id=id)
        return render(request, "administrator/edit_disaster.html",{'c':c})
    def post(self, request,id):
        c= DisasterTable.objects.get(id=id)
        form= disasterForm(request.POST,instance=c)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert(" successfully");window.location="/Viewdisasterdata"</script>''')
        return render(request, "administrator/add_disaster.html")


class addResources(View):
    # def get(self, request):
    #     return render(request, "ngo/add_resources.html")
    def post(self, request):
        id= request.session["loginid"]
        form= resourcesForm(request.POST, request.FILES)
        if form.is_valid():
            form.LOGIN=id
            form.save()
            return HttpResponse('''<script>alert("successfully");window.location="/Viewresource"</script>''')
        return render(request, "ngo/ViewResource.html")
 
class ViewResources(View):
    def get(self, request):
        obj=ResourceTable.objects.exclude(LOGIN_id= request.session['login_id'])
        return render(request, "ngo/ViewResource.html",{'val':obj})
class Dlt_Resources(View):
    def get(self, request, id):
        obj = ResourceTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/Viewresource"</script>''')

class editNGOresource(View):
    def get(self, request,id):
        c= ResourceTable.objects.get(id=id)
        print(c)
        return render(request, "administrator/edit_resource.html",{'c':c, 'date': str(c.Date)})
    def post(self, request,id):
        obj = ResourceTable.objects.get(id=id)
        form = resourcesForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("added successfully");window.location="/Viewresource"</script>''')
   

    
class ViewVolunteerStatus(View):
    def get(self, request):
        obj=UserTable.objects.filter(Type='volunteer')
        return render(request, "ngo/ViewVolunteerStatus.html",{'val':obj})
    
class active_VolunteerStatus(View):
    def get(self, request, id):
        obj = UserTable.objects.get(id=id)
        obj.Status="active"
        obj.save()
        return HttpResponse('''<script>alert("Updated successfully");window.location="/volunteerstatus"</script>''')

class inactive_VolunteerStatus(View):
    def get(self, request, id):
        obj = UserTable.objects.get(id=id)
        obj.Status="inactive"
        obj.save()
        return HttpResponse('''<script>alert("Updated successfully");window.location="/volunteerstatus"</script>''')

    

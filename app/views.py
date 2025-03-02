
from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import logout

from .models import *
from .serializers import ComplaintTableSerializer, ComplaintTableSerializer1, DisasterTableSerializer, DonationTableSerializer, DonationTableSerializer1, LoginTableSerializer, NGOTableSerializer, ResourceTableSerializer, Resourcelimitserializer, SkillTableSerializer, TaskTableSerializer, TaskTableSerializer1, UserTableSerializer, profileupdateAPISerializer
from.forms import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# ///////////////////////////////////// ADMIN ////////////////////////////////////

class home(View):
    def get(self,request):
        volcount=  UserTable.objects.count()
        total_amount = DonationTable.objects.aggregate(total=Sum('Amount'))['total']
        total_amount = total_amount or 0
        ngocount = NGOTable.objects.count()        
        return render(request,"home.html",{'volcount':volcount,'total_amount':total_amount,'ngocount':ngocount},)


class Logout(View):
    def get(self, request):
        # Flush the session data
        request.session.flush()
        # Log out the user
        # logout(request)
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

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            login_obj = LoginTable.objects.get(Username=username, Password=password)
            request.session["loginid"] = login_obj.id  # Store user session

            if login_obj.Type == "admin":
                return HttpResponse('''<script>alert("Logged in successfully"); window.location="/admindashboard";</script>''')
            elif login_obj.Type == "ngo":
                request.session['login_id'] = login_obj.id
                return HttpResponse('''<script>alert("Logged in successfully"); window.location="/ngodashboard";</script>''')

        except LoginTable.DoesNotExist:
            return HttpResponse('''<script>alert("Incorrect username or password"); window.location="/login";</script>''')

        return render(request, "login.html")        
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
        usercount=  UserTable.objects.count()
        total_amount = DonationTable.objects.aggregate(total=Sum('Amount'))['total']
        total_amount = total_amount or 0
        ngocount = NGOTable.objects.count()        
        return render(request, "administrator/admindashboard.html",{'val':obj,'usercount':usercount,'total_amount':total_amount,'ngocount':ngocount})

    
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
        return render(request, "administrator/edit_resource.html",{'c':c, 'date': str(c.Date)})
    def post(self, request,id):
        obj = ResourceTable.objects.get(id=id)
        print('---------------------------',obj)
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
        obj=UserTable.objects.all()
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
   
class viewtask(View):
    def get(self, request):
        obj=TaskTable.objects.all()
        return render(request, "administrator/viewtask.html",{'val':obj})
    
class admin_task_delete(View):
    def get(self, request, id):
        obj = TaskTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/viewtask"</script>''')
    
class addtask(View):
    def get(self, request):
        obj=TaskTable.objects.all()
        return render(request, "administrator/addtask.html",{'val':obj})
    def post(self, request):
        form= taskForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.Status="pending"
            f.save()
            return HttpResponse('''<script>alert("successfully");window.location="/addtask"</script>''')
        return render(request, "administrator/addtask.html")

   
  
  

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
        obj=DisasterTable.objects.all()
        usercount=  UserTable.objects.count()
        total_amount = DonationTable.objects.aggregate(total=Sum('Amount'))['total']
        total_amount = total_amount or 0
        ngocount = NGOTable.objects.count()        
        return render(request, "ngo/ngodashboard.html",{'val':obj,'usercount':usercount,'total_amount':total_amount,'ngocount':ngocount})

    
class Viewdisaster(View):
    def get(self, request):
        obj=DisasterTable.objects.all()
        print(obj)
        return render(request, "ngo/Viewdisasterdata.html",{'val':obj})

class AddNGODisaster(View):
    def post(self, request):
        print("hhhhh")
        obj=DisasterTable.objects.all()
        print(obj)
        form= disasterForm(request.POST,request.FILES)
        if form.is_valid():
            print("vvvvvvvvvvvv")
            form.save()
            return HttpResponse('''<script>alert(" successfully");window.location="/Viewdisasterdata"</script>''')
        return render(request, "ngo/Viewdisasterdata.html",{'val':obj})    

class Dlt_disaster(View):
    def get(self, request, id):
        obj = DisasterTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/Viewdisasterdata"</script>''')
class editNGODisaster(View):
    def get(self, request,id):
        c= DisasterTable.objects.get(id=id)
        return render(request, "ngo/edit_disaster1.html",{'c':c})
    def post(self, request,id):
        c= DisasterTable.objects.get(id=id)
        form= disasterForm(request.POST,instance=c)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert(" successfully");window.location="/Viewdisasterdata"</script>''')
        return render(request, "ngo/Viewdisasterdata.html")

class addResources(View):
    def post(self, request):
        print('----------->', request.POST)
        loginid = LoginTable.objects.get(id=request.session.get("loginid"))
        cat_obj = Resourcelimit.objects.get(id=request.POST['Name'])
        limit = int(cat_obj.resourcelimit)
        print("-------limit---> ", limit)
        print("name", cat_obj)

        # Calculate the current total resources
        sum1 = 0
        resource_count = ResourceTable.objects.filter(Name_id=cat_obj.id)
        print(resource_count)
        
        # Summing up the relevant field (e.g., quantity)
        for i in resource_count:
            sum1 = int(sum1) + int(i.Quantity)

        print("---sum----->", sum1)    
        total =sum1+int(request.POST['Quantity'])
        print("---------TOTl---------->", total)

        # Check if adding another resource exceeds the limit
        if total < limit:
            form = resourcesForm(request.POST)
            if form.is_valid():
                print("Form is valid")
                c = form.save(commit=False)
                c.LOGIN = loginid
                c.Name = cat_obj
                c.save()
                return HttpResponse('''<script>alert("Successfully added!");window.location="/Viewresource"</script>''')
            
            obj = ResourceTable.objects.filter(LOGIN__id=request.session.get('loginid')).all()
            return HttpResponse('''<script>alert("Error saving resource");window.location="/Viewresource"</script>''')
        else:
            return HttpResponse('''<script>alert("Limit exceeded");window.location="/Viewresource"</script>''')
 
class ViewResources(View):
    def get(self, request):
        obj=ResourceTable.objects.filter(LOGIN__id=request.session.get('loginid')).all()
        obj1 = Resourcelimit.objects.all()
        return render(request, "ngo/ViewResource.html",{'val':obj, 'val1': obj1})
class Dlt_Resources(View):
    def get(self, request, id):
        obj = ResourceTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/Viewresource"</script>''')

class editNGOresource(View):
    def get(self, request,id):
        c= ResourceTable.objects.get(id=id)
        print(c)
        return render(request, "ngo/edit_resource.html",{'c':c, 'date': str(c.Date)})
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

class view_task_ngo(View):
    def get(self, request):
        obj = TaskTable.objects.all()
        return render(request, "ngo/view_task_ngo.html", {'val': obj})

class view_volunteer(View):
    def get(self, request, id):
        request.session['task_id']=id
        obj = UserTable.objects.filter(Type='volunteer')
        return render(request, "ngo/ViewVolunteers.html", {'val': obj})
class assign_task(View):
    def get(self, request, id):
        obj = TaskTable.objects.get(id=request.session['task_id'])
        obj.Status="assigned"
        obj.save()
        obj1 =  AssignTable()
        obj1.TASK = TaskTable.objects.get(id=request.session['task_id'])
        obj1.USER = UserTable.objects.get(id=id)
        obj1.Status = "assigned"
        obj1.save()
        return HttpResponse('''<script>alert("Updated successfully");window.location="/view_task_ngo"</script>''')        
class TaskCompleted(View):
    def get(self, request, id):
        obj = TaskTable.objects.get(id=id)
        print('------------->', obj.id)
        obj.Status="completed"
        obj.save()
        obj1 =  AssignTable.objects.get(TASK_id=obj.id)
        obj1.Status = "completed"
        obj1.save()
        return HttpResponse('''<script>alert("Updated successfully");window.location="/view_task_ngo"</script>''')        
class task_delete(View):
    def get(self, request, id):
        obj = TaskTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("Deleted successfully");window.location="/viewtask"</script>''')

# Create View
class CreateResourcelimitView(View):
    def get(self, request):
        form = ResourcelimitForm()
        return render(request, 'administrator/resourcelimit_form.html', {'form': form})

    def post(self, request):
        form = ResourcelimitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
        return render(request, 'administrator/resourcelimit_form.html', {'form': form})

# List (Read) View
class ListResourcelimitView(View):
    def get(self, request):
        resourcelimits = Resourcelimit.objects.all()
        return render(request, 'administrator/resourcelimit_list.html', {'resourcelimits': resourcelimits})

# Update View
class UpdateResourcelimitView(View):
    def get(self, request, pk):
        resourcelimit = get_object_or_404(Resourcelimit, pk=pk)
        form = ResourcelimitForm(instance=resourcelimit)
        return render(request, 'administrator/resourcelimit_form.html', {'form': form})

    def post(self, request, pk):
        resourcelimit = get_object_or_404(Resourcelimit, pk=pk)
        form = ResourcelimitForm(request.POST, instance=resourcelimit)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
        return render(request, 'administrator/resourcelimit_form.html', {'form': form})

# Delete View
class DeleteResourcelimitView(View):
    def get(self, request, pk):
        resourcelimit = get_object_or_404(Resourcelimit, pk=pk)
        return render(request, 'administrator/resourcelimit_confirm_delete.html', {'resourcelimit': resourcelimit})

    def post(self, request, pk):
        resourcelimit = get_object_or_404(Resourcelimit, pk=pk)
        resourcelimit.delete()
        return redirect('resource_list')  
    
################################api################################

class LoginAPI(APIView):
    def post(self, request):
        response_dict = {}

        # Get data from the request
        username = request.data.get("username")
        password = request.data.get("password")

        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the user from LoginTable
        t_user = LoginTable.objects.filter(Username=username,Password=password).first()

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)

        # # Check password using check_password
        # if not check_password(password, t_user.password):
        #     response_dict["message"] = "failed"
        #     return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)

        # Successful login response
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id
        response_dict["user_type"] = t_user.Type

        return Response(response_dict, status=status.HTTP_200_OK)

class UserAPI(APIView):
    def get(self, request,id):
        response_dict = {}

        # Fetch all UserTable objects
        user_table_objects = UserTable.objects.filter(LOGIN__id=id).first()

        # Serialize the data
        serializer = UserTableSerializer(user_table_objects)

        # Return the serialized data
        return Response(serializer.data)
    

class userregister(APIView):
    def post(self,request):
        user_serializer=UserTableSerializer(data=request.data)
        login_serializer=LoginTableSerializer(data=request.data)
        if user_serializer.is_valid() and login_serializer.is_valid():
            login_serializer.save()
            user_serializer.save(LOGIN=login_serializer.instance)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DonationAPI(APIView):
    def get(self, request):
        response_dict = {}

        # Fetch all UserTable objects
        user_table_objects = DonationTable.objects.all()

        # Serialize the data
        serializer = DonationTableSerializer(user_table_objects, many=True)

        # Return the serialized data
        return Response(serializer.data)
    def post(self, request,lid):
        userlid=UserTable.objects.get(LOGIN=lid)
        user_serializer=DonationTableSerializer1(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save(USER=userlid)
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ComplaintAPI(APIView):
    def get(self, request):
        response_dict = {}

        # Fetch all UserTable objects
        user_table_objects = ComplaintTable.objects.all()

        # Serialize the data
        serializer = ComplaintTableSerializer(user_table_objects, many=True)

        # Return the serialized data
        return Response(serializer.data)
    def post(self, request):
        user_serializer=ComplaintTableSerializer1(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class NGOAPI(APIView):
    def get(self, request):
        response_dict = {}

        # Fetch all UserTable objects
        user_table_objects = NGOTable.objects.all()

        # Serialize the data
        serializer = NGOTableSerializer(user_table_objects, many=True)

        # Return the serialized data
        return Response(serializer.data)
    
class ResourcelimitAPI(APIView):
    def get(self, request):
        response_dict = {}

        # Fetch all UserTable objects
        user_table_objects = Resourcelimit.objects.all()

        # Serialize the data
        serializer = Resourcelimitserializer(user_table_objects, many=True)

        # Return the serialized data
        return Response(serializer.data)
from rest_framework.permissions import AllowAny
class ResourceAPI(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        response_dict = {}
        # Fetch all UserTable objects
        user_table_objects = ResourceTable.objects.all()
        # Serialize the data
        serializer = ResourceTableSerializer(user_table_objects, many=True)
        # Return the serialized data
        return Response(serializer.data)
    def post(self, request):
        user_serializer = ResourceTableSerializer(data=request.data)
        print('----->', request.data)

        try:
            user_obj = LoginTable.objects.get(id=request.data.get('LOGIN'))
            cat = Resourcelimit.objects.get(resourcecategory=request.data.get('Name'))
        except LoginTable.DoesNotExist:
            return Response({"error": "Invalid LOGIN ID"}, status=status.HTTP_400_BAD_REQUEST)
        except Resourcelimit.DoesNotExist:
            return Response({"error": "Invalid Resource Category"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch total quantity already donated for this category
        total_quantity = ResourceTable.objects.filter(Name=cat).exclude(Quantity=None).values_list('Quantity', flat=True)
        total_quantity = sum(int(q) for q in total_quantity if q.isdigit())  # Convert to int safely
        print('total_quantity', total_quantity)
        new_quantity = int(request.data.get('Quantity', 0))
        resource_limit = int(cat.resourcelimit) if cat.resourcelimit else 0
        print('resource_limit', resource_limit)
        print('new_quantity', new_quantity)
        # Check if adding the new quantity exceeds the resource limit
        if total_quantity + new_quantity > resource_limit:
            return Response(
                {"message": "Resource limit reached!"},
                status=status.HTTP_200_OK
            )
        print('resource_limit', resource_limit)
        # If limit not reached, save the resource
        if user_serializer.is_valid():
            user_serializer.save(LOGIN=user_obj, Name=cat)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DisasterAPI(APIView):
    def get(self, request):
    

        # Fetch all UserTable objects
        user_table_objects = DisasterTable.objects.last()

        # Serialize the data
        serializer = DisasterTableSerializer(user_table_objects)

        # Return the serialized data
        return Response(serializer.data)

class DisasterMapAPI(APIView):
    def get(self, request):
    

        # Fetch all UserTable objects
        user_table_objects = DisasterTable.objects.last()

        # Serialize the data
        serializer = DisasterTableSerializer(user_table_objects)

        # Return the serialized data
        return Response(serializer.data)

class SkillAPI(APIView):
    def get(self, request):
        response_dict = {}

        # Fetch all UserTable objects
        user_table_objects = SkillTable.objects.all()

        # Serialize the data
        serializer = SkillTableSerializer(user_table_objects, many=True)

        # Return the serialized data
        return Response(serializer.data)

class AssignAPI(APIView):
    def post(self, request):
        task_id = request.data.get("task_id")
        objects = TaskTable.objects.get(id=task_id)
        objects.Status = "completed"
        objects.save()
        return Response(status=status.HTTP_200_OK)

class TaskAPI(APIView):
    def get(self, request, lid):
        print('------------->')
        response_dict = {}

        # Fetch all UserTable objects
        user_table_objects = AssignTable.objects.filter(USER__LOGIN_id=lid)

        # Serialize the data
        serializer = TaskTableSerializer(user_table_objects, many=True)
        print(serializer.data)
        # Return the serialized data
        return Response(serializer.data)
    
class TaskupdateAPI(APIView):
    def put(self, request):
        id = request.data.get("task_id")
        print('id',id)
        print('--------------', request.data)
        # Fetch all UserTable objects
        user_table_objects = TaskTable.objects.filter(id=id).first()

        # Serialize the data
        serializer = TaskTableSerializer1(user_table_objects, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class profileupdateAPI(APIView):
    def get(self, request):
        response_dict = {}

        # Fetch all UserTable objects
        user_table_objects = UserTable.objects.all()

        # Serialize the data
        serializer = profileupdateAPISerializer(user_table_objects, many=True)

        # Return the serialized data
        return Response(serializer.data)
    def put(self, request,id):
        user = UserTable.objects.get(LOGIN__id=id)
        serializer = profileupdateAPISerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework import serializers
from .models import DonationTable

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationTable
        fields = ['Amount']  # Include only relevant fields

from django.db.models import Sum
class Viewvolunteerscount(APIView):
    def get(self,request):
        v=LoginTable.objects.filter(Type='volunteer').count()
        print(v)
        total_amount = DonationTable.objects.aggregate(total=Sum('Amount'))['total']
        total_amount = total_amount or 0  # Handle None if there are no donations
        print(total_amount)
        return Response({"total_donation": total_amount,"volunteercount":v}, status=status.HTTP_200_OK)
       


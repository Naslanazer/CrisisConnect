from rest_framework import serializers


from .models import *

class LoginTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginTable
        fields = ['Username', 'Password', 'Type']

class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields =['Name', 'age','Gender','Phone','Email','Address','Type','Skill','Status']

class profileupdateAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields =['Name', 'age','Gender','Phone','Email','Address','Type','Skill']

class DonationTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationTable
        fields = ['Amount', 'Description', 'Date']
class DonationTableSerializer1(serializers.ModelSerializer):
    class Meta:
        model = DonationTable
        fields = ['USER','Amount']

class ComplaintTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['Complaint', 'Reply', 'Date']
class ComplaintTableSerializer1(serializers.ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['USER','Complaint']

class NGOTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGOTable
        fields = ['Name', 'Email', 'Phone', 'Service', 'Specialization']

class ResourceTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceTable
        fields = ['Quantity', 'Details', 'Date']

class Resourcelimitserializer(serializers.ModelSerializer):
    class Meta:
        model = Resourcelimit
        fields = ['id','resourcecategory','resourcelimit','resourcepercentage']

class DisasterTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterTable
        fields = ['Image', 'Disaster', 'Details', 'Location', 'Weather','created_at']

class SkillTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTable
        fields = ['skill']

class TaskTableSerializer(serializers.ModelSerializer):
    Task_no=serializers.CharField(source='TASK.Task')
    DATE=serializers.CharField(source='TASK.Date')
    Task=serializers.CharField(source='TASK.Task')
    class Meta:
        model = TaskTable
        fields = ['id','Task_no', 'Task', 'Date', 'Status']

class TaskTableSerializer(serializers.ModelSerializer):
    Task_no = serializers.CharField(source='TASK.Task_no')
    Task = serializers.CharField(source='TASK.Task')
    Date = serializers.DateTimeField(source='TASK.Date')

    class Meta:
        model = AssignTable
        fields = ['id', 'Task_no', 'Task', 'Date', 'Status', 'AssignDate']

class TaskTableSerializer1(serializers.ModelSerializer):
    class Meta:
        model = TaskTable
        fields = ['Status']
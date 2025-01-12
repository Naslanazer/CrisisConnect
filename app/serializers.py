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

class DonationTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationTable
        fields = ['Amount', 'Description', 'Date']

class ComplaintTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['Complaint', 'Reply', 'Date']

class NGOTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGOTable
        fields = ['Name', 'Email', 'Phone', 'Service', 'Specialization']

class ResourceTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceTable
        fields = ['Name', 'Quantity', 'Details', 'Date']

class DisasterTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisasterTable
        fields = ['Image', 'Disaster', 'Details', 'Location', 'Weather']

class SkillTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTable
        fields = ['skill']
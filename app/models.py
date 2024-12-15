from django.db import models

class LoginTable(models.Model):
    Username= models.CharField(max_length=30, null=True, blank=True)
    Password= models.CharField(max_length=30, null=True, blank=True)
    Type= models.CharField(max_length=30, null=True, blank=True)
    
class UserTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name= models.CharField(max_length=30, null=True, blank=True)
    age= models.IntegerField(null=True, blank=True)
    Gender= models.CharField(max_length=20, null=True, blank=True)
    Phone= models.BigIntegerField(null=True, blank=True)
    Email= models.CharField(max_length=20, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    Type = models.CharField(max_length=30, null=True, blank=True)
    Skill = models.CharField(max_length=30, null=True, blank=True)
 
class DonationTable(models.Model):
    USER= models.ForeignKey(UserTable, on_delete=models.CASCADE)
    Amount= models.FloatField(null=True, blank=True)
    Description=models.CharField(max_length=20, null=True, blank=True)
    Date= models.DateField(null=True, blank=True)

class ComplaintTable(models.Model):
    USER= models.ForeignKey(UserTable, on_delete=models.CASCADE)
    Complaint= models.CharField(max_length=100, null=True, blank=True)
    Reply= models.CharField(max_length=20, null=True, blank=True)
    Date= models.DateField(null=True, blank=True)

class NGOTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name= models.CharField(max_length=30, null=True, blank=True)
    Email= models.CharField(max_length=20, null=True, blank=True)
    Phone= models.BigIntegerField(null=True, blank=True)
    Service= models.CharField(max_length=20, null=True, blank=True)
    Specialization= models.CharField(max_length=20, null=True, blank=True)
    
class ResourceTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name= models.CharField(max_length=30, null=True, blank=True)
    Quantity= models.IntegerField(null=True, blank=True)
    Details= models.CharField(max_length=20, null=True, blank=True)
    Date= models.DateField(null=True, blank=True)

class DisasterTable(models.Model):
    Disaster= models.CharField(max_length=30, null=True, blank=True)
    Details= models.CharField(max_length=125, null=True, blank=True)
    Location= models.CharField(max_length=20, null=True, blank=True)
    Weather= models.CharField(max_length=20, null=True, blank=True)

class SkillTable(models.Model):
    skill = models.CharField(max_length=30, null=True, blank=True)
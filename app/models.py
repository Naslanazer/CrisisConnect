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
    Status = models.CharField(max_length=30, null=True, blank=True)
 
class DonationTable(models.Model):
    USER= models.ForeignKey(UserTable, on_delete=models.CASCADE,null=True,blank=True)
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
class Resourcelimit(models.Model):
    resourcecategory =  models.CharField(max_length=100, null=True, blank=True)
    resourcelimit =  models.CharField(max_length=100, null=True, blank=True)
    resourcepercentage = models.IntegerField(null=True, blank=True)

    
class ResourceTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True,blank=True)
    Name= models.ForeignKey(Resourcelimit,on_delete=models.CASCADE, null=True, blank=True)
    Quantity= models.CharField(max_length=100,null=True, blank=True)
    Details= models.CharField(max_length=100, null=True, blank=True)
    Date= models.DateField(auto_now_add=True, null=True, blank=True)
    def calculate_percentage(self):
        """
        Calculate the percentage of the resource used.
        """
        if self.Name and self.Quantity:
            try:
                resource_limit = int(self.Name.resourcelimit)
                quantity = int(self.Quantity)
                if resource_limit > 0:
                    return (quantity / resource_limit) * 100
            except (ValueError, TypeError):
                # Handle invalid or missing values gracefully
                return None
        return None

    def save(self, *args, **kwargs):
        """
        Override the save method to update the resource percentage
        in the associated Resourcelimit model.
        """
        percentage = self.calculate_percentage()
        if self.Name and percentage is not None:
            self.Name.resourcepercentage = int(percentage)  # Save as an integer
            self.Name.save()  # Update the Resourcelimit instance
        super(ResourceTable, self).save(*args, **kwargs)  # Save the ResourceTable instance

class DisasterTable(models.Model):
    Image= models.FileField()
    Disaster= models.CharField(max_length=30, null=True, blank=True)
    Details= models.CharField(max_length=125, null=True, blank=True)
    Location= models.CharField(max_length=20, null=True, blank=True)
    Weather= models.CharField(max_length=20, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)

class SkillTable(models.Model):
    skill = models.CharField(max_length=30, null=True, blank=True)

class TaskTable(models.Model):
    Task_no= models.CharField(max_length=100, null=True, blank=True)
    Task= models.CharField(max_length=100, null=True, blank=True)
    Date= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    Status= models.CharField(max_length=30, null=True, blank=True)

class AssignTable(models.Model):
    TASK= models.ForeignKey(TaskTable, on_delete=models.CASCADE)
    USER= models.ForeignKey(UserTable, on_delete=models.CASCADE)
    AssignDate= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    Status= models.CharField(max_length=30, null=True, blank=True)
from django.db import models

# Create your models here.
class AppUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    access_label = models.IntegerField(blank=True, null=True)

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    lastname = models.CharField(max_length=45, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(AppUser, models.DO_NOTHING, blank=True, null=True)

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=45, blank=True, null=True)

    

class Designation(models.Model):
    desg_id = models.AutoField(primary_key=True)
    desg_name = models.CharField(max_length=45, blank=True, null=True)
    desg_description = models.CharField(max_length=45, blank=True, null=True)


class EmployeeDetails(models.Model):
    emp_details_id = models.AutoField(primary_key=True)
    date_of_join = models.DateField(blank=True, null=True)
    status_of_emp = models.CharField(max_length=45, blank=True, null=True)
    desg = models.ForeignKey(Designation, models.DO_NOTHING, blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    project = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(AppUser, models.DO_NOTHING, blank=True, null=True)

class LeaveType(models.Model):
    leave_type_id = models.AutoField(primary_key=True)
    leave_type = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.leave_type


class LeaveApplication(models.Model):
    application_id = models.AutoField(primary_key=True)
    date_of_application = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    leave_approval_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(AppUser, models.DO_NOTHING, blank=True, null=True)
    leave_status = models.CharField(max_length=45, blank=True, null=True)
    leave_type = models.ForeignKey(LeaveType, models.DO_NOTHING, blank=True, null=True)
    leave_description = models.CharField(max_length=100, blank=True, null=True)
  

class Leaves(models.Model):
    leave_id = models.AutoField(primary_key=True)
    leaves_consume = models.IntegerField(blank=True, null=True)
    leaves_remain = models.IntegerField(blank=True, null=True)
    total_leaves = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(AppUser, models.DO_NOTHING, blank=True, null=True)

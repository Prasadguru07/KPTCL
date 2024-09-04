from django.db import models

# models for contractor
class contractor(models.Model):
    id = models.IntegerField(primary_key=True,max_length=100)
    password = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

# models for admin login
class admin(models.Model):
    id = models.IntegerField(primary_key=True,max_length=200)
    password = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True) 

# models for verifier login
class verifier(models.Model):
    id = models.IntegerField(primary_key=True,max_length=200)
    password = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

# models for CI dept
class CI(models.Model):
    project_id = models.CharField(max_length=200)
    draw_id = models.CharField(primary_key=True,max_length=200)
    file = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

#models for EEE dept
class EEE(models.Model):
    project_id = models.CharField(max_length=200)
    draw_id = models.CharField(primary_key=True,max_length=200)
    file = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

#models for ME dept
class ME(models.Model):
    project_id = models.CharField(max_length=200)
    draw_id = models.CharField(primary_key=True,max_length=200)
    file = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

#models for CIV dept
class CIV(models.Model):
    project_id = models.CharField(max_length=200)
    draw_id = models.CharField(primary_key=True,max_length=200)
    file = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

#models of overall project_details
class project_details(models.Model):
    project_id = models.CharField(primary_key=True,max_length=200)
    project_Title  = models.TextField(max_length=200)
    dept = models.CharField(max_length=200)
    desc = models.TextField(max_length=300)
    file = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
from django.db import models
from django.db.models import CharField, DateTimeField, BooleanField

################################################################
#No.1
LEVELS = (
    'Root',
    'Admin', #register
    'Gate', #admin create
    'Supporter' #root create
)

USER_STATUS = (
    'Registered',
    'Verified', #verify by phone number
    'Approved', #root approve
    'Suspend',
    'Invited'
)

class User(models.Model):    
    email               =  CharField(max_length=200)
    fullname            =  CharField(max_length=200)
    position            =  CharField(max_length=200)
    password            =  CharField(max_length=200)
    phone               =  CharField(max_length=200)
    level               =  CharField(max_length=200) #, choices=LEVELS
    status              =  CharField(max_length=200) #, choices=USER_STATUS
    timeUpdate          =  DateTimeField()  
    suspendReason       =  CharField(max_length=200)
    isDeleted           =  BooleanField(default = False)
    

################################################################
#No.2
class Level(models.Model):
    levelID             =  CharField(max_length=200)
    levelName           =  CharField(max_length=200)

################################################################
#No.3
class Option(models.Model):
    optionName          =  CharField(max_length=200)
    value               =  CharField(max_length=200)
  
################################################################
GENDERS = (
    'Male',
    'Female',
    'undefined',
)
STATE = (
    'Checked_in',
    'Checked_out',
    'Visitor'
)
PERSON_TYPE = (
    'Staff',
    'Guest',
)

################################################################
#No.6
class LoginSession(models.Model):
    token               =  models.CharField(max_length=200)
    email               =  models.CharField(max_length=200)
    level               =  models.CharField(max_length=200)
    fullname            =  models.CharField(max_length=200)
    loginTime           =  models.DateTimeField()
    logoutTime          =  models.DateTimeField()
    platform            =  models.CharField(max_length=200)
    validTo             =  models.DateTimeField()
    isDeleted           =  models.BooleanField(default=False)


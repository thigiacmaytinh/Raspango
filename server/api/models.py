from django.db import models

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
    email               =  models.CharField(max_length=200)
    fullname            =  models.CharField(max_length=200)
    position            =  models.CharField(max_length=200)
    password            =  models.CharField(max_length=200)
    phone               =  models.CharField(max_length=200)
    level               =  models.CharField(max_length=200) #, choices=LEVELS
    status              =  models.CharField(max_length=200) #, choices=USER_STATUS
    timeUpdate          =  models.DateTimeField()  
    suspendReason       =  models.CharField(max_length=200)
    isDeleted           =  models.BooleanField(default = False)
    

################################################################
#No.2
class Level(models.Model):
    levelID             =  models.CharField(max_length=200)
    levelName           =  models.CharField(max_length=200)

################################################################
#No.3
class Option(models.Model):
    optionName          =  models.CharField(max_length=200)
    value               =  models.CharField(max_length=200)
  
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


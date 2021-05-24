import os
import random
import string



def urlify(s):
    s = re.sub(r"[^\w\s]", '', s)
    s = re.sub(r"\s+", '-', s)
    return s

####################################################################################################

def GenerateRandomName(name):
    fileName, fileEx = os.path.splitext(name)
    fileName = urlify(fileName)
    return fileName + '.' + GenerateRandomString() + fileEx

####################################################################################################

def GenerateRandomString():
    return ''.join(random.choices(string.ascii_lowercase + "_" + string.ascii_uppercase +  string.digits, k=10))
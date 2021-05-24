import os
import shutil

def MkDir(dirPath):
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)

def GetDirName(fullpath):    
    return GetFileName(fullpath)

def GetParentDir(fullpath):    
    return os.path.abspath(os.path.join(fullpath, os.pardir))

def GetPathWithoutExt(filePath):
    filePathWithouExt, ext = os.path.splitext(filePath)
    return filePathWithouExt

def GetFileName(filePath):
    fileName = os.path.basename(filePath)
    return fileName

def GetFileNameWithoutExt(filePath):
    fileName = GetFileName(filePath)
    fileNameWithoutExt, ext = os.path.splitext(fileName)
    return fileNameWithoutExt

def RemoveDir(dirPath):
    if(os.path.exists(dirPath)):
        shutil.rmtree(dirPath)

def RemoveFile(filePath):
    if(os.path.exists(filePath)):
        os.remove(filePath)

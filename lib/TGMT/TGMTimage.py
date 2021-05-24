from PIL import Image, ExifTags
from api.util import *
from django.conf import settings as djangoSettings
from django.core.files.storage import FileSystemStorage
import base64

####################################################################################################

def ResizeImage(imgPath, desireWidth):
    img = Image.open(imgPath)
    width, height = img.size
    if(width > desireWidth):
        wpercent = (desireWidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((desireWidth,hsize), Image.ANTIALIAS)
        img.save(imgPath)
    img.close()

    if(width < djangoSettings.FACE_MIN_SIZE):
        return False
    return True

####################################################################################################

def RotateImageWithExif(imgPath):
    try:
        image=Image.open(imgPath)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif=dict(image._getexif().items())

        if exif[orientation] == 3:
            image=image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image=image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image=image.rotate(90, expand=True)
        image.save(imgPath)
        image.close()

    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass
    return True

####################################################################################################
#return true if has new image
def SaveImageFromRequest(request, saveDir, fileName):
    _isBase64 = request.POST.get("isBase64")
    
    if(_isBase64 != None and _isBase64 == "True"):
        _imageBase64 = request.POST.get("imageBase64")
        if(_imageBase64 != None and _imageBase64 != ""):                
            SaveBase64ToImg(saveDir, fileName, _imageBase64)
            return True
    elif request.method == 'POST' and request.FILES['selectedFile']:            
        uploadfile = request.FILES['selectedFile']
        upload_folder_abs = os.path.join(djangoSettings.MEDIA_ROOT, saveDir)
        fs = FileSystemStorage(upload_folder_abs, djangoSettings.MEDIA_URL)
        filename = fs.save( fileName , uploadfile)
        # uploaded_file_url = fs.url(filename)
        return True
    return False
    

####################################################################################################

def SaveBase64ToImg(folder_name, file_name, imageData):    
    if(imageData == None or imageData == "" ):
        return ""
    try:
        upload_folder_abs = os.path.join(djangoSettings.MEDIA_ROOT, folder_name)
        if not os.path.exists(upload_folder_abs):
            os.makedirs(upload_folder_abs)

        has_multiple_images = True if imageData.count("|") > 1 else False
        imageData = imageData.replace(" ", "+")
        imageData = imageData.replace("data:image/jpeg;base64,", "")
        imageData = imageData.replace("data:image/png;base64,", "")
        if has_multiple_images:
            imageData = imageData.split("|")

        if has_multiple_images:
            for img in imageData:
                if(len(img) == 0):
                    continue

                save_file = os.path.join(upload_folder_abs, file_name)
                uploadfile = base64.b64decode(img)
                with open(save_file, 'wb') as f:
                    f.write(uploadfile)              
        else:
            save_file = os.path.join(upload_folder_abs, file_name)
            uploadfile = base64.b64decode(imageData)
            with open(save_file, 'wb') as f:
                f.write(uploadfile)

        return True
    except Exception as e:
        print(str(e))
        return False

####################################################################################################

def Compress(imgPath):
    img = Image.open(imgPath)
    img = img.convert('RGB')
    img.save(imgPath, quality=90)
    img.close()
    return True

####################################################################################################

def PreprocessImage(imgPath):
    isValid = RotateImageWithExif(imgPath)
    if(isValid):
        isValid &= ResizeImage(imgPath, 1000)
    if(isValid):
        isValid &= Compress(imgPath)
    return isValid

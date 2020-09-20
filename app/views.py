from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
from app.forms import * 
def Image_form(request):
    form=Image()
    if request.method=='POST' and request.FILES:#checked wheathr the POST method,FILES are activated or not
        form_data=Image(request.POST,request.FILES)#collected the submitted data
        if form_data.is_valid():                    #validating submitted data
            img=form_data.cleaned_data['image']     #collecting the uploaded image
            fs=FileSystemStorage()                  #creating a object for FileSystemStorage class 
            file=fs.save(img.name,img)                   # saving the image into our media folder
            img_url=fs.url(file)
            return render(request,'displayimage.html',context={'img_url':img_url})
    return render(request,'image_form.html',context={'form':form})
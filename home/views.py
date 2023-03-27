from django.shortcuts import render
from . models import *
from django.contrib import messages
from django.db.models import Q


def index(request):
    data=Blog.objects.all()
    return render (request,"index.html",{"data":data})

def signup(request):
    if request.method =='POST':
        email=request.POST['email']
        pwd =request.POST['pwd']
        cpwd =request.POST['cpwd']
        if pwd != cpwd:
            messages.error(request,"Password not matched") 
            return render (request,'user.html')
            
        elif User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists") 
            return render (request,'user.html')
        else:
            User.objects.create(email=email, pwd=pwd)
            return render(request,'login.html')
            
    else:
        
        return render (request,'user.html')
    
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        pwd =request.POST['pwd']
        if User.objects.filter(email=email).exists():
            if User.objects.filter(pwd=pwd).exists():
                data=Blog.objects.all()
                return render(request,'dash.html' ,{'blog':data})
            else:
                messages.error(request,'password is wrogn')
                return render (request,'login.html')
                
        else:
            messages.error(request,'email not exists')
            return render (request,'login.html')
            
    
    else:    
        return render (request,'login.html')
    

def delete(request,id):
    i=Blog.objects.filter(pk=id)
    i.delete()
    data=Blog.objects.all()
    return render(request,'dash.html' ,{'blog':data})


def Addblog(request):
    if request.method=='POST':
        Title=request.POST['title']
        Text=request.POST['text']
        images = request.FILES.get('files')
        Blog.objects.create( Text=Text,Title=Title,Images = images)
        data=Blog.objects.all()
        return render(request,'dash.html',{'blog':data})
    else:
        return render(request,'dash.html')
    
    
def search(request):
    find=request.POST['name']
    data=Blog.objects.filter(Q(Title=find) | Q(Text=find))
    return render (request,"index.html",{"data":data})
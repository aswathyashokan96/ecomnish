from django.shortcuts import render
from myapp.models import *
# from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def fruits(request):
    return render(request,'ecommerceapp/fruits.html')

def apple(request):
    return render(request,'ecommerceapp/apple.html')

def grapes(request):
    return render(request,'ecommerceapp/grapes.html')

def orange(request):
    return render(request,'ecommerceapp/orange.html')

def strawberry(request):
    return render(request,'ecommerceapp/strawberry.html')

def vegitable(request):
    return render(request,'ecommerceapp/vegitable.html')

def tomatto(request):
    return render(request,'ecommerceapp/tomatto.html')

def carrot(request):
    return render(request,'ecommerceapp/carrot.html')

def potatto(request):
    return render(request,'ecommerceapp/potatto.html')

def bitter_gourd(request):
    return render(request,'ecommerceapp/bitter_gourd.html')

def electronics(request):
    return render(request,'ecommerceapp/electronics.html')

def tv(request):
    return render(request,'ecommerceapp/tv.html')

def mobile(request):
    return render(request,'ecommerceapp/mobile.html')

def fridge(request):
    return render(request,'ecommerceapp/fridge.html')

def washingmechine(request):
    return render(request,'ecommerceapp/washingmechine.html')

def grocery(request):
    return render(request,'ecommerceapp/grocery.html')

def atta(request):
    return render(request,'ecommerceapp/atta.html')

def maida(request):
    return render(request,'ecommerceapp/maida.html')

def rice(request):
    return render(request,'ecommerceapp/rice.html')

def oil(request):
    return render(request,'ecommerceapp/oil.html')

def home(request):
    return render(request,'ecommerceapp/home.html')

def base(request):
    return render(request,'ecommerceapp/base.html')

# def registration(request):
#     if request.method=='POST':
#         member=Member(firstname=request.POST['firstname'],contact=request.POST['contact'],email=request.POST['email'],password=request.POST['password'])
#         member.save()
#         msg="Registration successfully done!!!"
#         return redirect('/')
#     else:
#         msg="Passwords didnt match"
#         return render(request,'ecommerceapp/registration.html')

def registration(request):
            msg=""
            if request.method=='POST':
                firstname=request.POST.get('firstname')
                lastname=request.POST.get('lastname')
                username=request.POST.get('username')
                contact=request.POST.get('contact')
                email=request.POST.get('email')
                password=request.POST.get('password')
                rpassword=request.POST.get('rpassword')
                if password==rpassword:
                    data=tbl_registrations.objects.create(firstname=firstname,lastname=lastname,username=username,contact=contact,email=email,password=password,status=1)
                    data=tbl_login.objects.create(username=username,password=password,status=1)
                    msg="Registration successfully done!!!"
                    return render(request,'ecommerceapp/home.html')
                else:
                    msg="Passwords didnt match"
            return render(request,"ecommerceapp/registration.html",{'msg':msg})

def login(request):
    msg=""
    if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            if tbl_login.objects.filter(username=username,password=password):
                data=tbl_registrations.objects.get(username=username,password=password)
                request.session['userid']=data.id
                if data.status=='admin':
                    # return HttpResponseRedirect(reverse('registration.html'))
                    return render(request,"ecommerceapp/registration.html",{'msg':msg})
                elif data.status=='1':
                    # return HttpResponseRedirect(reverse('login.html'))
                    return render(request,"ecommerceapp/home.html",{'msg':msg})
                    # return HttpResponse("login successfully")
                    

                 
            else:
                msg="incorrect password or username"
                # return HttpResponse("incorrect username or password")
    return render(request,"ecommerceapp/login.html",{'msg':msg})
    










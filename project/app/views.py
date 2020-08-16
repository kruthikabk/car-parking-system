from django.shortcuts import render , HttpResponse , redirect
from .models import Feedback,BlogPost
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,'index.html')

    return render(request,'index.html')

def book(request):
    return render(request,'book.html')

def index2(request):
    return render(request,'index2.html')


def feedback(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        
        from_email=settings.EMAIL_HOST_USER
            
        connection = mail.get_connection()
        connection.open()
        email1=mail.EmailMessage(name,f'email: {email} \n phone number: {phone} Query : {desc}',from_email,['kruthikabk01@gmail.com'],connection=connection)
        connection.send_messages([email1])
        connection.close()
       
        


        myusercontact=Contact(name=name , email=email , desc=desc)
        myusercontact.save()
        messages.warning(request,"Your feedback is submitted")
        return redirect("/index2")

    return render(request,'feedback.html')


def handlesignup(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 != pass2:
            messages.warning(request,"your password is not matching")
            return redirect('/signup')
        try:
            if User.objects.get(username=username):
                messages.warning(request,"username already exists")
                return redirect('/signup')
        except Exception as identifier:
            pass 

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.info(request,"Signup successfull")
        return redirect('/index2')
    return render(request,'signup.html')


def handlelogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request,"login successful")
            return redirect('/index2')
        else:
            messages.error(request,"invalid credentials")
            return redirect('/login')    

    return render(request,'login.html')


def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Succesfull")
    return redirect('/')    



def reviews(request):
    if not request.user.is_authenticated:
        messages.error(request,"please login and try again")
        return redirect('/login')

    allPosts=BlogPost.objects.all()
    context = {'allPosts':allPosts}
    return render(request,'reviews.html', context)  


def search(request):
    query=request.GET["search"]
    if len(query)>80:
        allPosts=BlogPost.objects.none()
    else:
        allPostsTitle=BlogPost.objects.filter(title__icontains=query)
        allPostsContent=BlogPost.objects.filter(content__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)

    if allPosts.count()==0:
        messages.warning(request,"No results found")
    params={'allPosts':allPosts,'query':query}

    return render(request,'search.html',params)  


def rules(request):
    return render(request , 'rules.html')



def reservation(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['num']
        place=request.POST['place']
        date=request.POST['date']
        time=request.POST['time']
        slot=request.POST['slot']
        try:
            if  User.objects.get(slot=slot):
                messages.warning(request,"This slot is alredy booked!")
                return redirect('/reservation')
        except Exception as identifier:
            pass 

       
        userbooking= User.objects.create_user(fname,date,time)
        userbooking.first_name=fname
        userbooking.last_name=lname
        userbooking.save()
        messages.info(request,"Booking successfull")
        return redirect('/index2')
    
    return render(request , 'reservation.html')


def about(request):
    return render(request , 'about.html')


from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
import datetime
# Create your views here.
def Home(request):
    return render(request,'index.html')
def Adminlogin(request):
    error=False
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(username=u,password=p)
        if user.is_staff:
            login(request,user)
            return redirect('AddBook')
        else:
            error=True
    d={'error':error}
    return render(request,'admin.html',d)
def Signupadmin(request):
    error=False
    if request.method == "POST":
        f=request.POST['firstname']
        l=request.POST['lastname']
        e=request.POST['emailid']
        u=request.POST['username']
        p=request.POST['password']
        user = User.objects.filter(username = u)
        if user:
            error= True
        else:
            us = User.objects.create_user(username = u,password=p, email=e, first_name=f,last_name=l )

            return redirect('loginadmin')


    d = {"error":error}
    return render(request, 'signupadmin.html',d)

def Student_login(request):
    error=False
    if request.method=="POST":
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        if user:
            login(request,user)
            return redirect('studentbooksearch')
        else:
            error=True
    d={'error':error}
    return render(request,'studentlogin.html')


def Signup_student(request):
    error=False
    if request.method == "POST":
        f=request.POST['firstname']
        l=request.POST['lastname']
        e=request.POST['emailid']
        u=request.POST['username']
        p=request.POST['password']
        s=request.POST['studentid']
        user = User.objects.filter(username = u)
        if user:
            error= True
        else:
            us = User.objects.create_user(username = u,password=p, email=e, first_name=f,last_name=l )
            Studentinfo.objects.create(user=us,studentid=s)
            return redirect('loginstudent')


    d = {"error":error}
    return render(request,'signupstudent.html',d)
def Add_book(request):
    if not request.user.is_authenticated:
        return redirect('loginadmin')

    messages1=[]
    if request.method == "POST":
        bookid=request.POST['Bookid']
        Title=request.POST['title']
        Authorname=request.POST['Authorname']
        cost=request.POST['cost']
        q=request.POST['quantity']
        error = True
        Book.objects.create(bookid=bookid,title=Title,Authorname=Authorname,cost=cost,quantity=q)
        messages1 = messages.info(request, 'Add Book Successfully')
        return redirect('bookview')

    d ={'messages':messages1}
    return render(request,'AddBook.html',d)
def search_book(request):
    if not request.user.is_authenticated:
        return redirect('loginadmin')
    error=False
    data1=Book.objects.all()
    if request.method=="POST":
        s = request.POST['bookid']

        data = Book.objects.filter(bookid=s)
        if data:
            data1 = data
            error=True


    d = {'data':data1,'error':error}

    return render(request,'booksearch.html',d)

def View_Book(request):
    if not request.user.is_authenticated:
        return redirect('loginadmin')
    data=Book.objects.all()
    d={'data':data}
    return render(request,'bookview.html',d)

def edit_book(request,pid):
    if not request.user.is_authenticated:
        return redirect('loginadmin')
    messages1=[]
    data1=Book.objects.get(id=pid)
    if request.method == "POST":
        bookid=request.POST['Bookid']
        Title=request.POST['title']
        Authorname=request.POST['Authorname']
        cost=request.POST['cost']
        q=request.POST['quantity']
        data1.bookid=bookid
        data1.title=Title
        data1.cost=cost
        data1.quantity=q
        data1.Authorname=Authorname
        data1.save()
        messages1 = messages.info(request,'Selected Book is Updated Successfully')
        return redirect('searchbook')

    d = {'messages':messages1,'data':data1}
    return render(request,'editbook.html',d)
def booksearch2(request):
    if not request.user.is_authenticated:
        return redirect('loginstudent')
    error=False
    data1=Book.objects.all()
    data=Book.objects.all()
    if request.method=="POST":
        bookname=request.POST['bookname']
        authorname=request.POST['authorname']
        data2=Book.objects.filter(title=bookname,Authorname=authorname)
        if data2:
            data1=data2
            error=True

    d={'data':data1,'error':error}
    return render(request,'studentbooksearch.html',d)
def order(request):
    if not request.user.is_authenticated:
        return redirect('loginstudent')
    error=False
    data1=Book.objects.all()
    if request.method=="POST":
        bookname=request.POST['bookname']
        authorname=request.POST['authorname']
        data2=Book.objects.filter(title=bookname,Authorname=authorname)
        if data2:
            data1=data2
            error=True

    d={'data':data1,'error':error}
    return render(request,'placeorder.html',d)

def order_book(request,pid):
    if not request.user.is_authenticated:
        return redirect('loginstudent')
    data=Book.objects.get(id=pid)
    user1=Studentinfo.objects.filter(user=request.user.id).first()
    tday=datetime.date.today()
    tdelta=datetime.timedelta(days=30)
    ex=tday+tdelta
    Placeorder.objects.create(book=data,user=user1,issuedate=tday, expirydate=ex)
    data.quantity-=1
    data.save()
    return redirect('vieworder')

def ViewOrder(request):
    if not request.user.is_authenticated:
        return redirect('loginstudent')
    data=Studentinfo.objects.filter(user=request.user.id).first()
    order1 = Placeorder.objects.filter(user=data)
    d = {'data1':order1}
    return render(request,'order.html',d)

def returnbook(request,pid):
    if not request.user.is_authenticated:
        return redirect('loginstudent')
    data=Book.objects.get(id=pid)
    data1=Placeorder.objects.filter(book=data).first()
    data1.delete()
    data.quantity+=1
    data.save()
    return redirect('vieworder')
def Fine(request):
    if not request.user.is_authenticated:
        return redirect('loginstudent')
    error=False
    data=Studentinfo.objects.filter(user=request.user.id).first()
    order1 = Placeorder.objects.filter(user=data)
    d = {'data1':order1}
    return render(request,'fineview.html',d)

def f(request,pid):
    if not request.user.is_authenticated:
        return redirect('loginstudent')

    error=False
    data = Placeorder.objects.get(id=pid)
    tday = datetime.date.today()
    mon1 =  data.expirydate.month
    d1 =  data.expirydate.day
    f1=0
    d2=0
    if  mon1 == tday.month:
        if d1 < tday.day:
            d2=tday.day-d1
            f1=d2*5
            error=True
        else:
            pass
    elif  mon1 < tday.month:
        m2=tday.month-mon1
        d3=(30*m2)+tday.day
        d2=d3-d1
        f1=d2*5
        error=True

    else:
        f1=0
        d2=0
        error=True
    d={'fine':f1,'late':d2,'error':error}
    return render(request, 'fineview.html',d)

def orderview(request):
    if not request.user.is_authenticated:
        return redirect('loginadmin')
    view=Placeorder.objects.all()
    d={'view':view}
    return render(request,'orderview.html',d)
def Logout(request):
    logout(request)
    return redirect('home')



def bookdelete(request,pid):
    if not request.user.is_authenticated:
        return redirect('loginadmin')
    error1=False
    data = Book.objects.get(id=pid)
    data.delete()
    error1=True
    d = {'error1':error1}
    return render(request,'booksearch.html',d)
    return redirect('searchbook')

def about(request):
    return render(request,'about.html')

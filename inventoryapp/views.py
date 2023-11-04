from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    product = Product.objects.all()
    context={
        'product':product,
    }
    return render(request,'home.html',context)


@login_required(login_url='/signin')
def add(request):
    if request.method == 'POST':
        productname = request.POST['productname']
        purchaseitems = request.POST['purchaseitems']
        solditems = request.POST['solditems']
        itempiece = request.POST['itempiece']
        sales = request.POST['sales']
        purchasedate = request.POST['purchasedate']
        newproduct=Product(productname=productname,purchaseitems=purchaseitems,solditems=solditems,itempiece=itempiece, sales=sales,purchasedate=purchasedate)
        newproduct.save()
        return redirect("/")
    return render(request,'add.html')


@login_required(login_url='/signin')
def update(request,id):
    product = Product.objects.get(id=id)
    if request.method =='POST':
        new_productname=request.POST['productname']
        new_purchaseitems=request.POST['purchaseitems']
        new_solditems=request.POST['solditems']
        new_itempiece=request.POST['itempiece']
        new_sales=request.POST['sales']
        new_purchasedate=request.POST['purchasedate']

        product.productname = new_productname
        product.purchaseitems = new_purchaseitems
        product.solditems = new_solditems
        product.itempiece = new_itempiece
        product.sales = new_sales
        product.purchasedate = new_purchasedate
        product.save()
        return redirect("/")
    return render(request,'update.html',context={'product':product})

@login_required(login_url='/signin')
def delete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/')
    
@login_required(login_url='/signin')
def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        product = Product.objects.filter(productname__contains=query)

        context={
            'product':product
        }
        return render(request,'search.html',context)
    return render(request,'search.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confrimpassword =request.POST['confrimpassword']
        if password == confrimpassword:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already in use')
                return redirect('/register')
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already used')
                return redirect('/register')
            else:
                User.objects.create_user(username=username,email=email,password=password)
                messages.success(request,'Account created successfully.Goto login page')
                return redirect('/signin')
        else:
            messages.error(request,'password do not match pls check password')
            return redirect('/register')
    return render(request,'register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfully')
            return redirect('/')
        else:
            messages.error(request,'Invalid details')
            return redirect('/signin')

    return render(request,'signin.html')
    

def logout(request):
    if request.method =='POST':
        logout(request)
        messages.success(request,'logout successfully')
        return redirect('/')
    return render(request,'logout.html')
    

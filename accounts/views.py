from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm,CreateUserForm,CustomerForm,CustomerOrderForm,UpdateOrderForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unautherized_user,allowed_users,admin_only
# Create your views here.


@unautherized_user
def signup(request):
    form= CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
    if form.is_valid():
        user=form.save()  
        messages.success(request, "Account created")
        return redirect('login')  
    context={"form":form}
    return render(request,"signup.html", context)

@unautherized_user
def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request, username=username,password=password)
        if user is not None:
            login(request , user)
            return redirect('home')
        else:            
            messages.info(request,"Your username OR password is incorrect")
                            
    context={}
    return render(request,"login.html", context)

def logout_page(request):
    logout(request)
    return redirect('login')

 
@login_required(login_url=('login'))
@allowed_users(allowd=['customer'])
def users_profile(request):
    order=Order.objects.all()
    orders= request.user.customer.order_set.all()
    total_orders=orders.count()
    delivered=orders.filter(status="delivered").count()
    pending=orders.filter(status="pending").count()
    context={'orders':orders,
    "total_orders":total_orders,
    "pending":pending,
    'order':order,
    "delivered":delivered
    }
    return render(request,"usersprofile.html",context)

def setting_profile(request):
    user=request.user.customer
    form= CustomerForm(instance=user)
    if request.method=='POST':
        form = CustomerForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('home')    
    context={'form':form}
    return render(request,"setting.html",context)

@login_required(login_url=('login'))
@admin_only
def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status="delivered").count()
    pending=orders.filter(status="pending").count()
    
    context={
        "total_customers":total_customers,
        "total_orders":total_orders,
        "customers":customers,
        "orders":orders,
        "pending":pending,
        "delivered":delivered
    }
    return render(request,"dashboard.html", context)
    

@login_required(login_url=('login'))
@allowed_users(allowd=['admins'])
def products(request):
    products=Product.objects.all()
    context={
        "products":products
    }
    return render(request,"products.html", context)

@login_required(login_url=('login'))
def customers(request, pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    total_orders=orders.count()
    context={
        "customer":customer,
        "total_orders":total_orders,
        "orders":orders
    }
    return render(request,"customers.html",context)

@login_required(login_url=('login'))
def order_create(request):
    form = OrderForm()
    if request.method == 'POST':
    	form = OrderForm(request.POST)
    	if form.is_valid():
    		form.save()
    		return redirect('/')

    context = {'form':form}
    return render(request, 'order_create.html', context)

@login_required(login_url=('login'))
def update_order(request,pk):
    order=Order.objects.get(id=pk)
    form = UpdateOrderForm(instance=order)
    if request.method=='POST':
        form= UpdateOrderForm(request.POST,instance=order)
    if form.is_valid():          
        form.save()        
        return redirect('/')
        
    context={
        'form':form,
    }
    return render(request,"order_create.html",context) 
        
@login_required(login_url=('login'))
def delete_order(request,pk):

    order=Order.objects.get(id=pk)
        
    if request.method=='POST':
        order.delete()
        
        return redirect('/')
        
    context={"order":order}
    return render(request,"delete_order.html",context) 

@login_required(login_url=('login'))
def customer_order(request):
    form = CustomerOrderForm()
    if request.method=='POST':
        form= CustomerOrderForm(request.POST)
    if form.is_valid():          
        form.save()        
        return redirect('/')        
    context={'form':form,
    }
    return render(request,"customer_order.html",context)


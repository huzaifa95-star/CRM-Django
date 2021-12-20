from django.http import HttpResponse
from django.shortcuts import redirect

def unautherized_user(view_func):
    def wrapper_func(request,*args, **kwargs):

        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_func

def allowed_users(allowd=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            group= None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowd:
                return view_func(request,*args, **kwargs)
            else:
               return HttpResponse("Your're restricted to view this page")    
        return wrapper_func
    return decorator        

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group= None
        if request.user.groups.exists():            
            group = request.user.groups.all()[0].name
        if group =='customer':
            return redirect('users')
        if group =='admins':
            return view_func(request,*args,**kwargs)
    return wrapper_func    
from django.shortcuts import render, redirect,get_object_or_404
from service.models import Employees
# create
def home(request):
    data = Employees.objects.all()
    context={
        'data':data
    }
    
    return render(request, 'index.html', context)

# update
def Add(request):
    if request.method =='POST':
       name = request.POST.get('name')
       email = request.POST.get('email') 
       address = request.POST.get('address') 
       phone = request.POST.get('phone') 
       emp = Employees(
           name = name,
           email = email,
           address = address,
           phone = phone
           
       )
       emp.save()
       return redirect('home')
    
    return render(request, 'index.html')

def Edit(request):
    data = Employees.objects.all()
    context = {
        'emp': data
    }
    return render(request, 'index.html', context)

def update(request, id):
    if request.method =='POST':
       name = request.POST.get('name')
       email = request.POST.get('email') 
       address = request.POST.get('address') 
       phone = request.POST.get('phone') 
       emp = Employees(
           id=id,
           name = name,
           email = email,
           address = address,
           phone = phone
           
       )
       emp.save()
       return redirect('home')
    
    
    return redirect(request,'index.html')

# delete

def delete(request, id):
    data = get_object_or_404(Employees, id=id)  
    data.delete()
    return redirect('home')  
    

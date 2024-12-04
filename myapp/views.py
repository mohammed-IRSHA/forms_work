from django.shortcuts import render,redirect
from .models import *
from .forms import contactform,customertform
# Create your views here.
def getall(request):
    data=customer.objects.all()
    return render(request,"new.html",{'my':data})

def frm(request):
    if request.method =='POST':
        form=customertform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ad')
    
    else:
        form = customertform()
        return render(request,"forms.html",{'form':form})
    
    
    
def dele(request,id):
    dlet=customer.objects.get(id=id)
    dlet.delete()
    return redirect('ad')



def cntact(request):
    if request.method == 'POST':
        form1 = contactform(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('ad')
        else:
            return render(request, 'forms1.html', {'form': form1})
    else:
        form1 = contactform()
        return render(request, 'forms1.html', {'form': form1})
    
    
def updt(request,id):
    data=customer.objects.get(id=id)
    if request.method=='POST':
        id=request.POST.get('id')
        item=request.POST.get('item')
        rate=request.POST.get('rate')
        contact=request.POST.get('contact')
        data.id=id
        data.item=item
        data.rate=rate
        contact=contact
        data.save()
        return redirect('ad')   
    return render(request,'updat.html',{'daata':data})     
        
    

    
  
        
    


    

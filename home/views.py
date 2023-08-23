from django.shortcuts import render,redirect
from django.views import View
from datetime import datetime
from home.models import Customer
# Create your views here.

class IndexView(View):
    def get(self,request):
        customer = Customer.objects.all()
        context = {
            "customer": customer
        }
        return render(request,'index.html',context)


class AddView(View):
    def post(self,request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        customer = Customer(name=name, email=email, phone=phone,desc=desc)
        customer.save()
        return redirect('/customer')

    def get(self,request):
        return render(request,'add.html')


class EditView(View):
    def get(self,request,id):
        customer = Customer.objects.get(pk=id)
        context = {
            "customer": customer
        }
        return render(request,'edit.html',context)
        
    def post(self,request,id):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        customer = Customer(id=id,name=name, email=email, phone=phone,desc=desc)
        customer.save()
        return redirect('/customer')
    


class DeleteView(View):
    def get(self,request,id):
        c = Customer.objects.get(pk=id)
        c.delete()
        return redirect('/customer')
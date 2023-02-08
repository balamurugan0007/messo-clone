from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import  JsonResponse
# Create your views here.
import rsa
from .models import catogory,products,info
from django.contrib import messages






def sign_in(request):

    if request.method=="POST":
        name=request.POST["user"]
        email=request.POST['email']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        
        

        obj=info()
        obj.Name=name
        obj.email=email
        
        
        if name=='':
            return render(request,"signin.html",{'error':'please enter the username'})
        
        if email =='':
            return render(request,"signin.html",{'error':'please enter the email'})
        
        if(info.objects.filter(email=email)):
            user=info.objects.filter(email=email)
            for data in user:
                if data.email==email:
                    return render(request,"signin.html",{'error':'email already exits'})
                    

        if password1=='':
            return render(request,"signin.html",{'error':'please enter the password'})
        
        if password1==password2:
            publicKey, privateKey = rsa.newkeys(520)
            msg=password1
            encript = rsa.encrypt(msg.encode(),
                         publicKey)
            print("encrypted string: ", encript)
            obj.pass1=encript
            #obj.save()
            #print(obj)
            return HttpResponseRedirect('/login')
        
        
        

            

        else:
            return render(request,"signin.html",{'error':'please enter the repeat password as a same one'})

    return render(request,"signin.html")

def home(request):
    if request.method=="POST":
        find = request.POST.get('search')
        print(find)
        if (products.objects.filter(name=find)):
            product=products.objects.filter(name=find)
            return render(request,'search.html',{'data':product})
        
        if(catogory.objects.filter(name=find,status=0)):
            catagory=catogory.objects.filter(name=find,status=0)
            return render(request,'search.html',{'data':catagory})
        
        if find:
            err=str('The product not found please search another...!')
            return render(request,'err.html',{'data':err})



        
    
    data=catogory.objects.all()

    
            
            
    return render(request,'home.html',{'data':data})


def collectionsview(request,id):
    if request.method=="POST":
        find = request.POST.get('search')
        print(find)
        if (products.objects.filter(name=find)):
            product=products.objects.filter(name=find)
            return render(request,'search.html',{'data':product})
        
        if(catogory.objects.filter(name=find,status=0)):
            catagory=catogory.objects.filter(name=find,status=0)
            return render(request,'search.html',{'data':catagory})
        
        if find:
            err=str('The product not found please search another...!')
            return render(request,'err.html',{'data':err})

    Catagory=catogory.objects.all()
    for item in Catagory:
        if id==item.id:
            print(id)
            name=catogory.objects.get(id=id)
            print(name)
            if(catogory.objects.filter(name=name,status=0)):
                Products=products.objects.filter(catogory=name)
                for a in Products:
                    print(a.name)
                    print(a.description)


    #if(catogory.objects.filter(name=name,status=0)):
       # Products=products.objects.filter(catogory=name)
                return render(request,"collection.html",{"products":Products,"name":name})
    


def productview(request,id):
    if request.method=="POST":
        find = request.POST.get('search')
        print(find)
        if (products.objects.filter(name=find)):
            product=products.objects.filter(name=find)
            return render(request,'search.html',{'data':product})
        
        if(catogory.objects.filter(name=find,status=0)):
            catagory=catogory.objects.filter(name=find,status=0)
            return render(request,'search.html',{'data':catagory})
        
        if find:
            err=str('The product not found please search another...!')
            return render(request,'err.html',{'data':err})

    
      
    if(products.objects.filter(id=id,status=0)):
        

        Products=products.objects.filter(id=id,status=0)
       
               
       
        return render(request,"product.html",{"products":Products})
    else:
        messages.error(request,"No Such Produtct Found")
        return HttpResponseRedirect ('home')
    
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        if(info.objects.filter(email=email)):
            user=info.objects.filter(email=email)

           

        else:
            return render(request,"login.html",{'error':'enter the correct email or password'})


               
                
                
    return render(request,"login.html",)




def about(request):
    return render(request,"about.html",)






def cart(request):
    
    return render(request,"cart.html",)





def search(request):
    
    return render(request,"search.html",)




    
    




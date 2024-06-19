from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from myapp.form import employee,stdform,curdd
from myapp.models import Tech,crud
# from myapp.form import stdform
# Create your views here.
def emp_reg(request):
    if request.method=="GET":

        emp=employee()
        return render(request,'sample.html',{'form':emp})
    else:
        # return HttpResponse("success")
        frm=employee(request.POST)

        if frm.is_valid():
            frm.save()
            # print(frm)
            return HttpResponse("<Script>window.alert('successfull added');window.location.href='/emp/'</Script>")
        else :
            return HttpResponse('field.....')
    


def stdindex(request):
    student=stdform()
    return render(request,"sample.html",{'form':student})

# def emplo(request):
#     if request.method=='POST':
#         emplo=

def tech_add(request):
    if request.method=="POST":
        fn=request.POST['fname']
        pho=request.FILES['pic']
        print(pho)
        print(fn)
        t=Tech.objects.create(fname=fn,photo=pho)
        t.save()
        return HttpResponse("<Script>window.alert('added successfull.....');window.location.href='/uplo/'</Script>")
    else:
        return render (request,'files.html')
    

#session

def setsession(request):
    request.session['name']="ammu"
    request.session['email']="akila@gamil.com"
    return HttpResponse("session set")

def getsession(request):
    n=request.session["name"]
    e=request.session["email"]
    return HttpResponse (n + "and" +e)

def delsession(request):
    del request.session["name"]
    return HttpResponse("successfully dtt")


#cookie

def setcook(request):
    res=HttpResponse("cookie set")
    res.set_cookie('name','ammu')
    return res

def getcook(request):
    b=request.COOKIES['name']
    return HttpResponse(b)


def crud1(request):
    dat=crud.objects.all()
    return render(request,"crudtable.html",{"data":dat})




def crud2(request):
    if request.method=="GET":

        emp=curdd()
        return render(request,'cruddata.html',{'form':emp})
    else:
        # return HttpResponse("success")
        frm=curdd(request.POST)

        if frm.is_valid():
           frm.save()
        #    print(frm)
           return HttpResponse("<Script>window.alert('successfull added');window.location.href='/crdd/'</Script>")
        else :
            return HttpResponse('field.....')
        
def crud3(request,datakey):
    print(datakey)
    tem=crud.objects.get(id=datakey)
    tem.delete()
    return HttpResponse("<script>window.alert('deleted');window.location.href='/crdv/'</script>")
    # return HttpResponse("<script>window.alert('deleted')</script>")

def crud4(request,de):
    # print(datakey)
    tem=crud.objects.get(id=de)
    # print(tem)
    return render(request,'crudedit.html',{'form':tem})


def crud5(request,d):
    print(d)
    data=crud.objects.get(id=d)
    frm=curdd(request.POST,instance=data)
    print(frm)
    # frm.is_valid()
    frm.save()
    # return HttpResponse('updatd')
    return HttpResponse("<script>window.alert('updated');window.location.href='/crdv/'</script>")
    # return HttpResponse("<script>window.alert('updated')</script>")

def workhome(request):
    return render(request,"workhome.html")

def worklogin(request):
    if request.method=="POST":
        name=request.POST["login"]
        # print(name)
        # passw=request.POST["password"]
        request.session["login"]=name
        # return HttpResponse("gfghdfgdhf")
        return render(request,'workhome.html',{"data":name})
        # return redirect(workhome)
    else:
        return render(request,'worklogin.html')

def edit(request):
    if request.method=="POST":
        x=request.session['login']
        # del x
        # print(x)
        
        return HttpResponse("<script>window.alert('logout succesfull');window.location.href='/w1/'</script>")
    else:
        k=request.session['login']
        # print(k)
        return render(request,'edit.html',{'data':k})
def edit1(request):
    k=request.session['login']
    if request.POST['login']==k:
        return redirect(edit)
    else:
        return redirect(workhome)
from django.shortcuts import render,redirect
from backend.models import admindb,catdb,breeddb,fooddb,contactdb,disrtibuterdb,checkout
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages

#-----------------------------INDEX PAGE----------------------------------#

def indexpage(r):
    return render(r,"index.html")

#-----------------------------ADMIN PAGE----------------------------------#

def adminpage(r):
    return render(r,"admin.html")

def saveadmin(r):
    if r.method == "POST":
        na = r.POST.get('name')
        em = r.POST.get('email')
        pas = r.POST.get('password')
        co = r.POST.get('confirm')
        im = r.FILES['image']
        obj = admindb(Name=na,Email=em,Password=pas,Confirm=co,Image=im)
        obj.save()
        return redirect(adminpage)

def displayadmin(r):
    data = admindb.objects.all()
    return render(r,"displayadmin.html",{"data": data})

def editadmin(r,dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(r,"editadmin.html",{'data':data})

def deleteadmin(r,dataid):
    data=admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)

def updateadmin(r,dataid):
    if r.method == "POST":
        na = r.POST.get('name')
        em = r.POST.get('email')
        pas = r.POST.get('password')
        co = r.POST.get('confirm')
        try:
            img = r.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image
        admindb.objects.filter(id=dataid).update(Name=na,Email=em,Password=pas,Confirm=co,Image=file)
        return redirect(displayadmin)


#-----------------------------CATEGORY PAGE----------------------------------#

def addcategory(r):
    return render(r,"category.html")

def savecategory(r):
    if r.method=="POST":
        ca=r.POST.get('category')
        de = r.POST.get('description')
        im = r.FILES['image']
        obj=catdb(Category=ca,Description=de,Image=im)
        obj.save()
        return redirect(addcategory)

def catdisplay(r):
    data=catdb.objects.all()
    return render(r,"catdisplay.html",{'data':data})

def catedit(r,dataid):
    data = catdb.objects.get(id=dataid)
    print(data)
    return render(r,"catedit.html",{'data':data})

def catdelete(r,dataid):
    data=catdb.objects.filter(id=dataid)
    data.delete()
    return redirect(catdisplay)

def catupdate(req,dataid):
    if req.method=="POST":
        ca = req.POST.get('category')
        de = req.POST.get('description')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = catdb.objects.get(id=dataid).Image
        catdb.objects.filter(id=dataid).update(Category=ca,Description=de,Image=file)
        return redirect(catdisplay)


#-----------------------------BREEDS PAGE----------------------------------#

def addbreeds(r):
    data = catdb.objects.all()
    return render(r,"breeds.html", {'data':data})

def savebreed(r):
    if r.method=="POST":
        br=r.POST.get('breed')
        de = r.POST.get('description')
        ca = r.POST.get('category')
        di = r.POST.get('distributer')
        info = r.POST.get('dinfo')
        im = r.FILES['image']
        obj=breeddb(Breed=br,Description=de,Category=ca,Image=im,Dinfo=info,Distributer=di)
        obj.save()
        return redirect(addbreeds)

def displaybreed(r):
    data=breeddb.objects.all()
    return render(r,"breeddisplay.html",{"data":data})

def editbreed(r,dataid):
    data=breeddb.objects.get(id=dataid)
    da = catdb.objects.all()
    print(data)
    return render(r,"editbreed.html",{"data":data, "da":da})

def deletebreed(r,dataid):
    data=breeddb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaybreed)

def updatebreed(req,dataid):
    if req.method=="POST":
        br = req.POST.get('breed')
        de = req.POST.get('description')
        ca = req.POST.get('category')
        di = req.POST.get('distributer')
        info = req.POST.get('dinfo')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = breeddb.objects.get(id=dataid).Image
        breeddb.objects.filter(id=dataid).update(Breed=br,Description=de,Category=ca,Image=file,Dinfo=info,Distributer=di)
        return redirect(displaybreed)


#-----------------------------LOGIN/LOGOUT PAGE----------------------------------#

def loginpage(r):
    return render(r,"login.html")

def adminlogin(r):
    if r.method == "POST":
        username_r = r.POST.get('username')
        password_r = r.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r,password=password_r)
            if user is not None:
                login(r,user)
                r.session['username']=username_r
                r.session['password']=password_r
                messages.success(r,"log in successfully")
                return redirect(indexpage)
            else:
                messages.error(r,"Error")
                return redirect(loginpage)
        else:
            return redirect(loginpage)
        
def logout(r):
    del r.session['username']
    del r.session['password']
    messages.success(r,"Logout Sucessfully !")
    return redirect(loginpage)


#-----------------------------PET-FOOD PAGE----------------------------------#

def foodpage(r):
    data=catdb.objects.all()
    return render(r,"foodcategory.html",{"data":data})

def savefood(r):
    if r.method=="POST":
        fo=r.POST.get('food')
        pr = r.POST.get('price')
        de = r.POST.get('description')
        ca = r.POST.get('category')
        im = r.FILES['image']
        obj=fooddb(Food=fo,Price=pr,Description=de,Category=ca,Image=im)
        obj.save()
        return redirect(foodpage)

def displayfood(r):
    data=fooddb.objects.all()
    return render(r,"fooddisplay.html",{"data":data})

def editfood(r,dataid):
    data=fooddb.objects.get(id=dataid)
    da=catdb.objects.all()
    print(data)
    return render(r,"editfood.html",{"data":data, "da":da})

def deletefood(r,dataid):
    data=fooddb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayfood)

def updatefood(r,dataid):
    if r.method=="POST":
        fo = r.POST.get('food')
        pr = r.POST.get('price')
        de = r.POST.get('description')
        ca = r.POST.get('category')
        try:
            img = r.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = fooddb.objects.get(id=dataid).Image
        fooddb.objects.filter(id=dataid).update(Food=fo,Price=pr,Description=de,Category=ca,Image=file)
        return redirect(displayfood)

#-----------------------------CONTACT PAGE----------------------------------#

def viewmessage(r):
    data=contactdb.objects.all()
    return render(r,"contactdetails.html",{"data":data})

def deletemessage(r,dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewmessage)


#-----------------------------CHECKOUT PAGE----------------------------------#

def discheckout(r):
    data=checkout.objects.all()
    return render(r,"checkoutdisplay.html",{"data":data})


def delckeckout(r,dataid):
    data=checkout.objects.filter(id=dataid)
    data.delete()
    return redirect(discheckout)

#-----------------------------DISTRIBUTER PAGE----------------------------------#


#
# def savedistributer(r):
#     if r.method=="POST":
#         na=r.POST.get('name')
#         ad = r.POST.get('address')
#         mo = r.POST.get('mobile')
#         ca = r.POST.get('category')
#         img = r.FILES['image']
#         obj=disrtibuterdb(Name=na,Address=ad,Mobile=mo,Category=ca,Image=img)
#         obj.save()
#         return redirect(distributer)
#
# def disdistributer(r):
#     data=disrtibuterdb.objects.all()
#     return render(r,"disdistributer.html",{"data":data})
#
# def editdistributer(r,dataid):
#     data=breeddb.objects.filter(id=dataid)
#     da=disrtibuterdb.objects.all()
#     print(data)
#     return render(r,"editdistributer.html",{"data":data,"da":da})
#
# def updistributer(r,dataid):
#     if r.method == "POST":
#         na = r.POST.get('name')
#         ad = r.POST.get('address')
#         mo = r.POST.get('mobile')
#         ca = r.POST.get('category')
#         try:
#             img = r.FILES['image']
#             fs = FileSystemStorage()
#             file = fs.save(img.name,img)
#         except MultiValueDictKeyError:
#             file = disrtibuterdb.objects.get(id=dataid).Image
#         disrtibuterdb.objects.filter(id=dataid).update(Name=na,Address=ad,Mobile=mo,Category=ca,Image=file)
#         return redirect(disdistributer)
#
# def deldistributer(r,dataid):
#     data = disrtibuterdb.objects.filter(id=dataid)
#     data.delete()
#     return redirect(disdistributer)
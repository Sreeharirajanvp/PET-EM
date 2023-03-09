from django.shortcuts import render,redirect
from backend.models import catdb, fooddb, breeddb,contactdb,disrtibuterdb,cartdb,checkout
from frontend.models import savelogindb
from django.contrib import messages



#-----------------------------HOME PAGE----------------------------------#

def homepage(r):
    data=catdb.objects.all()
    return render(r,"homepage.html",{"data":data})

def aboutpage(r):
    return render(r,"about.html")


def products(r):
    data=catdb.objects.all()
    return render(r,"products.html",{"data":data})



#-----------------------------CONTACT PAGE----------------------------------#


def contact(r):
    return render(r,"contact.html")

def savecontact(r):
    if r.method=="POST":
        na=r.POST.get('name')
        em = r.POST.get('email')
        su = r.POST.get('subject')
        me = r.POST.get('message')
        obj=contactdb(Name=na,Email=em,Subject=su,Message=me)
        obj.save()
        messages.success(r,"Message sent Successfully !")
        return redirect(contact)



#-----------------------------  PETS  ----------------------------------#


def petsection(r):
    data=catdb.objects.all()
    return render(r,"petsection.html",{"data":data})


def petdisplay(r,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = breeddb.objects.filter(Category=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(r, "pets.html", context)


#-----------------------------SINGLE PAGE----------------------------------#

def singlepage(r,dataid):
    data=breeddb.objects.filter(id=dataid)
    return render(r,"singlepage.html",{"data":data})

def foodpagefn(r,dataid):
    data=fooddb.objects.filter(id=dataid)
    return render(r,"foodpage.html",{"data":data})



#-----------------------------PET FOOD----------------------------------#

def petfood(r):
    data=catdb.objects.all()
    return render(r,"petfood.html",{"data":data})

def petfooddisplay(r,itemcatg):
    print("===itemcatg===",itemcatg)
    catg=itemcatg.upper()
    products=fooddb.objects.filter(Category=itemcatg)
    context = {
        'products' : products,
        'catg':catg
    }
    return render(r,"petfooddisplay.html",context)



def mainlogin(r):
    return render(r,"loginpage.html")

def savelogin(r):
    if r.method=="POST":
        us=r.POST.get('username')

        pa = r.POST.get('password')
        co = r.POST.get('confirm')
        obj=savelogindb(Username=us,Password=pa,Confirm=co)
        obj.save()
        return redirect(mainlogin)

def getlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if savelogindb.objects.filter(Username=username_r, Password=password_r).exists():
            req.session['username'] = username_r
            req.session['password'] = password_r
            messages.success(req,"Login Successfully")
            return redirect(homepage)
        else:
            messages.error(req,"Invalid Username or Password !")
            return render(req,'loginpage.html')

def gologout(r):
    del r.session['username']
    del r.session['password']
    return redirect(mainlogin)


#-----------------------------ADD TO CART----------------------------------#


def addtocart(r):
    data=cartdb.objects.all()
    return render(r,"addtocart.html",{"data":data})


def savecart(req):
    if req.method == "POST":
        fo = req.POST.get('food')
        ca = req.POST.get('category')
        qty = req.POST.get('quantity')
        tprice = req.POST.get('totalprice')
        obj = cartdb( Food=fo, Category=ca, Quantity=qty, Price=tprice,)
        obj.save()
        messages.success(req,"Product Added")
        return redirect(homepage)

def deletecart(r,dataid):
    data=cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(addtocart)

def checkoutpage(r):
    data=cartdb.objects.all()
    return render(r,"checkout.html",{"data":data})

def savecheckout(r):
    if r.method=="POST":
        fn=r.POST.get('fname')
        ln=r.POST.get('lname')
        em=r.POST.get('email')
        ad=r.POST.get('address')
        co=r.POST.get('country')
        st=r.POST.get('state')
        pin=r.POST.get('pin')
        noc=r.POST.get('noc')
        ccn=r.POST.get('ccn')
        ex=r.POST.get('expiration')
        cvv=r.POST.get('cvv')
        obj=checkout(Fname=fn,Lname=ln,Email=em,Address=ad,Country=co,State=st,Pin=pin,NOC=noc,CCN=ccn,Expiration=ex,CVV=cvv)
        obj.save()
        messages.success(r,"Ordered Successfully")
        return redirect(checkoutpage)

def delckeckout(r,dataid):
    data=checkout.objects.filter(id=dataid)
    data.delete()
    return redirect()


# -----------------------------DISTRIBUTER----------------------------------#


def distributerinfo(r,dataid):
    data=breeddb.objects.filter(id=dataid)
    return render(r,"distributerinfo.html",{{"data":data}})

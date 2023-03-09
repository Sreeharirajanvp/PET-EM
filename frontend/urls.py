from django.urls import path
from frontend import views

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contact/',views.contact,name="contact"),
    path('products/', views.products, name="products"),
    path('contact/', views.contact, name="contact"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('singlepage/,<int:dataid>/', views.singlepage, name="singlepage"),
    path('petfood/', views.petfood, name="petfood"),
    path('petdisplay/<itemcatg>', views.petdisplay, name="petdisplay"),
    path('petsection/', views.petsection, name="petsection"),
    path('petfooddisplay/<itemcatg>', views.petfooddisplay, name="petfooddisplay"),
    path('foodpagefn/,<int:dataid>/', views.foodpagefn, name="foodpagefn"),
    path('mainlogin/', views.mainlogin, name="mainlogin"),
    path('savelogin/', views.savelogin, name="savelogin"),
    path('getlogin/', views.getlogin, name="getlogin"),
    path('gologout/', views.gologout, name="gologout"),
    path('savecart/', views.savecart, name="savecart"),
    path('addtocart/', views.addtocart, name="addtocart"),
    path('deletecart/<int:dataid>/', views.deletecart, name="deletecart"),
    path('checkoutpage/', views.checkoutpage, name="checkoutpage"),
    path('savecheckout/', views.savecheckout, name="savecheckout"),
    path('distributerinfo/,<int:dataid>/', views.distributerinfo, name="distributerinfo")

]
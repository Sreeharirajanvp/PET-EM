from django.urls import path
from backend import views

urlpatterns=[

    path('indexpage/',views.indexpage,name="indexpage"),
    path('adminpage/',views.adminpage,name="adminpage"),
    path('saveadmin/', views.saveadmin, name="saveadmin"),
    path('displayadmin/',views.displayadmin,name="displayadmin"),
    path('editadmin/,<int:dataid>/',views.editadmin,name="editadmin"),
    path('deleteadmin/,<int:dataid>/',views.deleteadmin,name="deleteadmin"),
    path('updateadmin/,<int:dataid>/',views.updateadmin,name="updateadmin"),

    path('addcategory/', views.addcategory, name="addcategory"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('catdisplay/', views.catdisplay, name="catdisplay"),
    path('catedit/,<int:dataid>/', views.catedit, name="catedit"),
    path('catdelete/,<int:dataid>/', views.catdelete, name="catdelete"),
    path('catupdate/,<int:dataid>/', views.catupdate, name="catupdate"),

    path('addbreeds/', views.addbreeds, name="addbreeds"),
    path('savebreed/', views.savebreed, name="savebreed"),
    path('displaybreed/', views.displaybreed, name="displaybreed"),
    path('editbreed/,<int:dataid>/', views.editbreed, name="editbreed"),
    path('deletebreed/,<int:dataid>/', views.deletebreed, name="deletebreed"),
    path('updatebreed/,<int:dataid>/', views.updatebreed, name="updatebreed"),

    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('logout/', views.logout, name="logout"),

    path('foodpage/', views.foodpage, name="foodpage"),
    path('savefood/', views.savefood, name="savefood"),
    path('displayfood/', views.displayfood, name="displayfood"),
    path('editfood/<int:dataid>/', views.editfood, name="editfood"),
    path('deletefood/,<int:dataid>/', views.deletefood, name="deletefood"),
    path('updatefood/,<int:dataid>/', views.updatefood, name="updatefood"),

    path('viewmessage/', views.viewmessage, name="viewmessage"),
    path('deletemessage/,<int:dataid>/', views.deletemessage, name="deletemessage"),

    path('discheckout/', views.discheckout, name="discheckout"),
    path('delckeckout/,<int:dataid>/', views.delckeckout, name="delckeckout")




    # path('distributer/', views.distributer, name="distributer"),
    # path('savedistributer/', views.savedistributer, name="savedistributer"),
    # path('savedistributer/', views.savedistributer, name="savedistributer"),
    # path('savedistributer/', views.savedistributer, name="savedistributer"),
    # path('disdistributer/', views.disdistributer, name="disdistributer"),
    # path('editdistributer/<int:dataid>/', views.editdistributer, name="editdistributer"),
    # path('updistributer/<int:dataid>/', views.updistributer, name="updistributer"),
    # path('deldistributer/<int:dataid>/', views.deldistributer, name="deldistributer")








]
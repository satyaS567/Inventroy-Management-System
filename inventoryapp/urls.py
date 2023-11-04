from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('search',views.search,name='search'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
]
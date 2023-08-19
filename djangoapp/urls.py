from django.urls import path
from . import views

urlpatterns = [
    path('', views.getUsers),
    path('create', views.addUser),
    path('read/<str:pk>', views.getUser),
    path('update/<str:pk>', views.updateUser),
    path('delete/<str:pk>', views.deleteUser),

    #  notes
    path('notes', views.getNotes),
    path('notes/create', views.addNotes),
    path('notes/read/<str:pk>', views.getNotes),
    path('notes/update/<str:pk>', views.updateNotes),
    path('notes/delete/<str:pk>', views.deleteNotes),

]

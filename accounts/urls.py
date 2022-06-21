from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('apilist/',views.Apilist,name='apilist'),
    path('Create/',views.Create,name='Create'),
    path('Update/<int:pk>/',views.Update,name='Update'),
    path('Delete/<int:pk>/',views.Delete,name='Delete'),

]
    
    # path('apilist/',views.Apilist,name='apilist'),
    # path('Create/',views.Create,name='Create'),
    # path('Update/<int:pk>/',views.Update,name='update'),
    # path('Create/<int:pk>/',views.Delete,name='Delete'),
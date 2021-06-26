from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('delete/<list_id>', views.delete, name='delete'),    
    path('select/<list_id>', views.select, name='select'),    
    path('unselect/<list_id>', views.unselect, name='unselect'),    
    path('edit/<list_id>', views.edit, name='edit'),    

]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('finished/<int:id>/',views.finished,name='finished'),
    path('delete_all',views.delete_all,name='delete_all'),
    path('clear_finished',views.clear_finished,name='clear_finished'),
    path('add',views.add,name='add'),
    path('recurring',views.recurring,name='recurring'),
    path('R_delete/<int:id>/',views.R_delete,name='R_delete'),
    path('R_update/<int:id>/',views.R_update,name='R_update'),
    path('R_finished/<int:id>/',views.R_finished,name='R_finished'),
    path('R_delete_all',views.R_delete_all,name='R_delete_all'),
    path('R_clear_finished',views.R_clear_finished,name='R_clear_finished'),
    path('R_add',views.R_add,name='R_add')
    
]
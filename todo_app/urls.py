from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static

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
    path('R_add',views.R_add,name='R_add'),
    path('progress',views.progress,name='progress'),
    re_path(r'^changechartcolor/(?P<color>[a-z].*)/$', views.changechartcolor,name='changechartcolor'),
    path('changeaudio/<int:audio_number>/',views.changeaudio,name='changeaudio'),
    path('timer',views.timer,name='timer'),
    path('simple_upload',views.simple_upload,name='simple_upload'),
    path('delete_audio/<int:num>/',views.delete_audio,name='delete_audio')

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
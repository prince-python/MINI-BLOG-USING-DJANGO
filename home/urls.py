from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.urls import path


urlpatterns = [
    path('',views.index),
    path('sign_up/',views.signup,name='sign_up'),
    path('login/',views.login,name='login'),
    path('delete<int:id>/',views.delete,name='delete'),
    path('Addblog',views.Addblog,name='Addblog'),
    path('search',views.search),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

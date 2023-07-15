from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name='user'
urlpatterns = [
    path('', views.Homepage.as_view(),name="homepage"),
    path('registration/', views.registration,name="registration"),
    path('login/', views.login,name="login"),
    path('logout/', views.logout,name="logout"),
    
]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

"""SocialCode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from userauthentification.models import Profile
from userauthentification.views import userProfile, follow, EditProfile
from userauthentification.views import sign,signin,signup,outout

from post.views import UserSearch 



from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('userauthentification.urls')),
    path('users/', include('comment.urls')),
    path('sign/', sign,name='sign'),
    path('logup/', signup,name='logup'),
    path('login/',signin,name='login'),
    path('logout/', outout,name='logout' ),
    # Forgot Password
    path("password-reset/", 
    	PasswordResetView.as_view(template_name='sign/password_reset.html'),
    	name="password_reset"),
    

	path("password-reset/done/", 
		PasswordResetDoneView.as_view(template_name='sign/password_reset_done.html'), 
		name="password_reset_done"),
	path("password-reset-confirm/<uidb64>/<token>/", 
		PasswordResetConfirmView.as_view(template_name='sign/password_reset_confirm.html'), 
		name="password_reset_confirm"),

	path("password-reset-complete/", 
		PasswordResetCompleteView.as_view(template_name='sign/password_reset_complete.html'), 
		name="password_reset_complete"),

 
 
 
 
 
    path('post/', include('post.urls')),
    path('search/', UserSearch, name="Search"),
    path('ask/', include('Ask_Chat_Get.urls')),

    path('<username>/', userProfile, name="profile"),
    path('<username>/saved/', userProfile, name="favourite"),
    
    
    path('<username>/follow/<option>', follow, name="follow"),
    
    
    
    
    
    


    ]

# This is used for
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
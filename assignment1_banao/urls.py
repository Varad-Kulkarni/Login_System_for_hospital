"""assignment1_banao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import URLPattern, path
from signup.views import register_Activity, addimg, homep
from signin.views import login_Activity

# from imagesup.views import hotel_image_view, success
# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#     URLPattern += static(settings.MEDIA_URL,
#        document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homep),
    path('signup/', register_Activity),
    path('signin/', login_Activity),
    path('signup/add_img', addimg), 

    # path('image_upload', hotel_image_view, name = 'image_upload'),
    # path('success', success, name = 'success'),
]

# if settings.DEBUG:  
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  

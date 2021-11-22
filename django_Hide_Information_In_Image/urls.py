"""django_Hide_Information_In_Image URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from HomeManagement import views as hm_views
from registration import views as r_views
from profileManagement import views as pm_views
from Encode import views as en_views
from Decode import views as de_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', hm_views.home, name="home"),
                  path('user_list/', hm_views.user_list, name="user_list"),
                  path('registration/', r_views.registration, name="registration"),
                  path('login/', r_views.login_user, name="login"),
                  path('logout/', r_views.logout_user, name="logout"),
                  path('profile/', pm_views.profile, name="profile"),
                  path('update_profile/', pm_views.update_profile, name="update_profile"),
                  path('insert_nickname/', pm_views.insert_nickname, name="insert_nickname"),
                  path('insert_profile_pic/', pm_views.insert_profile_pic, name="insert_profile_pic"),
                  path('insert_cover_pic/', pm_views.insert_cover_pic, name="insert_cover_pic"),
                  path('show_nicknames/', pm_views.show_nicknames, name="show_nicknames"),
                  path('show_profile_pics/', pm_views.show_profile_pics, name="show_profile_pics"),
                  path('show_cover_pics/', pm_views.show_cover_pics, name="show_cover_pics"),
                  path('set_nickname/<int:nickname_id>/', pm_views.set_nickname, name='set_nickname'),
                  path('set_profile_pic/<int:profile_pic_id>/', pm_views.set_profile_pic, name='set_profile_pic'),
                  path('set_cover_pic/<int:cover_pic_id>/', pm_views.set_cover_pic, name='set_cover_pic'),
                  path('encode/', en_views.encode_form, name='encode'),
                  path('encoded_image_list/', en_views.encoded_image_list, name='encoded_image_list'),
                  path('delete/<int:row_id>/', de_views.deleteRow, name='delete'),
                  path('decode/<int:image_id>/', de_views.decode_form, name='decode'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

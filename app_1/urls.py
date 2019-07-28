from django.urls import re_path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'app_1'

urlpatterns = [
    # ex: /
    re_path(r'^$', views.home, name='home'),
    # ex: /register/
    re_path(r'^register/$', views.register, name='register'),
    # ex: /profile/
    re_path(r'^profile/$', views.index, name='index'),
    # ex: /profile/5/
    re_path(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    # ex: /profile/5/history/
    re_path(r'^profile/(?P<user_id>[0-9]+)/history/$', views.history, name='history'),
    # ex: /profile/5/add_food
    re_path(r'^profile/(?P<user_id>[0-9]+)/add_food/$', views.add_food, name='add_food'),
    # ex: /profile/5/add_food/3/delete
    re_path(r'^profile/(?P<user_id>[0-9]+)/item/(?P<item_id>[0-9]+)/delete$', views.delete_food, name='delete_food'),
    # ex: /profile/5/add_food/4/add_ingredient
    re_path(r'^profile/(?P<user_id>[0-9]+)/add_food/(?P<item_id>[0-9]+)/add_ingredient$', views.add_ingredient,
        name='add_ingredient'),
    re_path(r'^profile/(?P<user_id>[0-9]+)/remove_user$', views.remove_user, name='remove_user'),

    re_path(r'^profile/(?P<user_id>[0-9]+)/objective/$', views.objective, name='objective'),

    re_path(r'^profile/(?P<user_id>[0-9]+)/modify_profile/$', views.edit_profile, name='edit_profile'),


    # ex: /login
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name ='app_1/login.html'), name='login'),
    # ex: /logout
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page = '/'), name='logout')



]

"""showtime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(success_url='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html', next_page='login'), name='logout'),
    
    # Home page
    path('', views.home, name='home'),

    # Privacy policy
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),

    # Shows
    path('shows/', views.show_list, name='show_list'),
    path('shows/add/', views.add_show, name='add_show'),
    path('shows/edit/<int:show_id>/', views.edit_show, name='edit_show'),
    path('shows/remove/<int:show_id>/', views.remove_show, name='remove_show'),

    # Workshops
    path('workshops/', views.workshop_list, name='workshop_list'),
    path('workshops/add/', views.add_workshop, name='add_workshop'),
    path('workshops/edit/<int:workshop_id>/', views.edit_workshop, name='edit_workshop'),
    path('workshops/remove/<int:workshop_id>/', views.remove_workshop, name='remove_workshop'),

    # Teams
    path('teams/', views.team_list, name='team_list'),
    path('teams/add/', views.add_team, name='add_team'),
    path('teams/edit/<int:team_id>/', views.edit_team, name='edit_team'),
    path('teams/remove/<int:team_id>/', views.remove_team, name='remove_team'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
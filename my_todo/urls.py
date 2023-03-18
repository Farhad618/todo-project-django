"""my_todo URL Configuration

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
from django.urls import path, include

# import views
from home import home_views, delete_views, update_views, task_views
# from signin import signin_views
# from signup import signup_views
# from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('accounts/', include('allauth.urls')),
    path('', home_views.home, name='home'),
    path('delete/<id>/', delete_views.delete, name='delete'),
    path('update/<id>/', update_views.update, name='update'),
    path('<id>/', task_views.task, name='task'),
    # path('signin/', signin_views.signin, name='signin'),
    # path('signup/', signup_views.signup, name='signup'),
]

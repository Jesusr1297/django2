from django.contrib import admin
from django.urls import path

# module to import urls from other apps
from django.urls import include
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', user_views.register, name='register'),

    path('', include('blog.urls'))
]

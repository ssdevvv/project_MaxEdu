from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_adv.urls')),
    path('lesson_4/', include('app_lesson_4.urls')),
]

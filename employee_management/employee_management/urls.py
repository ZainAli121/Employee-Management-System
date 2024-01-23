from django.contrib import admin
from django.urls import path, include
from django.conf import settings   
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('employee_info.urls')),
    path('attendence/', include('attendence.urls')),
    path('apply_leave/', include('leave_requests.urls')),
    path('', include('users.urls')),
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

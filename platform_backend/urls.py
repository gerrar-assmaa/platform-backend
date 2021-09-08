from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
  #path('admin/', admin.site.urls),
  path('api/',include('main_app.urls')),
  path('sign/',include('signIn_Up.urls')),
  path('downFiles/',include('Stats.urls')),
  path('__debug__/', include(debug_toolbar.urls)),
]

# if settings.DEBUG:
#   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
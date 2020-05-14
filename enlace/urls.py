from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = 'IIIT Kottayam | Enlace 2020'                    # default: "Django Administration"
admin.site.index_title = 'IIITK | Enlace 2k20 Site Admin.'                 # default: "Site administration"
admin.site.site_title = 'Enlace Site Admin.' # default: "Django site admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("",include('main.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

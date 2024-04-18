
from django.contrib import admin
from django.urls import path,include
admin.site.site_header='store front Admin'
admin.site.index_title='Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/',include('playground.urls')),
     path("__deb__/", include("debug_toolbar.urls")),
]
 
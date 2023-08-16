
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "ICE CREAMS"
admin.site.site_title = "Welcome to Ice Creams"
admin.site.index_title = "Welcome to Ice Cream Centre"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]

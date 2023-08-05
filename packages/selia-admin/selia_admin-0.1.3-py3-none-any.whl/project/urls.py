from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(r'^admin/', include('selia_admin.urls')),
]

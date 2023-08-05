from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url('', admin.site.urls),
    url('docs/', include('django.contrib.admindocs.urls'))
]

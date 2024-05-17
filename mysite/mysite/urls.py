from django.contrib import admin
from django.urls import include, path

# include blog urls here
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]

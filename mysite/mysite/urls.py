from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from blog.sitemaps import PostSitemap

# defined sitemaps dictionary
sitemaps = {
    'posts': PostSitemap
}

# include blog urls here

"""
We have defined a URL pattern that matches the sitemap.
xml pattern and uses the sitemap view provided by Django. 
The sitemaps dictionary is passed to the sitemap view.
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    )
]

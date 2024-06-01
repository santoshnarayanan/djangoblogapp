from django.contrib.sitemaps import Sitemap
from .models import Post

"""
defined a custom sitemap by inheriting the Sitemap class of the sitemaps module
"""
class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    """
    The lastmod method receives each object returned by items() and 
    returns the last time the object was modified.
    """
    def lastmod(self, obj):
        return obj.updated
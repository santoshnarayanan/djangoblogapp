from django import template
from ..models import Post

register = template.Library()

"""
creating a simple tag to retrieve the total posts that have been published on the blog
"""
@register.simple_tag
def total_posts():
    return Post.published.count()

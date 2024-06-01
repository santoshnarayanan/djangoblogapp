import markdown
from django.utils.safestring import mark_safe
from django.db.models import Count
from django import template
from ..models import Post


register = template.Library()

"""
creating a simple tag to retrieve the total posts that have been published on the blog
"""
@register.simple_tag
def total_posts():
    return Post.published.count()

"""
create a tag to display the most commented posts
"""
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
        ).order_by('-total_comments')[:count]


"""
create another tag to display the latest posts in the sidebar of the blog
Inclusion tags have to return a dictionary of values, which is used as the 
context to render the specified template
"""
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

"""
create a filter to convert markdown to html
"""
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
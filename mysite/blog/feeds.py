import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post

class LatestPostsFeed(Feed):
    title = 'My blog'
    # It allows you to use a URL reversal before the project’s URL configuration is loaded.
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'

    """
    The items() method retrieves the objects to be included in the feed. 
    We retrieve the last five published posts to include them in the feed
    """
    def items(self):
        return Post.published.all()[:5]

    """
    The title, link, and description attributes correspond to the <title>, <link>, and
    <description> RSS elements, respectively
    """

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        return item.publish
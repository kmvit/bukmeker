from django import template
from articles.models import Article

register = template.Library()
@register.inclusion_tag('tags/article_list.html', takes_context=True)
def article_list(context):
    request = context['request']
    article_list = Article.objects.filter(published=True)
    context_dict = {'article_list':article_list}
    return context_dict

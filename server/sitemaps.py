from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index',
        'userguide',
        'dashboard',
        'price',
        'faq',
        'terms']
    def location(self, item):
        return reverse(item)
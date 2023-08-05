'''
Auto genenel DRF routers
'''

from rest_framework.routers import DefaultRouter

from hi import viewsets

router = DefaultRouter()
router.register('blogs', viewsets.BlogViewSet)
router.register('bingos', viewsets.BingoViewSet)
router.register('authors', viewsets.AuthorViewSet)
'''
Auto genenel DRF routers
'''

from rest_framework.routers import DefaultRouter

from hi import viewsets

router = DefaultRouter()
router.register('blogs', viewsets.BlogViewSet)
router.register('authors', viewsets.AuthorViewSet)
router.register('bingos', viewsets.BingoViewSet)
router.register('gans', viewsets.GanViewSet)
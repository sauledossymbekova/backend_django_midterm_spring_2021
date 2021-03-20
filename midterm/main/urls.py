from views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'journals', JournalViewSet, basename='journal')
urlpatterns = router.urls

# article_manage/urls.py

from article_manage.views import ArticleViewSet, AuthorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'authors', AuthorViewSet, basename='author')
urlpatterns = router.urls
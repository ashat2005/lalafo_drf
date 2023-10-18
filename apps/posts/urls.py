from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewset


router = DefaultRouter()
router.register('posts', PostAPIViewset, "api_posts")

urlpatterns = router.urls   
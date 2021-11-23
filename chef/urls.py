from rest_framework import urlpatterns
from rest_framework import routers
from chef.views import ReceitasViewSet
from rest_framework.routers import DefaultRouter


app_name = 'chef'
router = DefaultRouter()
router.register(r'', ReceitasViewSet)
urlpatterns = router.urls

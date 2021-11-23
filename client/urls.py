from rest_framework import urlpatterns
from rest_framework import routers
from client.views import ReceitasViewSet
from rest_framework.routers import DefaultRouter

app_name = 'client'
router = DefaultRouter()
router.register(r'', ReceitasViewSet)
urlpatterns = router.urls
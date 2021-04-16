from rest_framework import routers

from .views import ToDoListModelViewSet, ToDoListCreateViewSet

router = routers.SimpleRouter()
router.register(r'api/v1', ToDoListModelViewSet)
router.register(r'todo-create', ToDoListCreateViewSet)

urlpatterns = router.urls

from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import TaskViewSet, CreateUserView, TaskListView, TaskRetrieveView, PostListView, PostRetrieveView, AnswerListView, AnswerRetrieveView


# viewsets.ModelViewSetから継承した場合とgenericsから継承した場合でpathの書き方が異なる！
# viewsetsの書き方
router = routers.DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')
# genericsのpathの書き方
urlpatterns = [
    path('list-post/', PostListView.as_view(), name='list-post'),
    path('detail-post/<str:pk>', PostRetrieveView.as_view(), name='detail-post'),
    path('list-task/', TaskListView.as_view(), name='list-task'),
    path('detail-task/<str:pk>', TaskRetrieveView.as_view(), name='detail-task'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
    path('list-answer/', AnswerListView.as_view(), name='list-answer'),
    path('detail-answer/<str:pk>', AnswerRetrieveView.as_view(), name='detail-answer'),
]
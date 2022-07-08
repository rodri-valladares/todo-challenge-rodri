from django.urls import path
from . import views

urlpatterns = [
	path(
        'task/list/',
        views.TaskListApiView.as_view(),
        ),
    path(
        'task/create/',
        views.TaskCreateApiView.as_view(),
        ),
    path(
        'task/detail/<pk>/',
        views.TaskRetrieveApiView.as_view(),
        ),
    path(
        'task/delete/<pk>/',
        views.TaskDeleteView.as_view(),
        ),
    path(
        'task/update/<pk>/',
        views.TaskUpdateView.as_view(),
        ),
    path(
        'task/update-detail/<pk>/',
        views.TaskRetrieveUpdateView.as_view(),
        ),
    path(
        'task/search/<kword>/',
        views.TaskSearchApiView.as_view(),
        ),
]

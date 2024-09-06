from django.urls import path
from . import views

urlpatterns = [
    path("", views.board_list, name="board-list"),
    path("<int:board_id>", views.board_detail, name="board-detail"),
    path("write", views.board_write, name="board-write"),
    path("delete", views.board_delete, name="board-delete"),
    path("<int:board_id>/modify", views.board_modify, name="board-modify"),
]

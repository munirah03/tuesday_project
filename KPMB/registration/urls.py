from django.urls import path
from registration import views

urlpatterns = [
    path(" ", views.index, name="index"),
    path("new_course/", views.new_course, name="new_course"),
    path("course/", views.course, name="course"),
    path("course/update/str:code>", views.update, name='update'),
    path("course/searchpage/", views.searchpage, name='searchpage'),
    path("course/update_data/str:code>", views.update_data, name='update_data'),
]
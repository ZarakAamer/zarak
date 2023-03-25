from django.urls import path
from .views import home, article_details, project_details, contact


urlpatterns = [
    path('', home, name="home"),
    path('project-details/<int:id>', project_details, name="project_details"),
    path('article-details/<int:id>', article_details, name="article_details"),
    path('contact', contact, name="contact"),

]

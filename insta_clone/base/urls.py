from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('', views.PostListView.as_view(), name="home"),
    path('add-post/', views.PostCreateView.as_view(), name="create_post"),
    path('delete-post/<int:pk>', views.PostDeleteView.as_view(),
         name="delete_post"),
    path('update-post/<int:pk>', views.PostUpdate.as_view(),
         name="update_post"),


    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema))
]

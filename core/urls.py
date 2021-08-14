from django.urls import path
from core import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('snippets/', views.Snippet_list.as_view()),
    path('snippets/<int:pk>/', views.Snippet_detail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path ,include
from core import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
        path('', include(router.urls)),
#     path('', views.api_root),

#     path('snippets/', views.SnippetList.as_view(),name='snippet-list'),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('users/', views.UserList.as_view()),
# path('users/<int:pk>/', views.UserDetail.as_view()),
# path('snippets/<int:pk>/highlight/',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     path('users/',
#         views.UserList.as_view(),
#         name='user-list'),
#     path('users/<int:pk>/',
#         views.UserDetail.as_view(),
#         name='user-detail')

]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
# urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from . import views

urlpatterns = [
    path('stream/', views.StreamingPLatform_View.as_view()),
    path('stream/<int:pk>/', views.StreamingPLatform_View.as_view()),
    path('stream/update/<int:pk>/', views.StreamingPLatform_View.as_view()),
    path('stream/delete/<int:pk>/', views.StreamingPLatform_View.as_view()),
    path('watchlist/', views.WatchList_View.as_view()),
    path('watchlist/<int:pk>/', views.WatchList_View.as_view()),
    path('watchlist/<int:pk>/reviews/', views.get_watchlist_review),
    path('watchlist/update/<int:pk>/', views.WatchList_View.as_view()),
    path('watchlist/delete/<int:pk>/', views.WatchList_View.as_view()),
    path('reviews/<int:pk>/', views.Reviews_View.as_view()),
    path('reviews/update/<int:pk>/', views.Reviews_View.as_view()),
    path('reviews/delete/<int:pk>/', views.Reviews_View.as_view()),
]
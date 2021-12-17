from django.urls import path
from . import views

urlpatterns = [
    path('prediction', views.StrokePredictionView.as_view(),
         name="StrokePredictionView"),
    path("detection", views.StrokeDetectionView.as_view(),
         name="StrokeDetectionView")
]

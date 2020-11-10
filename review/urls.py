from django.urls import path
from . import views

urlpatterns = [
    path('<int:atencion>', views.ReviewView.as_view(), name="review_atencion")
]
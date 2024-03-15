from django.urls import path
from .views import StudentsListCreate, StudentsRetrieveUpdateDestroy

urlpatterns = [
    path('students/', StudentsListCreate.as_view()),
    path('students/<int:pk>/', StudentsRetrieveUpdateDestroy.as_view()),
]

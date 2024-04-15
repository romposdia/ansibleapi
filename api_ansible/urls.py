from django.urls import path
from .views import ExecutePlaybookView

urlpatterns = [
    path('execute-playbook/', ExecutePlaybookView.as_view(), name='execute-playbook'),
]
from django.urls import path
from .views import UploadCSVAPIView, DatasetHistoryAPIView, GeneratePDFAPIView

urlpatterns = [
    path('upload/', UploadCSVAPIView.as_view(), name='upload-csv'),
    path('history/', DatasetHistoryAPIView.as_view()),
    path('report/pdf/', GeneratePDFAPIView.as_view()),

]

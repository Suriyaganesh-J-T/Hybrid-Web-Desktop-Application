from django.shortcuts import render

# Create your views here.
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dataset

from reportlab.pdfgen import canvas
from django.http import HttpResponse

class UploadCSVAPIView(APIView):
    def post(self, request):
        csv_file = request.FILES.get('file')

        if not csv_file:
            return Response({"error": "No file uploaded"}, status=400)

        df = pd.read_csv(csv_file)

        summary = {
            "total_equipment": len(df),
            "avg_flowrate": round(df["Flowrate"].mean(), 2),
            "avg_pressure": round(df["Pressure"].mean(), 2),
            "avg_temperature": round(df["Temperature"].mean(), 2),
            "type_distribution": df["Type"].value_counts().to_dict()
        }

        Dataset.objects.create(
            name=csv_file.name,
            summary=summary
        )

        # Keep only last 5 datasets (safe deletion)
        dataset_ids = list(
            Dataset.objects.order_by('uploaded_at')
            .values_list('id', flat=True)
        )

        if len(dataset_ids) > 5:
            ids_to_delete = dataset_ids[:-5]
            Dataset.objects.filter(id__in=ids_to_delete).delete()


        return Response({
            "summary": summary,
            "rows": df.to_dict(orient="records")
        }, status=status.HTTP_200_OK)

    

class DatasetHistoryAPIView(APIView):
    def get(self, request):
        datasets = Dataset.objects.order_by('-uploaded_at')[:5]
        history = [
            {
                "name": d.name,
                "uploaded_at": d.uploaded_at,
                "summary": d.summary
            }
            for d in datasets
        ]
        return Response(history)


class GeneratePDFAPIView(APIView):
    def get(self, request):
        dataset = Dataset.objects.order_by('-uploaded_at').first()

        if not dataset:
            return Response({"error": "No dataset available"}, status=400)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        p = canvas.Canvas(response)
        p.setFont("Helvetica", 12)

        y = 800
        p.drawString(50, y, "Chemical Equipment Report")
        y -= 30

        for key, value in dataset.summary.items():
            p.drawString(50, y, f"{key}: {value}")
            y -= 20

        p.showPage()
        p.save()

        return response
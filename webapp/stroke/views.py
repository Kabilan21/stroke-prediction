from django.http.response import JsonResponse
from core.test import process
from rest_framework.views import APIView

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status

from .forms import PredictionSerializer

from rest_framework.permissions import AllowAny

from PIL import Image
from core.classify import predict


class StrokePredictionView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serialized = PredictionSerializer(request.data)
        values = serialized.data
        prediction = process(
            values['gender'], values['age'], values['hypertension'],
            values['heart_disease'], values['ever_married'], values['work_type'],
            values['residence_type'], values['avg_glucose_level'], values['bmi'], values['smoking_status'])
        return Response(status=status.HTTP_200_OK, data={
            'normal': prediction[0],
            'stroke': prediction[1]
        })


class StrokeDetectionView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        context = {
            "title": "Stroke detection"
        }
        return render(request, template_name="stroke/prediction.html", context=context)

    def post(self, request):
        image = request.FILES.get("image")
        result = predict(Image.open(image))
        return Response(data={
            "detection": result
        })

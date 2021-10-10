from django.shortcuts import render
from django.http import JsonResponse
from core.test import process


def homeview(request):

    return render(request, "stroke/index.html")


def formview(reqest):
    if reqest.method == "POST":
        gender = reqest.POST.data('gender')
        age = reqest.POST.data('age')
        hypertension = reqest.POST.data('hypertension')
        heart_disease = reqest.POST.data('heart_disease')
        ever_married = reqest.POST.data('ever_married')
        work_type = reqest.POST.data('work_type')
        residence_type = reqest.POST.data('residence_type')
        avg_glucose_level = reqest.POST.data('avg_glucose_level')
        bmi = reqest.POST.data('bmi')
        smoking_status = reqest.POST.data('smoking_status')
        probability = process(gender, age, hypertension, heart_disease, ever_married,
                              work_type, residence_type, avg_glucose_level, bmi, smoking_status)

        return JsonResponse(data={'probablility': probability})

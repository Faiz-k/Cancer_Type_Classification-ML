from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns


# Create your views here.
def home(request):
    if request.method == 'POST':
        # Retrieve values for each field
        radius_mean = request.POST.get('radius_mean')
        texture_mean = request.POST.get('texture_mean')
        perimeter_mean = request.POST.get('perimeter_mean')
        area_mean = request.POST.get('area_mean')
        smoothness_mean = request.POST.get('smoothness_mean')
        compactness_mean = request.POST.get('compactness_mean')
        concavity_mean = request.POST.get('concavity_mean')
        concave_points_mean = request.POST.get('concave_points_mean')
        symmetry_mean = request.POST.get('symmetry_mean')
        fractal_dimension_mean = request.POST.get('fractal_dimension_mean')
        radius_se = request.POST.get('radius_se')
        texture_se = request.POST.get('texture_se')
        perimeter_se = request.POST.get('perimeter_se')
        area_se = request.POST.get('area_se')
        smoothness_se = request.POST.get('smoothness_se')
        compactness_se = request.POST.get('compactness_se')
        concavity_se = request.POST.get('concavity_se')
        concave_points_se = request.POST.get('concave_points_se')
        symmetry_se = request.POST.get('symmetry_se')
        fractal_dimension_se = request.POST.get('fractal_dimension_se')
        radius_worst = request.POST.get('radius_worst')
        texture_worst = request.POST.get('texture_worst')
        perimeter_worst = request.POST.get('perimeter_worst')
        area_worst = request.POST.get('area_worst')
        smoothness_worst = request.POST.get('smoothness_worst')
        compactness_worst = request.POST.get('compactness_worst')
        concavity_worst = request.POST.get('concavity_worst')
        concave_points_worst = request.POST.get('concave_points_worst')
        symmetry_worst = request.POST.get('symmetry_worst')
        fractal_dimension_worst = request.POST.get('fractal_dimension_worst')
        

        data = pd.read_csv('C:\\Users\\mf879\\OneDrive\\Desktop\\47_cancertype\\bdiag.csv')
        inputs=data.drop(['id','diagnosis'],'columns')
        output=data['diagnosis']
        X_train, X_test, y_train, y_test = train_test_split(inputs, output, test_size=0.3, random_state=42)
        model = GaussianNB()
        model.fit(X_train, y_train)
        y_pred = model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst	,area_worst	,smoothness_worst	,compactness_worst,	concavity_worst,	concave_points_worst	,symmetry_worst,	fractal_dimension_worst]])
        return render(request, "home.html", context={'y_pred':y_pred })

    return render(request, 'home.html')

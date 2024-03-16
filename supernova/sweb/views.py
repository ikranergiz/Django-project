from django.http import HttpResponse
from django.shortcuts import render
from .forms import HotelForm
import os

from ultralytics import YOLO
from PIL import Image
from django.conf import settings



def detect_objects(image_path, model_path="/Users/ikranergiz/Downloads/django-project/supernova/models/yolov8-small-last.pt"):
    # Load the pretrained YOLO model
    model = YOLO(model_path)

    # Perform inference on the image and save the results
    results = model(image_path, save=True, project="media", name="inference", exist_ok=True)

    detected_image_name = image_path.split('/')[-1]  # inferred image will be in the 'inference' folder
    
    return detected_image_name

# Define your view function
def hotel_image_view(request):
    uploaded_image = None
    detected_image_path = None

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the uploaded image path
            uploaded_image_path = form.instance.hotel_Main_Img.path
            # Detect objects in the uploaded image
            detected_image_name = detect_objects(uploaded_image_path)
            
            
            uploaded_image = form.instance.hotel_Main_Img
            print(uploaded_image)
    else:
        form = HotelForm()

    return render(request, 'index.html', {'form': form, 'uploaded_image': uploaded_image})


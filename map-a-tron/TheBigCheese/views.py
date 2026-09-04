
from tempfile import template
from django.shortcuts import render
import cv2
import numpy as np
from django.http import HttpResponse, Http404
import os
import cv2
from django.conf import settings
from django.shortcuts import render

def index(request):
    template = "main/index.html"
    return render(request, template)

def rendertiff(request):
    tiff_path = r'C:\Users\sammy\source\repos\SammyFejer\map-a-tron\map-a-tron\static\images\8927-3N_Corang_GetlostMap_V15.tif'

    output_name = 'output.jpg'

    # img = cv2.imread('8927-3N_Corang_GetlostMap_V15.tif', cv2.IMREAD_UNCHANGED)

    # if img is None:
    #     raise Http404("TIFF image not found or cannot be read.")

    output_path = os.path.join(settings.MEDIA_ROOT, output_name)
    
    # Only convert if the JPEG doesn't exist yet (Basic Caching)
    if not os.path.exists(output_path):
        image = cv2.imread(tiff_path)
        if image is not None:
            cv2.imwrite(output_path, image)
            
    # Pass the URL of the saved JPEG to the template
    context = {
        'image_url': f"{settings.MEDIA_URL}{output_name}"
    }
    return render(request, 'main/well.html', context)
# Create your views here.

# views.py
import cv2
import os
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import StreamingHttpResponse
from django.shortcuts import render
from .models import File
from .forms import FileUploadForm, ModificationForm
from django.http import HttpResponse
from uploadify.manager.email_manager import send_email_via_zoho
from credentail.settings import TO_EMAIL

# View to upload a file


@login_required(login_url='login/')
def home(request):
    """Show the home page with a list of all files."""
    files = File.objects.all()
    modification_form = ModificationForm()
    return render(request, 'home.html', {
        'modification_form': modification_form,
        'files': files
    })

def custom_login_view(request):
    """Handle login attempts."""
    if request.method == "POST":
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"status_code": 200, "msg": "success"})
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html", {"form": ""})

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.uploaded_by = request.user
            new_file.save()
            return redirect('file_details', file_id=new_file.id)
    else:
        form = FileUploadForm()
    
    return render(request, 'upload_file.html', {'form': form})

# View to display details of a file
@login_required
def file_details(request, file_id):
    file = get_object_or_404(File, id=file_id)
    modifications = file.modifications.all()
    return render(request, 'file_details.html', {'file': file, 'modifications': modifications})

# View to add a modification
@login_required
def add_modification(request, file_id):
    file = get_object_or_404(File, id=file_id)
    
    if request.method == 'POST':
        form = ModificationForm(request.POST)
        if form.is_valid():
            modification = form.save(commit=False)
            modification.file = file
            modification.modified_by = request.user
            modification.save()
            return redirect('file_details', file_id=file.id)
    else:
        form = ModificationForm()
    
    return render(request, 'add_modification.html', {'form': form, 'file': file})

# Path to the video file
VIDEO_PATH = '/home/shashank/Downloads/5e4580be20250205-101205.mp4'

# Open the video file
video_capture = cv2.VideoCapture(VIDEO_PATH)

def video_stream(request):
    # Open the video file in binary mode
    with open(VIDEO_PATH, 'rb') as video_file:
        # Set the content type for video (e.g., video/mp4)
        response = HttpResponse(video_file.read(), content_type='video/mp4')
        # Set the appropriate headers for video streaming
        response['Content-Length'] = os.path.getsize(VIDEO_PATH)
        response['Content-Disposition'] = 'inline; filename="video.mp4"'
        return response

def video_feed(request):
    # Return the video stream response
    return StreamingHttpResponse(video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')



def email(request):
    """Show the home page with a list of all files."""
    send_email_via_zoho(
        subject="e-mail testing",
        body="Welcome to Dialmax",
        recipient_email=TO_EMAIL
    )
    return render(request, 'email.html', {})



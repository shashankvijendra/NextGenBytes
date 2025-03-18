# views.py
import cv2
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import StreamingHttpResponse
from django.shortcuts import render
from .models import File
from .forms import FileUploadForm, ModificationForm
from django.http import HttpResponse

# View to upload a file


@login_required(login_url='login/')
def home(request):
    file = File.objects.all()
    form = ModificationForm()
    return render(request, 'home.html', {'form': form, 'files': file})    

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page or any other page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
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


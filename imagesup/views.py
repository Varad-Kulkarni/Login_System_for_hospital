# #-*- coding: utf-8 -*-
# from imagesup.forms import ProfileForm
# from .models import Profile

# def SaveProfile(request):
#    saved = False
   
#    if request.method == "POST":
#       #Get the posted form
#       MyProfileForm = ProfileForm(request.POST, request.FILES)
      
#       if MyProfileForm.is_valid():
#          profile = Profile()
#          profile.name = MyProfileForm.cleaned_data["name"]
#          profile.picture = MyProfileForm.cleaned_data["picture"]
#          profile.save()
#          saved = True
#    else:
#       MyProfileForm = Profileform()
		
#    return render(request, 'saved.html', locals())

# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .forms import *
  
# Create your views here.
# def hotel_image_view(request):
  
#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES)
  
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = HotelForm()
#     return render(request, 'hotel_image_form.html', {'form' : form})
  
  
# def success(request):
#     return HttpResponse('successfully uploaded')
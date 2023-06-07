from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage  # To upload Profile Picture
from django.urls import reverse
import datetime  # To Parse input DateTime into Python Date Time Object
from django.contrib.auth.decorators import login_required
from esl.forms import AddAdvancedSign, AddAdvancedVideoLecture, AddBeginnerSign, AddBeginnerVideoLecture, AddIntermediateSign, AddIntermediateVideoLecture, SignupInstructorForm
from esl.models import Advanced, AdvancedVideo, Beginner, BeginnerVideo, CustomUser, Dictionary, FeedBackInstructor, Instructor, Intermediate, IntermediateVideo, VideoLecture
from django.contrib.auth.models import User, auth


def instructor_home(request):
    if request.user.is_authenticated:
        status = request.user.instructor.status
        instructor_name_list = []

        instructors = CustomUser.objects.filter(user_type='2')
        for instructor in instructors:
            instructor_name_list.append(instructor.first_name)
            context = {
                "status": status,
                "instructor_name_list": instructor_name_list,

            }
        return render(request, "instructor/instructor_home.html", context)
    else:
        return render(request, "login.html")


def account_status(request):
    status = request.user.instructor.status

    context = {

            "status": status,

        }
    return render(request,"instructor/account_status.html", context)

def signup_instructor(request):
    form = SignupInstructorForm
    context = {
        "form": form
    }
    return render(request, "signup_instructor_form.html", context)



def signup_instructor_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('signup_instructor')
    else:
        form = SignupInstructorForm(data=request.POST,files=request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            document = form.cleaned_data['document']
            phoneNo = form.cleaned_data['phoneNo']
            description = form.cleaned_data['description']
            id_pic = form.cleaned_data['id_pic']
            if password1 == password2:
                if CustomUser.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    return redirect('signup_instructor')
                # elif validate_email('email'):
                # messages.info(request, 'Enter a valid email address')
                # return redirect('signup_instructor')
                elif CustomUser.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('signup_instructor')
                else:
                    
                        user = CustomUser.objects.create_user(username=username, password=password1, email=email,
                                                              first_name=first_name, last_name=last_name, user_type=2)
                        user.save()
                        instructor = Instructor.objects.create(user=user,description=description,phoneNo=phoneNo,document=document,id_pic=id_pic)
                        instructor.save()

                        messages.success(request, "Instructer Added Successfully!")
                        return redirect('signup_instructor')
            else:
                messages.info(request, 'Password not matched')
                return redirect('signup_instructor')
        else:
       
            messages.info(request, 'Form is not Valid')
            return redirect('signup_instructor')

def instructor_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    status = user.instructor.status
    context = {
        'status': status,
        "user": user
    }
    return render(request, 'instructor/instructor_profile.html', context)


def instructor_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('instructor_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('instructor_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('instructor_profile')
# Add beginner sign
@login_required()
def add_beginner_sign(request):
    form = AddBeginnerSign()
    status = True
    context = {
        "status": status,
        "form": form
    }
    return render(request, "instructor/add_beginner_sign.html", context)

@login_required()
def add_beginner_sign_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_new_sign')
    else:
        form = AddBeginnerSign(request.POST, request.FILES)

        if form.is_valid():
            signImage = form.cleaned_data['signImage']
            type = form.cleaned_data['type']
            textForSign = form.cleaned_data['textForSign']
            try:
                dictionary = Dictionary(signImage=signImage, textForSign=textForSign)

                dictionary.save()
                beginner = Beginner(dictionary=dictionary, type=type)
                beginner.save()
                messages.success(request, "Sign Added Successfully!")
                return redirect('add_beginner_sign')
            except:
                messages.error(request, "Failed to Add Sign!")
                return redirect('add_beginner_sign')
        else:
            return redirect('add_beginner_sign')


# Add intermediate sign
@login_required()
def add_intermediate_sign(request):
    form = AddIntermediateSign()
    status = True
    context = {
        "status": status,
        "form": form
    }
    return render(request, "instructor/add_intermediate_sign.html", context)


def add_intermediate_sign_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_intermediate_sign')
    else:
        form = AddIntermediateSign(request.POST, request.FILES)

        if form.is_valid():
            signImage = form.cleaned_data['signImage']
            type = form.cleaned_data['type']
            textForSign = form.cleaned_data['textForSign']
            try:
                dictionary = Dictionary(signImage=signImage, textForSign=textForSign)

                dictionary.save()
                intermediate = Intermediate(dictionary=dictionary, type=type)
                intermediate.save()
                messages.success(request, "Sign Added Successfully!")
                return redirect('add_intermediate_sign')
            except:
                messages.error(request, "Failed to Add Sign!")
                return redirect('add_intermediate_sign')
        else:
            return redirect('add_intermediate_sign')

# Add Advanced sign
@login_required()
def add_advanced_sign(request):
    form = AddAdvancedSign()
    status =True
    context = {
        "status": status,
        "form": form
    }
    return render(request, "instructor/add_advanced_sign.html", context)

@login_required()
def add_advanced_sign_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_new_sign')
    else:
        form = AddAdvancedSign(request.POST, request.FILES)

        if form.is_valid():
            signImage = form.cleaned_data['signImage']
            type = form.cleaned_data['type']
            textForSign = form.cleaned_data['textForSign']
            try:
                dictionary = Dictionary(signImage=signImage, textForSign=textForSign)

                dictionary.save()
                beginner = Advanced(dictionary=dictionary, type=type)
                beginner.save()
                messages.success(request, "Sign Added Successfully!")
                return redirect('add_advanced_sign')
            except:
                messages.error(request, "Failed to Add Sign!")
                return redirect('add_advanced_sign')
        else:
            return redirect('add_advanced_sign')
# Add video lecture
@login_required()
def add_beginner_lecture_video(request):
    form = AddBeginnerVideoLecture()
    status = True
    context = {
        "status": status,
        "form": form
    }
    return render(request,'instructor/add_beginner_lecture_video.html',context)
@login_required()
def add_beginner_lecture_video_save(request):
 
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_beginner_lecture_video')
    else:
        form=AddBeginnerVideoLecture(data=request.POST,files=request.FILES)
        if form.is_valid():
            type = form.cleaned_data['type']
            video = form.cleaned_data['video']
            caption = form.cleaned_data['caption']
          
            try:
                video = VideoLecture(video=video, caption=caption)
                video.save()
                beginner = BeginnerVideo(video=video, type=type)
                beginner.save()
                messages.success(request, "Lecture Video Added Successfully!")
                return redirect('add_beginner_lecture_video')
            except:
                messages.error(request, "Failed to Add Lecture Video!")
                return redirect('add_beginner_lecture_video')

        else:
             return redirect('add_beginner_lecture_video')

@login_required()
def add_intermediate_lecture_video(request):
    form = AddIntermediateVideoLecture()
    status = True
    context = {
        "status": status,
        "form": form
    }
    return render(request,'instructor/add_intermediate_lecture_video.html',context)
@login_required()
def add_intermediate_lecture_video_save(request):
  
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_intermediate_lecture_video')
    else:
        form=AddIntermediateVideoLecture(data=request.POST,files=request.FILES)
        if form.is_valid():
            type = form.cleaned_data['type']
            video = form.cleaned_data['video']
            caption = form.cleaned_data['caption']
          
            try:
                video = VideoLecture(video=video, caption=caption)
                video.save()
                intermediate = IntermediateVideo(video=video, type=type)
                intermediate.save()
                messages.success(request, "Lecture Video Added Successfully!")
                return redirect('add_intermediate_lecture_video')
            except:
                messages.error(request, "Failed to Add Lecture Video!")
                return redirect('add_intermediate_lecture_video')

        else:
           return redirect('add_intermediate_lecture_video')
@login_required()          
def add_advanced_lecture_video(request):
    form = AddAdvancedVideoLecture()
    status = True
    context = {
        "status": status,
        "form": form
    }
    return render(request,'instructor/add_advanced_lecture_video.html',context)
@login_required()
def add_advanced_lecture_video_save(request):
    all_video=VideoLecture.objects.all()
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_advanced_lecture_video')
    else:
        form=AddAdvancedVideoLecture(data=request.POST,files=request.FILES)
        if form.is_valid():
            type = form.cleaned_data['type']
            video = form.cleaned_data['video']
            caption = form.cleaned_data['caption']
          
            try:
                video = VideoLecture(video=video, caption=caption)
                video.save()
                advanced = AdvancedVideo(video=video, type=type)
                advanced.save()
                messages.success(request, "Lecture Video Added Successfully!")
                return redirect('add_advanced_lecture_video')
            except:
                messages.error(request, "Failed to Add Lecture Video!")
                return redirect('add_advanced_lecture_video')

        else:
             return redirect('add_advanced_lecture_video')

# Add beginner sign
@login_required()
def add_beginner_sign(request):
    form = AddBeginnerSign()
    status = True
    context = {
        "status": status,
        "form": form
    }
    return render(request, "instructor/add_beginner_sign.html", context)

@login_required()
def add_beginner_sign_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_new_sign')
    else:
        form = AddBeginnerSign(request.POST, request.FILES)

        if form.is_valid():
            signImage = form.cleaned_data['signImage']
            type = form.cleaned_data['type']
            textForSign = form.cleaned_data['textForSign']
            try:
                dictionary = Dictionary(signImage=signImage, textForSign=textForSign)

                dictionary.save()
                beginner = Beginner(dictionary=dictionary, type=type)
                beginner.save()
                messages.success(request, "Sign Added Successfully!")
                return redirect('add_beginner_sign')
            except:
                messages.error(request, "Failed to Add Sign!")
                return redirect('add_beginner_sign')
        else:
            return redirect('add_beginner_sign')


# Add intermediate sign
@login_required()
def add_intermediate_sign(request):
    form = AddIntermediateSign()
    status = True
    context = {
        "status": status,
        "form": form
    }
    return render(request, "instructor/add_intermediate_sign.html", context)


def add_intermediate_sign_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_intermediate_sign')
    else:
        form = AddIntermediateSign(request.POST, request.FILES)

        if form.is_valid():
            signImage = form.cleaned_data['signImage']
            type = form.cleaned_data['type']
            textForSign = form.cleaned_data['textForSign']
            try:
                dictionary = Dictionary(signImage=signImage, textForSign=textForSign)

                dictionary.save()
                intermediate = Intermediate(dictionary=dictionary, type=type)
                intermediate.save()
                messages.success(request, "Sign Added Successfully!")
                return redirect('add_intermediate_sign')
            except:
                messages.error(request, "Failed to Add Sign!")
                return redirect('add_intermediate_sign')
        else:
            return redirect('add_intermediate_sign')

# Add Advanced sign
@login_required()
def add_advanced_sign(request):
    form = AddAdvancedSign()
    status = True
    context = {
        "status": status,
        "form": form
    }
    return render(request, "instructor/add_advanced_sign.html", context)

@login_required()
def add_advanced_sign_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_new_sign')
    else:
        form = AddAdvancedSign(request.POST, request.FILES)

        if form.is_valid():
            signImage = form.cleaned_data['signImage']
            type = form.cleaned_data['type']
            textForSign = form.cleaned_data['textForSign']
            try:
                dictionary = Dictionary(signImage=signImage, textForSign=textForSign)

                dictionary.save()
                beginner = Advanced(dictionary=dictionary, type=type)
                beginner.save()
                messages.success(request, "Sign Added Successfully!")
                return redirect('add_advanced_sign')
            except:
                messages.error(request, "Failed to Add Sign!")
                return redirect('add_advanced_sign')
        else:
            return redirect('add_advanced_sign')
# Add video lecture
@login_required()
def add_beginner_lecture_video(request):
    form = AddBeginnerVideoLecture()
    status = True
    context = {
        "status": status,
        "form": form
    }
    return render(request,'instructor/add_beginner_lecture_video.html',context)
@login_required()
def add_beginner_lecture_video_save(request):
 
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_beginner_lecture_video')
    else:
        form=AddBeginnerVideoLecture(data=request.POST,files=request.FILES)
        if form.is_valid():
            type = form.cleaned_data['type']
            video = form.cleaned_data['video']
            caption = form.cleaned_data['caption']
          
            try:
                video = VideoLecture(video=video, caption=caption)
                video.save()
                beginner = BeginnerVideo(video=video, type=type)
                beginner.save()
                messages.success(request, "Lecture Video Added Successfully!")
                return redirect('add_beginner_lecture_video')
            except:
                messages.error(request, "Failed to Add Lecture Video!")
                return redirect('add_beginner_lecture_video')

        else:
             return redirect('add_beginner_lecture_video')

@login_required()
def add_intermediate_lecture_video(request):
    form = AddIntermediateVideoLecture()
    status = True
    context = {
        "status": status,
        "form": form
    }
    return render(request,'instructor/add_intermediate_lecture_video.html',context)
@login_required()
def add_intermediate_lecture_video_save(request):
  
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_intermediate_lecture_video')
    else:
        form=AddIntermediateVideoLecture(data=request.POST,files=request.FILES)
        if form.is_valid():
            type = form.cleaned_data['type']
            video = form.cleaned_data['video']
            caption = form.cleaned_data['caption']
          
            try:
                video = VideoLecture(video=video, caption=caption)
                video.save()
                intermediate = IntermediateVideo(video=video, type=type)
                intermediate.save()
                messages.success(request, "Lecture Video Added Successfully!")
                return redirect('add_intermediate_lecture_video')
            except:
                messages.error(request, "Failed to Add Lecture Video!")
                return redirect('add_intermediate_lecture_video')

        else:
           return redirect('add_intermediate_lecture_video')
@login_required()          
def add_advanced_lecture_video(request):
    form = AddAdvancedVideoLecture()
    status = True
    context = {
        "status": status,
        "form": form
    }
    return render(request,'instructor/add_advanced_lecture_video.html',context)
@login_required()
def add_advanced_lecture_video_save(request):
    all_video=VideoLecture.objects.all()
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_advanced_lecture_video')
    else:
        form=AddAdvancedVideoLecture(data=request.POST,files=request.FILES)
        if form.is_valid():
            type = form.cleaned_data['type']
            video = form.cleaned_data['video']
            caption = form.cleaned_data['caption']
          
            try:
                video = VideoLecture(video=video, caption=caption)
                video.save()
                advanced = AdvancedVideo(video=video, type=type)
                advanced.save()
                messages.success(request, "Lecture Video Added Successfully!")
                return redirect('add_advanced_lecture_video')
            except:
                messages.error(request, "Failed to Add Lecture Video!")
                return redirect('add_advanced_lecture_video')

        else:
             return redirect('add_advanced_lecture_video')


def instructor_feedback(request):
    instructor_obj = CustomUser.objects.get(id=request.user.id)
    feedback_data = FeedBackInstructor.objects.filter(Instructor_id=instructor_obj)
    status = True
    context = {
        "status": status,
        "feedback_data": feedback_data
    }
    return render(request, 'instructor/instructor_feedback.html', context)


def instructor_feedback_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method.")
        return redirect('instructor_feedback')
    else:
        feedback = request.POST.get('feedback_message')
        instructor_obj = CustomUser.objects.get(id=request.user.id)

        try:
            add_feedback = FeedBackInstructor(Instructor_id=instructor_obj, feedback=feedback, feedback_reply="")
            add_feedback.save()
            messages.success(request, "Feedback Sent.")
            return redirect('instructor_feedback')
        except:
            messages.error(request, "Failed to Send Feedback.")
            return redirect('instructor_feedback')
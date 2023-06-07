from unicodedata import name
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage  # To upload Profile Picture
from django.urls import reverse
import datetime  # To Parse input DateTime into Python Date Time Object
from django.contrib.auth.decorators import login_required
from esl.forms import SignupLearnerForm
from esl.models import CustomUser, FeedBackLearner
from eslExercise.models import Learner, Level

@login_required()
def learner_home(request):
    if request.user.is_authenticated:
        # For Learner
        learner_name_list = []

        learners = CustomUser.objects.filter(user_type='3')
        for learner in learners:
            learner_name_list.append(learner.first_name)
            context = {
          
            "learner_name_list": learner_name_list,

            }
        return render(request, "learner/learner_home.html", context)
    else:
        render(request,'login.html')


def signup_learner(request):

    return render(request, 'signup_learner_form.html')


def signup_learner_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('signup_learner')
    else:
        form = SignupLearnerForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 == password2:
                if CustomUser.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    return redirect('signup_learner')
                # elif validate_email('email'):
                # messages.info(request, 'Enter a valid email address')
                # return redirect('signup_instructor')
                elif CustomUser.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('signup_learner')
                else:
                    try:
                        user = CustomUser.objects.create_user(username=username, password=password1, email=email,
                                                              first_name=first_name, last_name=last_name,
                                                              user_type=3)
                        user.save()
                        learner = Learner(user=user)
                        learner.save()
                        messages.success(request, "You are Signed Successfully!!!")
                        return redirect('signup_learner')
                    except:
                        messages.error(request, "Signup Failed!")
                        return redirect('signup_learner')
            else:
                messages.info(request, 'Password not matched')
                return redirect('signup_learner')
        else:
            messages.error(request, 'Form is not Valid')
            return redirect('signup_learner')

def learner_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        "user": user
    }
    return render(request, 'learner/learner_profile.html', context)


def learner_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('learner_profile')
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
            return redirect('learner_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('learner_profile')

def learner_feedback(request):
    learner_obj = CustomUser.objects.get(id=request.user.id)
    feedback_data = FeedBackLearner.objects.filter(Learner_id=learner_obj)
    context = {
        "feedback_data": feedback_data
    }
    return render(request, 'learner/learner_feedback.html', context)


def learner_feedback_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method.")
        return redirect('learner_feedback')
    else:
        feedback = request.POST.get('feedback_message')
        learner_obj = CustomUser.objects.get(id=request.user.id)

        try:
            add_feedback = FeedBackLearner(Learner_id=learner_obj, feedback=feedback, feedback_reply="")
            add_feedback.save()
            messages.success(request, "Feedback Sent.")
            return redirect('learner_feedback')
        except:
            messages.error(request, "Failed to Send Feedback.")
            return redirect('learner_feedback')
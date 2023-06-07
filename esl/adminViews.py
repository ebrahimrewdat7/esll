import os

from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage  # To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required

from esl.forms import AddAdminForm,SignupInstructorForm,SignupLearnerForm, AddBeginnerVideoLecture, AddAdvancedSign,AddAdvancedVideoLecture,AddIntermediateVideoLecture
from esl.models import BeginnerVideo, CustomUser, Dictionary, Beginner, FeedBackInstructor, FeedBackLearner, Instructor, VideoLecture, Advanced,AdvancedVideo, IntermediateVideo
from eslExercise.models import Learner
from esl.forms import AddBeginnerSign, AddIntermediateSign
from esl.learnViews import intermediate
from esl.models import Intermediate


@login_required()
def admin_home(request):
    if request.user.is_authenticated:

        all_admin_count = CustomUser.objects.filter(user_type='1').count()
        all_beginner_sign_count = Beginner.objects.all().count()
        all_intermediate_sign_count = Intermediate.objects.all().count()
        all_advanced_sign_count = Advanced.objects.all().count()
        all_learner_count = CustomUser.objects.filter(user_type='3').count()
        all_instructor_count = Instructor.objects.filter(status=True).count()
        all_unapproved_instructor_count = Instructor.objects.filter(status=False).count()
        learner_feedback = FeedBackLearner.objects.filter(feedback_reply='').count()
        instructor_feedback = FeedBackInstructor.objects.filter(feedback_reply='').count()

        # For Admin
        admin_name_list = []

        admins = CustomUser.objects.filter(user_type='1')
        for admin in admins:
            admin_name_list.append(admin.first_name)
        # For Instructor
        instructor_name_list = []

        instructors = CustomUser.objects.filter(user_type='2')
        for instructor in instructors:
            instructor_name_list.append(instructor.first_name)

        # For Learner
        learner_name_list = []

        learners = CustomUser.objects.filter(user_type='3')
        for learner in learners:
            learner_name_list.append(learner.first_name)

        context = {
            "all_beginner_sign_count": all_beginner_sign_count,
            "all_intermediate_sign_count": all_intermediate_sign_count,
            "all_advanced_sign_count": all_advanced_sign_count,
            "learner_feedback": learner_feedback,
            "instructor_feedback": instructor_feedback,
            "all_learner_count": all_learner_count,
            "all_instructor_count": all_instructor_count,
            "all_admin_count": all_admin_count,
            "admin_name_list": admin_name_list,
            "instructor_name_list": instructor_name_list,
            "learner_name_list": learner_name_list,
            "all_unapproved_instructor_count": all_unapproved_instructor_count
        }
        return render(request, "admin/home_content.html", context)
    else:
        render(request, "login.html")


def add_admin(request):
    form = AddAdminForm()
    context = {
        "form": form
    }
    return render(request, 'admin/add_admin.html', context)


def add_admin_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_admin')
    else:
        form = AddAdminForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                      is_superuser=True, first_name=first_name, last_name=last_name,
                                                      user_type=1)

                user.save()
                messages.success(request, "Admin Added Successfully!")
                return redirect('add_admin')
            except:
                messages.error(request, "Failed to Add Student!")
                return redirect('add_admin')
        else:
            return redirect('add_admin')

@login_required()
def add_instructor(request):
    form = SignupInstructorForm()
    context = {
        "form": form
    }
    return render(request, 'admin/add_instructor.html', context)

@login_required()
def add_instructor_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_instructor')
    else:
        form = SignupInstructorForm(request.POST, request.FILES)

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
                    return redirect('add_instructor')
                # elif validate_email('email'):
                # messages.info(request, 'Enter a valid email address')
                # return redirect('signup_instructor')
                elif CustomUser.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('add_instructor')
                else:
                    
                        user = CustomUser.objects.create_user(username=username, password=password1, email=email,
                                                              first_name=first_name, last_name=last_name, user_type=2)
                        user.save()
                        instructor = Instructor.objects.create(user=user,description=description,phoneNo=phoneNo,document=document,id_pic=id_pic)
                        instructor.save()
                        messages.success(request, "Instructer Added Successfully!")
                        return redirect('add_instructor')
         
            else:
    
                messages.info(request, 'Password not matched')
                return redirect('add_instructor')
        else:
       
            messages.info(request, 'Form is not Valid')
            return redirect('add_instructor')

@login_required()
def add_learner(request):
    form = SignupLearnerForm()
    context = {
        "form": form
    }
    return render(request, 'admin/add_learner.html', context)

@login_required()
def add_learner_save(request):
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
                    return redirect('add_learner')
                # elif validate_email('email'):
                # messages.info(request, 'Enter a valid email address')
                # return redirect('signup_instructor')
                elif CustomUser.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('add_learner')
                else:
                    try:
                        user = CustomUser.objects.create_user(username=username, password=password1, email=email,
                                                              first_name=first_name, last_name=last_name,
                                                              user_type=3)
                        user.save()
                        learner = Learner(user=user)
                        learner.save()
                        messages.success(request, "Learner Added Successfully!!!")
                        return redirect('add_learner')
                    except:
                        messages.error(request, "Adding Learner Failed!")
                        return redirect('add_learner')
            else:
                messages.info(request, 'Password not matched')
                return redirect('add_learner')
        else:
            messages.error(request, 'Form is not Valid')
            return redirect('add_learner')

@login_required()
def approve_instructor(request):
    instructors = Instructor.objects.filter(status=False).all()
    

    context = {
        "instructors": instructors
        

    }
    return render(request, "admin/approve_instructor.html", context)

@login_required()
def approve_instructor_detail(request, id):
    user = CustomUser.objects.get(id=id)
    instructor = Instructor.objects.filter(user=user)
    count = Instructor.objects.filter(status=False).count()
    id = id

    context = {
        
        "instructor": instructor,
        "count": count,
        "id": id

    }
    return render(request, "admin/approve_instructor_detail.html", context)

@login_required()
def decline(request, id):
    instructor = CustomUser.objects.get(id=id)
    
    if instructor.delete():
        messages.success(request, "Declined successfully!")
    else:
        messages.error(request, "Declined Failed!")

    return redirect('approve_instructor')

@login_required()
def approve(request, id):
    try:
        Instructor.objects.filter(id=id).update(status=True)

        messages.success(request, "Instructor Approved successfully!")
    except:
        messages.error(request, "Approval Failed!")

    return redirect('approve_instructor')

@login_required()
def manage_instructor(request):
    instructors = Instructor.objects.filter(status=True)
    
    context = {
        "instructors": instructors
    }
    return render(request, "admin/manage_instructor_template.html", context)
@login_required()
def edit_instructor(request, id):
    instructor = Instructor.objects.get(user_id=id)

    context = {
        "instructor": instructor,
    }
    return render(request, "admin/edit_instructor_template.html", context)

@login_required()
def edit_instructor_save(request,id):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
       
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
       

        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Instructor Model


            messages.success(request, "Instructor Updated Successfully.")
            return redirect('/edit_instructor/'+id)

        except:
            messages.error(request, "Failed to Update Instructor.")
            return redirect('/edit_instructor/'+id)


@login_required()
def delete_instructor(request,id):
    instructor = CustomUser.objects.get(id=id)
    try:
        instructor.delete()
        messages.success(request, "Instructor Deleted Successfully.")
        return redirect('manage_instructor')
    except:
        messages.error(request, "Failed to Delete Instructor.")
        return redirect('manage_instructor')
@login_required()
def manage_learner(request):
    learners = CustomUser.objects.filter(user_type='3')
    context = {
        "learners": learners
    }
    return render(request, 'admin/manage_learner_template.html', context)

def edit_learner(request,id):
    learner = CustomUser.objects.get(id=id)
   
    context = {
        "learner": learner,
    }
    return render(request, "admin/edit_learner_template.html", context)

@login_required()
def edit_learner_save(request,id):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')


        try:
            # INSERTING into Customuser Model
            user = CustomUser.objects.get(id=id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()
            
            # INSERTING into Instructor Model


            messages.success(request, "Learner Updated Successfully.")
            return redirect('/edit_learner/'+id)

        except:
            messages.error(request, "Failed to Update Instructor.")
            return redirect('/edit_learner/'+id)


@login_required()
def delete_learner(request,id):
    learner = CustomUser.objects.get(id=id)
    try:
        learner.delete()
        messages.success(request, "Learner Deleted Successfully.")
        return redirect('manage_learner')
    except:
        messages.error(request, "Failed to Delete Learner.")
        return redirect('manage_learner')


# Managr learning materials
@login_required()
def manage_beginner_sign(request):
    sign = Beginner.objects.all()
    context = {
        "sign": sign
    }
    return render(request, 'admin/manage_beginner_sign.html', context)
@login_required()
def manage_intermediate_sign(request):
    sign = Intermediate.objects.all()
    context = {
        "sign": sign
    }
    return render(request, 'admin/manage_intermediate_sign.html', context)
@login_required()
def manage_advanced_sign(request):
    sign = Advanced.objects.all()
    context = {
        "sign": sign
    }
    return render(request, 'admin/manage_advanced_sign.html', context)

@login_required()
def manage_video(request):
    learners = CustomUser.objects.filter(user_type='3')
    context = {
        "learners": learners
    }
    return render(request, 'admin/manage_learner_template.html', context)
@login_required()
def delete_beginner_sign(request,id):
    sign = Dictionary.objects.get(signId=id)
    try:
        sign.delete()
        messages.success(request, "Sign Deleted Successfully.")
        return redirect('manage_beginner_sign')
    except:
        messages.error(request, "Failed to Delete Sign.")
        return redirect('manage_beginner_sign')

@login_required()
def delete_intermediate_sign(request,id):
    sign = Dictionary.objects.get(signId=id)
    try:
        sign.delete()
        messages.success(request, "Sign Deleted Successfully.")
        return redirect('delete_intermediate_sign')
    except:
        messages.error(request, "Failed to Delete Sign.")
        return redirect('delete_intermediate_sign')
@login_required()
def delete_advanced_sign(request,id):
    sign = Dictionary.objects.get(signId=id)
    try:
        sign.delete()
        messages.success(request, "Sign Deleted Successfully.")
        return redirect('manage_advanced_sign')
    except:
        messages.error(request, "Failed to Delete Sign.")
        return redirect('manage_advanced_sign')
@login_required()
def edit_beginner_sign(request,id):
    sign = Beginner.objects.get(dictionary_id=id)
    form = AddBeginnerSign
   
    context = {
        "form": form,
        "sign": sign,
    }
    return render(request, "admin/edit_beginner_sign.html", context)

@login_required()
def edit_beginner_sign_save(request,id):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('/edit_beginner_sign/'+id)
    else:
        form = AddBeginnerSign(request.POST, request.FILES)
        if form.is_valid():
            signImage = form.cleaned_data['signImage']
            type = form.cleaned_data['type']
            textForSign = form.cleaned_data['textForSign']
     
       
            try:    
                dic = Dictionary.objects.get(signId=id)
                dic.signImage = signImage
                dic.textForSign = textForSign 
                
                dic.save()
           
                beginner = Beginner.objects.get(dictionary_id=dic)

                beginner.type = type
             
                beginner.save()
                messages.success(request, "Sign Updated Successfully!")
                return redirect('/edit_beginner_sign/'+id)
            except:
                messages.error(request, "Failed to Update Sign!")
                return redirect('/edit_beginner_sign/'+id)
        else:
            messages.error(request, "Failed to Update Sign!")
            return redirect('/edit_beginner_sign/'+id)
@login_required()
def edit_intermediate_sign(request,id):
    sign = Intermediate.objects.get(dictionary_id=id)
    form = AddIntermediateSign
   
    context = {
        "form": form,
        "sign": sign,
    }
    return render(request, "admin/edit_intermediate_sign.html", context)

@login_required()
def edit_intermediate_sign_save(request,id):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('/edit_intermediate_sign/'+id)
    else:
        form = AddIntermediateSign(request.POST, request.FILES)
        if form.is_valid():
            signImage = form.cleaned_data['signImage']
            type = form.cleaned_data['type']
            textForSign = form.cleaned_data['textForSign']
     
       
            try:    
                dic = Dictionary.objects.get(signId=id)
                dic.signImage = signImage
                dic.textForSign = textForSign 
                
                dic.save()
           
                beginner = Intermediate.objects.get(dictionary_id=dic)

                beginner.type = type
             
                beginner.save()
                messages.success(request, "Sign Updated Successfully!")
                return redirect('/edit_intermediate_sign/'+id)
            except:
                messages.error(request, "Failed to Update Sign!")
                return redirect('/edit_intermediate_sign/'+id)
        else:
            messages.error(request, "Failed to Update Sign!")
            return redirect('/edit_intermediate_sign/'+id)
@login_required()
def edit_advanced_sign(request,id):
    sign = Advanced.objects.get(dictionary_id=id)
    form = AddAdvancedSign
   
    context = {
        "form": form,
        "sign": sign,
    }
    return render(request, "admin/edit_advanced_sign.html", context)

@login_required()
def edit_advanced_sign_save(request,id):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('/edit_advanced_sign/'+id)
    else:
        form = AddAdvancedSign(request.POST, request.FILES)
        if form.is_valid():
            signImage = form.cleaned_data['signImage']
            type = form.cleaned_data['type']
            textForSign = form.cleaned_data['textForSign']
     
       
            try:    
                dic = Dictionary.objects.get(signId=id)
                dic.signImage = signImage
                dic.textForSign = textForSign 
                
                dic.save()
           
                advanced = Advanced.objects.get(dictionary_id=dic)

                advanced.type = type
             
                advanced.save()
                messages.success(request, "Sign Updated Successfully!")
                return redirect('/edit_advanced_sign/'+id)
            except:
                messages.error(request, "Failed to Update Sign!")
                return redirect('/edit_advanced_sign/'+id)
        else:
            messages.error(request, "Failed to Update Sign!")
            return redirect('/edit_advanced_sign/'+id)
@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_textForSign_exist(request):
    textForSign = request.POST.get("textForSign")
    user_obj = Dictionary.objects.filter(textForSign=textForSign).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@login_required()
def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context = {
        "user": user
    }
    return render(request, 'admin/admin_profile.html', context)

@login_required()
def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
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
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')


@login_required()
def instructor_feedback_message(request):
    feedbacks = FeedBackInstructor.objects.all()
    context = {
        "feedbacks": feedbacks
    }
    return render(request, 'admin/instructor_feedback_template.html', context)


@csrf_exempt
@login_required()
def instructor_feedback_message_reply(request):
    feedback_id = request.POST.get('id')
    feedback_reply = request.POST.get('reply')

    try:
        feedback = FeedBackInstructor.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
        return HttpResponse("True")

    except:
        return HttpResponse("False")

@login_required()
def learner_feedback_message(request):
    feedbacks = FeedBackLearner.objects.all()
    context = {
        "feedbacks": feedbacks
    }
    return render(request, 'admin/learner_feedback_template.html', context)


@csrf_exempt
@login_required()
def learner_feedback_message_reply(request):
    feedback_id = request.POST.get('id')
    feedback_reply = request.POST.get('reply')

    try:
        feedback = FeedBackLearner.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
        return HttpResponse("True")

    except:
        return HttpResponse("False")
@login_required()
def delete_instructor_feedback(request,id):
    feedback = FeedBackInstructor.objects.get(id=id)
    try:
        feedback.delete()
        messages.success(request, "Feedback Deleted Successfully.")
        return redirect('instructor_feedback_message')
    except:
        messages.error(request, "Failed to Delete Feedback.")
        return redirect('instructor_feedback_message')
@login_required()
def delete_learner_feedback(request,id):
    feedback = FeedBackLearner.objects.get(id=id)
    try:
        feedback.delete()
        messages.success(request, "Feedback Deleted Successfully.")
        return redirect('learner_feedback_message')
    except:
        messages.error(request, "Failed to Delete Feedback.")
        return redirect('learner_feedback_message')
import time
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from agora_token_builder import RtcTokenBuilder
import random
import json
from esl.UserBackEnd import UserBackEnd
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from esl.forms import SignupLearnerForm
from esl.models import Instructor, CustomUser
from esl.adminViews import admin_home
from esl.learnerViews import learner_home
from esl.instructorViews import instructor_home


def home(request):
    if request.user.is_authenticated:
        user = request.user
        user_type = user.user_type
        if user_type == '1':
            return redirect(admin_home)
        elif user_type == '2':
            return redirect(instructor_home)
        else:
            return redirect(learner_home)
    else:
        return render(request, "index.html")



def login(request):
    return render(request, "login.html")

def courses(request):
    return render(request, "courses.html")

def about(request):
    return render(request, "about.html")

def do_login(request):
    
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = UserBackEnd.authenticate(request,username,password
                                         )
        if user is not None:
            auth.login(request, user)
            
            user_type = user.user_type
            
            # return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_home')

            elif user_type == '2':
             
                return redirect('instructor_home')

            elif user_type == '3':
                # return HttpResponse("learner Login")
                return redirect('learner_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            return redirect('login')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('login')


def validate_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return False
    except ValidationError:
        return True

def signup_instructor(request):
    return render(request, 'signup_instructor_form.html')


def signup_instructor_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('signup_instructor')
    else:
        form = SignupLearnerForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                      is_superuser=True, first_name=first_name, last_name=last_name,
                                                      user_type=3)

                user.save()
                messages.success(request, "Signed Successfully!")
                return redirect('signup_instructor')
            except:
                messages.error(request, "Signup Failed!")
                return redirect('signup_instructor')
        else:
            return redirect('signup_instructor')
def signup_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup_student')
            elif validate_email('email'):
                messages.info(request, 'Enter a valid email address')
                return redirect('signup_student')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup_student')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name,
                                                last_name=last_name, user_type=2)
                user.save();
                print('user created')
        else:
            messages.info(request, 'Password not matched')
            return redirect('signup_student')
        return redirect('signup_student')
    return render(request, 'signup_student.html')

# Video call
def lobby(request):
    return render(request, 'video_call/lobby.html')


def room(request):
    return render(request, 'video_call/room.html')


def getToken(request):
    appId = "eacfe7d8bc2a447d870a191a7781a6c7"
    appCertificate = "ab5a3099591c43c88ff6fe1c38cf005e"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name': data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name': member.name}, safe=False)


@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)




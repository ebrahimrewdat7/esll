from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from eslVideo.models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required()
def lobby(request):
    
    if request.user.user_type == '2':
        status = request.user.instructor.status
        base_template_name = 'instructor/base_template.html'

    elif request.user.user_type == '1':
        status = True
        base_template_name = 'admin/base_template.html'
    else:
        status = True
        base_template_name = 'learner/base_template.html'
    context = {
            'status': status,
            'base_template_name': base_template_name
        }
    return render(request,'base/lobby.html', context)

@login_required()
def room(request):
    return render(request, 'base/room.html')

@login_required()
def getToken(request):
    appId = "fc2786a85b1a40f886875e9f9890ad27"
    appCertificate = "71a8d7cc235c40218e72a3c2db3f66f1"
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

    return JsonResponse({'name':data['name']}, safe=False)

@login_required()
def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

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
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from esl.models import CustomUser
from .models import Friends, Messages
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from chat.serializers import MessageSerializer


def getFriendsList(id):
    """
    Get the list of friends of the  user
    :param: user id
    :return: list of friends
    """
    try:
        user = CustomUser.objects.get(id=id)
        ids = list(user.friends_set.all())
        friends = []
        for id in ids:
            num = str(id)
            fr = CustomUser.objects.get(id=int(num))
            friends.append(fr)
        return friends
    except:
        return []


def getUserId(username):
    """
    Get the user id by the username
    :param username:
    :return: int
    """
    use = CustomUser.objects.get(username=username)
    id = use.id
    return id


def index(request):
    """
    Return the home page
    :param request:
    :return:
    """
    if not request.user.is_authenticated:
        print("Not Logged In!")
        return render(request, "login.html", {})
    else:
        if request.user.user_type == '2':
            status = request.user.instructor.status
            base_template_name = 'instructor/base_template.html'
        elif request.user.user_type == '1':
            status = True
            base_template_name = 'admin/base_template.html'
        else:
            status = True
            base_template_name = 'learner/base_template.html'
        username = request.user.username
        id = getUserId(username)
        friends = getFriendsList(id)
        context = {
            'friends': friends,
            'id': id,
            'status': status,
            'base_template_name': base_template_name
        }

        return render(request, "chat/Base.html", context)


def search(request):
    """
    Search users page
    :param request:
    :return:
    """
    if request.user.user_type == '2':
        status = request.user.instructor.status
        base_template_name = 'instructor/base_template.html'
    elif request.user.user_type == '1':
        status = True
        base_template_name = 'admin/base_template.html'
    else:
        status = True
        base_template_name = 'learner/base_template.html'
    users = list(CustomUser.objects.all())
    for user in users:
        if user.username == request.user.username:
            users.remove(user)
            break

    if request.method == "POST":
        print("SEARCHING!!")
        query = request.POST.get("search")
        user_ls = []
        for user in users:
            if query in user.first_name or query in user.username:
                user_ls.append(user)
        context = {

            'status': status,
            'base_template_name': base_template_name,
            'user': user_ls
        }
        return render(request, "chat/search.html", context)

    try:
        users = users[:10]
    except:
        users = users[:]
    id = getUserId(request.user.username)
    friends = getFriendsList(id)
    context = {
    'users': users,
    'friends': friends,
    'status': status,
    'base_template_name': base_template_name,
  
    }
    return render(request, "chat/search.html", context)


def addFriend(request,name):
    """
    Add a user to the friend's list
    :param request:
    :param name:
    :return:
    """

    username = request.user.username
    id = getUserId(username)
    friend = CustomUser.objects.get(username=name)
    curr_user = CustomUser.objects.get(id=id)
    print(curr_user.first_name)
    ls = curr_user.friends_set.all()
    flag = 0
    for username in ls:
        if username.friend == friend.id:
            flag = 1
            break
    if flag == 0:
        print("Friend Added!!")
        curr_user.friends_set.create(friend=friend.id)
        friend.friends_set.create(friend=id)
    return redirect("/search")


def chat(request, username):
    """
    Get the chat between two users.
    :param request:
    :param username:
    :return:
    """
    if not request.user.is_authenticated:
        print("Not Logged In!")
        return render(request, "login.html", {})
    else:
        if request.user.user_type == '2':
            status = request.user.instructor.status
            base_template_name = 'instructor/base_template.html'
        elif request.user.user_type == '1':
            status = True
            base_template_name = 'admin/base_template.html'
        else:
            status = True
            base_template_name = 'learner/base_template.html'
    if request.user.user_type == '2':
        status = request.user.instructor.status
        base_template_name = 'instructor/base_template.html'
    elif request.user.user_type == '1':
        status = True
        base_template_name = 'admin/base_template.html'
    else:
        status = True
        base_template_name = 'learner/base_template.html'
    friend = CustomUser.objects.get(username=username)
    id = getUserId(request.user.username)
    curr_user = CustomUser.objects.get(id=id)
    messages = Messages.objects.filter(sender_name=id, receiver_name=friend.id) | Messages.objects.filter(sender_name=friend.id, receiver_name=id)

    if request.method == "GET":
        friends = getFriendsList(id)
        return render(request, "chat/messages.html",
                      {'base_template_name': base_template_name,
                        'messages': messages,
                       'friends': friends,
                       'curr_user': curr_user, 'friend': friend, "base_template_name": base_template_name})

@csrf_exempt
def message_list(request, sender=None, receiver=None):
    if request.method == 'GET':
        messages = Messages.objects.filter(sender_name=sender, receiver_name=receiver, seen=False)
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.seen = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

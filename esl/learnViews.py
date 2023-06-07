from multiprocessing import context
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from esl.models import Beginner, Dictionary, VideoLecture

@login_required()
def beginner(request):
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
        'status': status,
        'base_template_name': base_template_name
    }
    
    return render(request,'learn/beginner.html',context)
    
@login_required()
def intermediate(request):
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
        'status': status,
        'base_template_name': base_template_name
    }
    
    return render(request,'learn/intermediate.html',context)

@login_required()
def advanced(request):
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
        'status': status,
        'base_template_name': base_template_name
    }
    
    return render(request,'learn/advanced.html',context)

# Beginner Sign languages
def eng_alphabet(request):
    all_eng_alphabets = Dictionary.objects.filter(beginner__type="English").all()
    beginner = VideoLecture.objects.filter(beginnervideo__type="English").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'

    context = {
         'status': status,
        "all_eng_alphabets": all_eng_alphabets,
        'base_template_name': base_template_name,
        "beginner": beginner,

    }
    return render(request, "learn/beginner/eng_alphabet.html", context)


def amharic_alphabet(request):
    all_amharic_alphabets = Dictionary.objects.filter(beginner__type="Amharic").all()
    amharic_video = VideoLecture.objects.filter(beginnervideo__type="Amharic").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
        "status": status,
        "all_amharic_alphabets": all_amharic_alphabets,
         "amharic_video": amharic_video,
        'base_template_name': base_template_name
    }
    return render(request, "learn/beginner/amharic_alphabet.html", context)

def number(request):
    all_numbers = Dictionary.objects.filter(beginner__type="Number").all()
    number_video = VideoLecture.objects.filter(beginnervideo__type="Number").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
         "status": status,
        "all_numbers": all_numbers,
        "number_video": number_video,
        'base_template_name': base_template_name
    }
    return render(request, "learn/beginner/number.html", context)

def week(request):
    all_week = Dictionary.objects.filter(beginner__type="Week").all()
    week_video = VideoLecture.objects.filter(beginnervideo__type="Week").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
               "status": status,
        "all_week": all_week,
        'base_template_name': base_template_name,
        "week_video": week_video,

    }
    return render(request, "learn/beginner/week.html", context)

def days(request):
    all_day = Dictionary.objects.filter(beginner__type="Day").all()
    video_day = VideoLecture.objects.filter(beginnervideo__type="Animals").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
        "status": status,
        "all_day": all_day,
        'base_template_name': base_template_name,
        "video_day": video_day,

    }
    return render(request, "learn/beginner/days.html", context)

def body(request):
    all_body = Dictionary.objects.filter(beginner__type="Body").all()
    video_body = VideoLecture.objects.filter(beginnervideo__type="Body").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
         "status": status,
        "all_body": all_body,
        'base_template_name': base_template_name,
        "video_body": video_body,

    }
    return render(request, "learn/beginner/body.html", context)

def family(request):
    all_family = Dictionary.objects.filter(beginner__type="Family").all()
    video_family = VideoLecture.objects.filter(beginnervideo__type="Family").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
         "status": status,
        "all_family": all_family,
        'base_template_name': base_template_name,
        "video_family": video_family,

    }
    return render(request, "learn/beginner/family.html", context)

def maths(request):
    all_maths = Dictionary.objects.filter(beginner__type="Maths").all()
    video_maths = VideoLecture.objects.filter(beginnervideo__type="Maths").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
        "status": status,
        "all_maths": all_maths,
        'base_template_name': base_template_name,
        "video_maths": video_maths,

    }
    return render(request, "learn/beginner/maths.html", context)


# Intermidate sign language
def cloth(request):
    all_cloth = Dictionary.objects.filter(intermediate__type="Cloths").all()
    video_cloth = VideoLecture.objects.filter(caption="Cloths").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
         "status": status,
        "all_cloth": all_cloth,
        'base_template_name': base_template_name,
        "video_cloth": video_cloth,

    }
    return render(request, "learn/intermediate/cloth.html", context)

def food(request):
    all_food = Dictionary.objects.filter(intermediate__type="Food").all()
    video_food = VideoLecture.objects.filter(intermediatevideo__type="Food").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
         "status": status,
        "all_food": all_food,
        'base_template_name': base_template_name,
        "video_food": video_food,

    }
    return render(request, "learn/intermediate/food.html", context)



def animal(request):
    all_animals = Dictionary.objects.filter(intermediate__type="Animals").all()
    video_animals = VideoLecture.objects.filter(intermediatevideo__type="Animals").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
        "status": status,
        "all_animals": all_animals,
        'base_template_name': base_template_name,
        "video_animals": video_animals,

    }
    return render(request, "learn/intermediate/animals.html", context)
def nature(request):
    all_natures = Dictionary.objects.filter(intermediate__type="Natures").all()
    video_natures = VideoLecture.objects.filter(caption="Natures").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
         "status": status,
        "all_natures": all_natures,
        'base_template_name': base_template_name,
        "video_natures": video_natures,

    }
    return render(request, "learn/intermediate/natures.html", context)

def color(request):
    all_colors = Dictionary.objects.filter(intermediate__type="Color").all()
    video_colors = VideoLecture.objects.filter(caption="Color").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
        "status": status,
        "all_colors": all_colors,
        'base_template_name': base_template_name,
        "video_colors": video_colors,

    }
    return render(request, "learn/intermediate/color.html", context)

def fruit(request):
    all_fruits = Dictionary.objects.filter(intermediate__type="Fruit").all()
    video_fruits = VideoLecture.objects.filter(caption="Fruit").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
         "status": status,
        "all_fruits": all_fruits,
        'base_template_name': base_template_name,
        "video_fruits": video_fruits,

    }
    return render(request, "learn/intermediate/fruit.html", context)

def vegetable(request):
    all_vegetables = Dictionary.objects.filter(intermediate__type="Vegetable").all()
    video_vegetables = VideoLecture.objects.filter(caption="Vegetable").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
         "status": status,
        "all_vegetables": all_vegetables,
        'base_template_name': base_template_name,
        "video_vegetables": video_vegetables,

    }
    return render(request, "learn/intermediate/vegetable.html", context)

def names(request):
    all_names = Dictionary.objects.filter(intermediate__type="Names").all()
    video_names = VideoLecture.objects.filter(caption="Names").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
        "status": status,
        "all_names": all_names,
        'base_template_name': base_template_name,
        "video_names": video_names,

    }
    return render(request, "learn/intermediate/names.html", context)

# Advanced

def spritual(request):
    all_spirituals = Dictionary.objects.filter(advanced__type="Spiritual").all()
    video_spirituals = VideoLecture.objects.filter(caption="Spiritual").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
        "status": status,
        "all_spirituals": all_spirituals,
        'base_template_name': base_template_name,
        "video_spirituals": video_spirituals,

    }
    return render(request, "learn/advanced/spiritual.html", context)

def question(request):
    all_questions = Dictionary.objects.filter(advanced__type="Quetion").all()
    video_questions = VideoLecture.objects.filter(caption="Question").all()
    if request.user.user_type == '2':
       base_template_name = 'instructor/base_template.html'
       status = request.user.instructor.status
    elif request.user.user_type == '1':
        status = False
        base_template_name = 'admin/base_template.html'
    else:
       status = False
       base_template_name = 'learner/base_template.html'
    context = {
        "status": status,
        "all_questions": all_questions,
        'base_template_name': base_template_name,
        "video_questions": video_questions,

    }
    return render(request, "learn/advanced/question.html", context)
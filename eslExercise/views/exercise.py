from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
        user_type =  request.user.user_type

        if user_type == '2':
            status = request.user.instructor.status

            context = {
            'status': status
                }
            return render(request, "instructor/quiz_change_list.html", context)
            
        elif user_type == '3':
            return redirect('learners:quiz_list')
        else:
            return render(request, 'home.html')

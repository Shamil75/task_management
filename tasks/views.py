from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg

# Create your views here.

def manager_dashboard(request):
    return render(request, "dashboard/manager_dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")

def test(request):
    names = ["mahmud", "ahamed", "john", "Mr. X"]
    count = 0
    for name in names:
        count += 1
    context = {
        "names" : names,
        "age" :23,
        "count" : count
    }
    return render(request, 'test.html', context)


def create_task(request):
    # employees = Employee.objects.all()
    form = TaskModelForm() # For DET

    if request.method == "POST":
        form = TaskModelForm(request.POST,)
        if form.is_valid():
            """For Model Form Data"""
            form.save()
            return render(request, 'task_form.html', {"form": form, "message":"Task added successfully"})
        
    context = {"form": form}
    return render(request, "task_form.html", context)


# def view_task(request):
#     # retrieving all data from task model
#     # tasks = Task.objects.all()

#     # retrieve a specific task
#     # task_3 = Task.objects.get(id=3)

#     # Fetch the first task
#     # first_task = Task.objects.first()
#     # return render(request, "show_task.html", {"tasks": tasks, "task_3": task_3, "first_task": first_task})

#     # show the task that are completed
#     # task = Task.objects.filter(status="COMPLETED")
#     # return render(request, "show_task.html", {"task": task})

#     # show the task which due date is today
#     # task = Task.objects.filter(due_date=date.today())
#     # return render(request, "show_task.html", {"task": task})

#     """Show the task whose priority is not low"""
#     # task = TaskDetail.objects.exclude(priority="L")
#     # return render(request, "show_task.html", {"task": task})

#     """Show the task that contain any word and status pending"""
#     # task = Task.objects.filter(title__icontains="c", status="PENDING")

#     """Show the task which are pending or in progress"""
#     task = Task.objects.filter(Q(status="PENDING") | Q(status="IN_PROGRESS"))
#     return render(request, "show_task.html", {"task": task})

# def view_task(request):
#     # Select related queries (Foreign key, OneToOne)
#     # task = Task.objects.select_related('details').all()
#     # task = TaskDetail.objects.select_related('task').all()
#     # task = Task.objects.select_related('project').all()

#     """prefetch_related (reversse Foreign ke, manytomany)"""
#     # task = Project.objects.prefetch_related('projects').all()
#     task = Task.objects.prefetch_related('assigned_to').all()

#     return render(request, "show_task.html", {"task": task})

"""aggregations"""
def view_task(request):
    # task_count = Task.objects.aggregate(num_task=Count('id'))
    projects = Project.objects.annotate(num_task=Count('task')).order_by('num_task')
    return render(request, "show_task.html", {'projects': projects})


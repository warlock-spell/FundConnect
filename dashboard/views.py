from django.shortcuts import render, redirect
from .forms import ControllerForm
from .models import Controller


def edit_dashboard(request):
    controller = Controller.objects.first()

    if request.method == 'POST':
        form = ControllerForm(request.POST, instance=controller)
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('dashboard:dashboard-home')
    else:
        form = ControllerForm(instance=controller)

    context = {
        'form': form,
    }
    return render(request, 'dashboard/edit-dashboard.html', context)


def view_dashboard(request):
    controller = Controller.objects.first()  # Retrieve the first instance of Controller

    context = {
        'controller': controller
    }

    return render(request, 'dashboard/view-dashboard.html', context)

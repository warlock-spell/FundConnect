from django.shortcuts import render, redirect
from .forms import BranchForm
from .models import Branch


# Create your views here.

def home(request):
    return render(request, 'branch/home.html')


def create_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('branch:branch-home')
    else:
        form = BranchForm()

    return render(request, 'branch/create-branch.html', {'form': form})


def list_branch(request):
    branches = Branch.objects.all()
    context = {
        'branches': branches,
    }
    return render(request, 'branch/list-branches.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberForm, EditMemberForm, MemberSearchForm
from .models import Member


# Create your views here.

def home(request):
    return render(request, 'member/home.html')


def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member:member-home')
    else:
        form = MemberForm()

    return render(request, 'member/create-member.html', {'form': form})


def member_edit_search_view(request):
    form = MemberSearchForm(request.GET)
    members = Member.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        branch = form.cleaned_data.get('branch')

        if search_query:
            members = members.filter(name__icontains=search_query) | members.filter(id__icontains=search_query)

        if branch:
            members = members.filter(branch=branch)

    context = {
        'form': form,
        'members': members
    }

    return render(request, 'member/edit-member.html', context)


def edit_selected_member(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        form = EditMemberForm(request.POST, instance=member)

        if form.is_valid():
            member.active_user = True
            form.save()

            return redirect('member:member-edit')
    else:
        form = EditMemberForm(instance=member)

    return render(request, 'member/edit-member-pk.html', {
        'form': form,
        'title': 'Edit member',
    })


def remove_member(request):
    form = MemberSearchForm(request.GET)
    members = Member.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        branch = form.cleaned_data.get('branch')

        if search_query:
            members = members.filter(name__icontains=search_query) | members.filter(id__icontains=search_query)

        if branch:
            members = members.filter(branch=branch)

    context = {
        'form': form,
        'members': members
    }

    return render(request, 'member/remove-member.html', context)


def remove_selected_member(request, pk):
    member = get_object_or_404(Member, pk=pk)

    # delete on click
    member.active_user = False
    # uncomment to delete member data
    # member.delete()
    member.save()
    return redirect('member:member-remove')


def view_member(request):
    form = MemberSearchForm(request.GET)
    members = Member.objects.all()

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        branch = form.cleaned_data.get('branch')

        if search_query:
            members = members.filter(name__icontains=search_query) | members.filter(id__icontains=search_query)

        if branch:
            members = members.filter(branch=branch)

    context = {
        'form': form,
        'members': members
    }

    return render(request, 'member/list_member.html', context)


def view_selected_member(request, pk):
    member = get_object_or_404(Member, pk=pk)

    context = {
        'member': member,
    }

    return render(request, 'member/detail-member.html', context)


def terminated_members(request):
    form = MemberSearchForm(request.GET)
    members = Member.objects.all()
    members = members.filter(active_user=False)

    if form.is_valid():
        search_query = form.cleaned_data.get('search_query')
        branch = form.cleaned_data.get('branch')

        if search_query:
            members = members.filter(name__icontains=search_query) | members.filter(id__icontains=search_query)

        if branch:
            members = members.filter(branch=branch)

    context = {
        'form': form,
        'members': members
    }

    return render(request, 'member/terminated-members.html', context)

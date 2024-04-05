from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from .models import Group,Profile
from .forms import GroupForm, JoinGroupForm
from itertools import chain
from .models import GroupChatMessage


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            group.members.add(request.user)
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'create_group.html', {'form': form})

@login_required
def join_group_by_name(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    group.members.add(request.user)
    return redirect('group_chat', group_id=group_id)

def group_info(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    members = group.members.all()
    return render(request, 'group_info.html', {'group': group, 'members': members})

@login_required
def group_index(request):
    user_profile = Profile.objects.get(user=request.user)

    user_created_groups = Group.objects.filter(members=request.user)

    all_groups = Group.objects.all()
    group_info_list = []
    for group in all_groups:
        members = group.members.all()
        group_info_list.append({'group': group, 'members': members})

    combined_group_info = list(chain.from_iterable(group_info_list))

    return render(request, 'index.html', {
        'user_profile': user_profile,
        'user_created_groups': user_created_groups,
        'group_info_list': combined_group_info
    })

@login_required
def group_chat(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    group_messages = GroupChatMessage.objects.filter(group=group).order_by('timestamp')
    return render(request, 'group_chat.html', {'group': group, 'group_messages': group_messages})

@login_required
def send_message(request, group_id):
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            group = get_object_or_404(Group, id=group_id)
            GroupChatMessage.objects.create(user=request.user, group=group, message=message)
    return redirect('group_chat', group_id=group_id)


# def join_success(request, group_name):
#     return render(request, 'join_success.html', {'group_name': group_name})

@login_required
def joined_groups(request):
    joined_groups = Group.objects.filter(members=request.user)
    return render(request, 'joined_groups.html', {'joined_groups': joined_groups})





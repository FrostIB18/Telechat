from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    try:
        room = Room.objects.get(slug=slug)
        messages = Message.objects.filter(room=room)
        room_messages = Message.objects.filter(room=room)
        users = []
        for message in room_messages:
            if message.user not in users:
                users.append(message.user)
        number_of_users = len(users)
        return render(request, 'room/room.html', {'room': room, 'messages': messages, 'number_of_users':number_of_users})
    except ObjectDoesNotExist:
        room = Room.objects.create(name=slug, slug=slug)
        messages = Message.objects.filter(room=room)
        return render(request, 'room/room.html', {'room': room, 'messages': messages,})
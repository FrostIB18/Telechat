from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
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
        return render(request, 'room/room.html', {'room': room, 'messages': messages,})
    except ObjectDoesNotExist:
        room = Room.objects.create(name=slug, slug=slug)
        messages = Message.objects.filter(room=room)
        return render(request, 'room/room.html', {'room': room, 'messages': messages,})
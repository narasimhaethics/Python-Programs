from django.shortcuts import render
from django.http import JsonResponse
from .models import TodoItem

def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'index.html', {'todos': todos})

def add_todo(request):
    text = request.POST.get('text')
    if text:
        todo = TodoItem.objects.create(text=text)
        return JsonResponse({'id': todo.id, 'text': todo.text})
    else:
        return JsonResponse({'error': 'Text cannot be empty'}, status=400)

def toggle_todo(request):
    todo_id = request.POST.get('id')
    if todo_id:
        todo = TodoItem.objects.get(pk=todo_id)
        todo.completed = not todo.completed
        todo.save()
        return JsonResponse({'id': todo.id, 'completed': todo.completed})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_todo(request):
    todo_id = request.POST.get('id')
    if todo_id:
        todo = TodoItem.objects.get(pk=todo_id)
        todo.delete()
        return JsonResponse({'id': todo_id})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

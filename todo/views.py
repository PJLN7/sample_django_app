# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todoView(request):
  # return HttpResponse('Hello, this is the todoView!')
  todos = TodoItem.objects.all()

  return render(request, 'todo.html', {'todos': todos})

# to return a template (html), use render(request,
#     template, context)
# the 3rd parameter (context) is data we want to pass
#     into template
# in templates, we can insert python code into html with {% ...code %} and interpolate from context with {{ variable_name }}

# {% %} -> template tag for for-loops and conditions
# code blocks must be contained within 2 template tags
#   i.e., {% for... %}
#             ....code
#          {% endfor %}

def addTodo(request):
  new_item = TodoItem(content = request.POST['content'])
  new_item.save()
  return HttpResponseRedirect('/todoView/')

def deleteTodo(request, todo_id):
  item_to_delete = TodoItem.objects.get(id=todo_id)
  item_to_delete.delete()
  return HttpResponseRedirect('/todoView/')
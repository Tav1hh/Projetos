from django.shortcuts import render
from .models import Topic
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'index.html')

def topics(request):
    topics = Topic.objects.all()
    context = {'topics':topics}
    return render(request, 'topics.html', context)

def topico(request,topic_id):
    topico = Topic.objects.get(id=topic_id)
    entries = topico.entry_set.order_by('-date_added')
    context = {'topico':topico, 'entries':entries}
    return render(request, 'topico.html', context)


def new_topic(request):
    if request.method != 'POST':
        #nenhum dado submetido, cria um formulario em branco
        form = TopicForm()
    else:
        #Dados do POST submetidos; processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form':form}
    return render(request, 'new_topic.html', context)
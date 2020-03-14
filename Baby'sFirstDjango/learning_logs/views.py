from django.shortcuts import render

from .models import Topic

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')
    # The render() function passes 2 arguments: original request object and a template
    # it can use to build the page.

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    # The '-' in front of date_added indicates that the results will be sorted in 
    # reverse order, most recent entries first!
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

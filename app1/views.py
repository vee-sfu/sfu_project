from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def hello(request):
   return HttpResponse("Hello World!")


from django.shortcuts import render
 
def index1(request):

    return render(request, "index1.html")



from .models import Event    #+

#from django.views import generic    #+

#class EventListView(generic.ListView):    #+ вываливает всю таблицу
#    model = Event
#    paginate_by = 10
#    template_name = 'index.html'


from django.views import generic   #+

class EventListView(generic.ListView):    #+ вываливает всю таблицу
    model = Event
    paginate_by = 10
    template_name = 'index.html'   # если не указать, ищет event_list.html

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'event.html'   # если не указать, ищет event_detail.html















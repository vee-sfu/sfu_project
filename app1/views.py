from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def hello(request):
   return HttpResponse("Hello World!")


from django.shortcuts import render
 
def index1(request):

    return render(request, "index1.html")



from .models import Event    #+

from django.views import generic    #+

class EventListView(generic.ListView):    #+
    model = Event
    paginate_by = 10
    template_name = 'index.html'
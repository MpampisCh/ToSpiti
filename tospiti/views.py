from django.views import generic
from .models import Property, Agent, Prop_Picture, Prop_Facility, Facility

class HomepageView(generic.ListView):
    template_name = 'tospiti/homepage.html'
    context_object_name = 'all_properties'

    def get_queryset(self):
        return Property.objects.all().order_by('-created_date')[0:8]

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context["all_agents"] = Agent.objects.order_by('?')[:8]
        return context

class IndexView(generic.ListView):
    template_name = 'tospiti/index.html'
    context_object_name = 'all_properties'

    def get_queryset(self):
        return Property.objects.all().order_by('-created_date')

class PropertyDetailList(generic.ListView):
    template_name = 'tospiti/index.html'
    context_object_name = 'all_properties'

    def get_queryset(self):
        category=self.request.GET.get('category')
        return Property.objects.all().filter(prop_category__description__iexact=category)

class PropertyGenreList(generic.ListView):
    template_name = 'tospiti/index.html'
    context_object_name = 'all_properties'

    def get_queryset(self):
        genre=self.request.GET.get('genre')
        return Property.objects.all().filter(prop_genre__description__iexact=genre)



class DetailView(generic.DetailView):
    queryset = Property.objects.all()
    template_name = 'tospiti/detail.html'


class AgentsView(generic.ListView):
    model = Agent
    template_name = 'tospiti/agents.html'
    context_object_name = 'all_agents'

    def get_queryset(self):
        return Agent.objects.all()

class PropPicturesView(generic.ListView):
    model = Prop_Picture
    template_name = 'tospiti/proppictures.html'
    context_object_name = 'all_pictures'

    def get_queryset(self):
        return Prop_Picture.objects.all().order_by('property')


from django.urls import reverse_lazy
from django.views.generic import FormView
from tools.forms import ToolsForm
from tools.script import Script

scripts = Script()
# Create your views here.
class HomePageView(FormView):
    form_class = ToolsForm
    template_name = 'tools/home.html'
    success_url = reverse_lazy('home')
    scripts.run()
    
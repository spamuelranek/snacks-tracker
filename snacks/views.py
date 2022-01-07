from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from snacks.models import Snack

class AboutPageView(TemplateView):
  template_name = "about.html"

class SnackListView(ListView):
  template_name = "snack_list.html"
  model = Snack

class SnackDetailView(DetailView):
  template_name = "snack_detail.html"
  model = Snack
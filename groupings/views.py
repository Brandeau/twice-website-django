from django.views.generic.base import TemplateView
from groupings.models import Groupings
from django.shortcuts import render, get_object_or_404


class GroupingsListView(TemplateView):
    template_name = 'groupings/groupings_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        groupings = Groupings.objects.all()
        context['groupings'] = groupings

        return context
    
class GroupingsDetailsView(TemplateView):
    template_name = 'groupings/groupings_detail.html'

    def get(self, request, id, *args, **kwargs):
        grouping = get_object_or_404(Groupings, pk=id)
        context = {'grouping': grouping}
        return render(request, self.template_name, context)
        
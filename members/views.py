from django.views.generic.base import TemplateView
from members.models import Member
from django.shortcuts import render, get_object_or_404


class MembersListView(TemplateView):
    template_name = 'members/members_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        members = Member.objects.all()
        context['members'] = members

        return context
    
class MembersDetailsView(TemplateView):
    template_name = 'members/members_detail.html'

    def get(self, request, id, *args, **kwargs):
        member = get_object_or_404(Member, pk=id)
        context = {'member': member}
        return render(request, self.template_name, context)
        

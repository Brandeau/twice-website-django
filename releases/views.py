from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from releases.models import ReleaseGroup, Release
from tracks.models import Track
from django.shortcuts import render, get_object_or_404
class ReleasesListView(TemplateView):
    template_name = 'releases/releases_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        releases = ReleaseGroup.objects.all()
        context['releases'] = releases

        return context
    
class ReleasesDetailsView(TemplateView):
    template_name = 'releases/releases_detail.html'

    def get(self, request, id, *args, **kwargs):
        releaseGroup = get_object_or_404(ReleaseGroup, pk=id)

        releases = Release.objects.filter(release_group_id=releaseGroup)     

        releases_tracks = {}       

        for release in releases:
            releases_tracks[release] = {
                'name': release,
                'tracks': {Track.objects.filter(releases=release)}
            }
        context = {'releases': releases, 
                   'release_group': releaseGroup,
                   'release_tracks': releases_tracks    
                   }
        return render(request, self.template_name, context)
        

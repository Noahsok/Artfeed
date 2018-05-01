from datetime import timedelta, datetime

from django.conf import settings
from django.views.generic import CreateView

from drum.links.models import Link
from django.contrib.messages import info

from .forms import LinkForm


# Create your views here.
class LinkCreate(CreateView):
    """
    Link creation view - assigns the user to the new link, as well
    as setting Mezzanine's ``gen_description`` attribute to ``False``,
    so that we can provide our own descriptions.
    """

    form_class = LinkForm
    model = Link

    def form_valid(self, form):
        hours = getattr(settings, "ALLOWED_DUPLICATE_LINK_HOURS", None)
        if hours and form.instance.link:
            lookup = {
                "link": form.instance.link,
                "publish_date__gt": datetime.now() - timedelta(hours=hours),
            }
            try:
                link = Link.objects.get(**lookup)
            except Link.DoesNotExist:
                pass
            else:
                error(self.request, "Link exists")
                return redirect(link)
        form.instance.user = self.request.user
        form.instance.gen_description = False
        info(self.request, "Link created")
        return super(LinkCreate, self).form_valid(form)

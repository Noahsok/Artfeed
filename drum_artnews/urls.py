from __future__ import unicode_literals
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from drum.links.views import LinkList, LinkCreate, LinkDetail, CommentList, TagList

admin.autodiscover()


urlpatterns = [
    url("^admin/", include(admin.site.urls)),
    url("^link/create/$",
        login_required(LinkCreate.as_view()),
        name="link_create"),
    url("^", include("drum.links.urls")),
    url("^", include("mezzanine.urls")),
]

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"

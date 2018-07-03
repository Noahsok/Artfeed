from django.contrib import admin

from copy import deepcopy
from drum.links.admin import LinkAdmin
from drum.links.models import Link

links_fieldsets = list(deepcopy(LinkAdmin.fieldsets))
fields = list(links_fieldsets[0][1]["fields"])
fields.insert(-2,"content")#"text")
links_fieldsets[0][1]["fields"] = fields

class ArtNewsLinkAdmin(LinkAdmin):
    fieldsets = links_fieldsets

admin.site.unregister(Link)
admin.site.register(Link, ArtNewsLinkAdmin)

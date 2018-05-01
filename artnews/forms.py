from django.conf import settings
from django import forms
from django.forms.models import modelform_factory
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.forms import TinyMceWidget
from mezzanine.generic.forms import ThreadedCommentForm

from drum.links.models import Link


BaseLinkForm = modelform_factory(Link, fields=["title", "link", "text"], widgets={"text": TinyMceWidget})


class LinkForm(BaseLinkForm):

    def clean(self):
        link = self.cleaned_data.get("link", None)
        text = self.cleaned_data.get("text", None)
        if not link and not text:
            raise ValidationError("Either a link or description is required")
        return self.cleaned_data


class ArtnewsCommentForm(ThreadedCommentForm):
    name = forms.CharField(label=_("Name"), help_text=_("required"),
                           max_length=50, widget=forms.HiddenInput)
    email = forms.EmailField(label=_("Email"),
                             help_text=_("required (not published)"), widget=forms.HiddenInput)
    url = forms.URLField(label=_("Website"), help_text=_("optional"),
                         required=False,widget=forms.HiddenInput)


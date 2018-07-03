from __future__ import unicode_literals

from django.db import models

from drum.links.models import Link

from mezzanine.core.models import MetaData
from mezzanine.generic.fields import RatingField

# def description_from_content(self):
#     """
#     Override ``Displayable.description_from_content`` to load the
#     content type subclass for when ``save`` is called directly on a
#     ``Page`` instance, so that all fields defined on the subclass
#     are available for generating the description.
#     """
#     if self.__class__ == Link:
#         if self.content_model:
#             return self.get_content_model().description_from_content()
#     return super(Link, self).description_from_content()

def description_from_content(self):
      """
      Returns the first block or sentence of the first content-like
      field.
      """
      description = ""
      # Use the first RichTextField, or TextField if none found.
      for field_type in (RichTextField, models.TextField):
          if not description:
              for field in self._meta.fields:
                  if (isinstance(field, field_type) and
                          field.name != "description"):
                      description = getattr(self, field.name)
                      if description:
                          from mezzanine.core.templatetags.mezzanine_tags \
                                                  import richtext_filters
                          description = richtext_filters(description)
                          break
      # Fall back to the title if description couldn't be determined.
      if not description:
          description = str(self)
      # Strip everything after the first block or sentence.
      ends = ("</p>", "<br />", "<br/>", "<br>", "</ul>",
              "\n", ". ", "! ", "? ")
      for end in ends:
          pos = description.lower().find(end)
          if pos > -1:
              description = TagCloser(description[:pos]).html
              break
      else:
          description = truncatewords_html(description, 100)
      try:
          description = unicode(description)
      except NameError:
          pass  # Python 3.
      return description

Link.description_from_content = description_from_content


from django.test import TestCase

class GenericTests(TestCase):


    def test_voting(self):
        """
        Test that voting can be voted up or voted down.
        """

        votes = votes.objects.create(title="Voting", user=self.user, status=CONTENT_STATUS_PUBLISHED)

from django.urls import reverse
from django.test import TestCase


class IndexViewTestCase(TestCase):
    def test_index_view(self):
        result = self.client.get(reverse('home:index'))

        assert result.status_code == 200
        assert b'<title>Holiday Homes</title>' in result.content

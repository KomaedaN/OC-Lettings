from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class LettingsTest(TestCase):
    def setUp(self):ggg
        address = Address.objects.create(
            number=1234,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TST'
        )
        self.letting = Letting.objects.create(
            title='Test Letting',
            address=address
        )

    def test_lettings_index(self):
        result = self.client.get(reverse('lettings:lettings_index'))

        assert result.status_code == 200
        assert b'<title>Lettings</title>' in result.content

    def test_letting(self):
        result = self.client.get(reverse('lettings:letting', args=[1]))

        assert result.status_code == 200
        assert b'<title>Test Letting</title>' in result.content

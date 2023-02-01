from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfilesTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = Profile.objects.create(
            user=user,
            favorite_city='Test City'
        )

    def test_profiles_index(self):
        result = self.client.get(reverse('profiles:profiles_index'))

        assert result.status_code == 200
        assert b'<title>Profiles</title>' in result.content

    def test_profile(self):
        result = self.client.get(reverse('profiles:profile', args=['testuser']))

        assert result.status_code == 200
        assert b'<title>testuser</title>' in result.content

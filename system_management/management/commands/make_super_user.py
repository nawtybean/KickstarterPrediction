from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        password = make_password("root", salt=None, hasher='default')
        User = get_user_model()
        qs = User.objects.filter(email='shaun@deponte.co.za')
        if not qs.exists():
            User.objects.create(first_name='Shaun',
                                last_name='De Ponte',
                                email='shaun@deponte.co.za',
                                phone='12345678',
                                password=password,
                                user_type=4,
                                is_confirmed=True,
                                is_staff=True,
                                is_active=True,
                                is_external=False)
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from trade.models import Trader

class Command(BaseCommand):
    help = 'Load trader data'

    def handle(self, *args, **options):
        password = 'admin12345678'
        hashed_password = make_password(password)
        user = Trader.objects.create(username="admin1", password=hashed_password, is_admin=True, is_active=True, is_staff=True)
        user.save()
        for i in range(1, 11):
            user = Trader.objects.create(username=f"user{i}", password=hashed_password, is_user=True)
            user.save()

        self.stdout.write(self.style.SUCCESS('Trader data loaded successfully.'))

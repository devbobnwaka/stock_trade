import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from trade.models import Trader, Trade

class Command(BaseCommand):
    help = 'Load trade data'

    def handle(self, *args, **options):
        traders = Trader.objects.all()
        start_time   = datetime.now()

        for min in range(20): # Simulate for 20 minutes

            current_time = start_time + timedelta(minutes=min)
            for trader in traders:
                if trader.is_admin:
                    continue
                # Generate random profit/loss between -10 and 10
                profit_loss = round(random.uniform(-10, 10), 2) 

                trade_qs = Trade.objects.filter(trader=trader) 
                if not trade_qs:
                    # print('hi')
                    # Save the profit/loss data to the database or perform other operations
                    trade = Trade(trader=trader, timestamp=current_time, profit_loss=profit_loss)
                    trade.save()
                    # Update the trader's balance
                    trade.balance += profit_loss
                    trade.save() 
                else:
                    # print('hey')
                    trade = Trade(trader=trader, timestamp=current_time, profit_loss=profit_loss)
                    trade.save()

        self.stdout.write(self.style.SUCCESS('Trade data loaded successfully.'))

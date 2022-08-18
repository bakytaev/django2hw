python manage.py shell
from restaurant.models import *
u1 = User.objects.create(email='nikname21@gmail.com', password='defender42')
c1 = Client.objects.create(name='Азат Соколов', card_number='4147 5657 9878 9009', user=u1)


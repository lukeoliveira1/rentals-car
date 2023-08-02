import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

import random
import datetime
from django.utils import timezone
from django.core.files import File
from cars.models import Car 
from rents.models import Rent 
from users.models import Client

def create_clients(num_instances):
    for i in range(1, num_instances + 1):
        client, created = Client.objects.get_or_create(
            name=f"Cliente {i}",
            cpf=f"123.456.789-{i:02d}",
            address=f"Endereço {i}",
            email=f"cliente{i}@example.com",
            phone_number=f"(11) 9{1000 + i:04d}",
            cnh=f"AB00{i:02d}",
        )
        client.save()

# create_clients(10)  

def create_cars(num_instances):
    car_models = ["Modelo A", "Modelo B", "Modelo C", "Modelo D", "Modelo E"]
    car_manufacturers = ["Fabricante X", "Fabricante Y", "Fabricante Z"]
    car_colors = ["Vermelho", "Azul", "Preto", "Branco", "Verde"]
    fuel_types = ["Gasolina", "Álcool", "Diesel", "Flex"]

    for _ in range(num_instances):
        car = Car.objects.create(
            model=random.choice(car_models),
            manufacter=random.choice(car_manufacturers),
            color=random.choice(car_colors),
            year=str(random.randint(2000, timezone.now().year)),
            motor="Motor XYZ",
            fuel_type=random.choice(fuel_types),
            license_plate=f"ABC{random.randint(1000, 9999)}",
            photo=File(open("media/carros/hilux.jpeg", "rb"))  
        )
        car.save()

# create_cars(10)  

def create_rents(num_instances):
    for _ in range(num_instances):
        pickup_date = timezone.now() + datetime.timedelta(days=random.randint(1, 30))
        delivery_date = pickup_date + datetime.timedelta(days=random.randint(1, 10))
        value = round(random.uniform(100, 1000), 2)

        client = Client.objects.order_by("?").first()  # randomly select an existing customer
        car = Car.objects.order_by("?").first()  # randomly select an existing car

        rent = Rent.objects.create(
            pickup_date=pickup_date,
            delivery_date=delivery_date,
            value=value,
            client=client,
            car=car
        )
        rent.save()

# create_rents(5)  

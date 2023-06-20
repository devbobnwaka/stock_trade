import json
from pathlib import Path
# from django.contrib.auth.hashers import make_password


def generate_seed_data():
    admin =[{
        "model": "trade.Trader",
        "fields": {
          "username": "admin1",
        #   "password": make_password("admin12345678"),
          "is_admin": True,
          "is_active": True,
          "is_staff": True
        }
    }]

    user = []

    for i in range(1, 11):
        user.append({
            "model": "trade.Trader",
            "fields": {
            "username": f"user{i}",
            # "password": make_password("admin12345678"),
            "is_user": True
            }
        })

    seed_data = admin + user

    return json.dumps(seed_data, indent=4)

def write_seed_data_to_fixture():
    seed_data = generate_seed_data()
    file_path = Path(__file__).resolve().parent.parent / "fixtures/seed_data.json"
    with open(file_path, 'w') as file:
        file.write(seed_data)

# Call the function to generate and write the seed data to the fixture file
write_seed_data_to_fixture()



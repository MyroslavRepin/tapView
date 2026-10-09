import json
import secrets

name_count = 0


def generate_db(length):
    db_data = []
    name = "Bob"

    for nfc in range(length):
        if length > 5:
            name = "Michael"

        new_nfc = {
            "uid": secrets.token_hex(3),
            "name": name,
        }
        db_data.append(new_nfc)

    with open("db.json", "w") as file:
        json.dump(db_data, file, indent=4)

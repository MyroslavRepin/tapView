import json
import logging

from fastapi import APIRouter
from fastapi.responses import RedirectResponse, Response

from backend.services.create_db import generate_db

router = APIRouter()

with open("db.json", "r") as file:
    nfc_tags = json.load(file)


@router.get("/s/{nfc_uid}")
def nfc_redirect(nfc_uid: str, response: Response):
    print("api triggered")
    for nfc in nfc_tags:
        uid = str(nfc["uid"])
        print(nfc_tags)

        if nfc_uid != uid:
            logging.info(f"UID: {nfc_uid} is out of bound")
            response.status_code = 404
            return response
        logging.info(f"UID: {nfc_uid} were found - Redirecting")
        break
    return {
        "msg": "im too lazy to make actual redirect",
    }

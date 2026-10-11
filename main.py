from fastapi import FastAPI

from backend.api.nfc_redirect import router as nfc_redirect_router
from backend.api.nfc_tags import router as nfc_tags_router

app = FastAPI()

app.include_router(nfc_redirect_router)
app.include_router(nfc_tags_router)


@app.get("/")
def main():
    return {"msg": "welcome to the best code ever"}

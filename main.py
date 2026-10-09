from fastapi import FastAPI

from backend.api.nfc_redirect import router as nfc_redirect_router

app = FastAPI()

app.include_router(nfc_redirect_router)


@app.get("/")
def main():
    return {"msg": "welcome to the best code ever"}

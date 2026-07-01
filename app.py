from fastapi import FastAPI
import logging
import requests

logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

N8N_WEBHOOK = "https://n8n.sketch2garment.shop/webhook-test/production-crash"

@app.get("/users")
def users():

    try:

        age = -5

        if age < 0:
            raise ValueError("Invalid age supplied")

        return {"age": age}

    except Exception as e:

        logging.exception("Application warning")

        requests.post(
            N8N_WEBHOOK,
            json={
                "error": str(e),
                "log_file": "error.log",
                "service": "user-api"
            }
        )

        return {
            "status": "warning",
            "message": str(e)
        }





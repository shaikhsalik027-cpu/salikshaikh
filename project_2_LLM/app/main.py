from fastapi import FastAPI
from app.whatsapp_webhook import router as whatsapp_router

app = FastAPI(title="WhatsApp LLM Stock Agent")

app.include_router(
    whatsapp_router,
    prefix="/whatsapp",
    tags=["WhatsApp"]
)

@app.get("/")
def health_check():
    return {"status": "ok"}
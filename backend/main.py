from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.correction import router as correction_router
from routes.payment import router as payment_router

app = FastAPI(title="Redify API", version="0.1.0")

# Libera acesso do frontend (ajustar origem quando for pra produção)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(correction_router)
app.include_router(payment_router)


@app.get("/")
def health_check():
    return {"status": "ok", "service": "Redify API"}
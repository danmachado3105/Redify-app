from fastapi import APIRouter
from services.payment_service import criar_preferencia_pagamento

router = APIRouter()


@router.post("/criar-pagamento")
def criar_pagamento():
    preferencia = criar_preferencia_pagamento()
    return {"init_point": preferencia["sandbox_init_point"]}
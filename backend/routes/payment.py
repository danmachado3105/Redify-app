from fastapi import APIRouter
from services.payment_service import criar_preferencia_pagamento

router = APIRouter()


@router.post("/criar-pagamento")
def criar_pagamento():
    preferencia = criar_preferencia_pagamento()
    link = preferencia.get("sandbox_init_point") or preferencia.get("init_point")
    return {"init_point": link}
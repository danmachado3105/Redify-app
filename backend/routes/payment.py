from fastapi import APIRouter
from services.payment_service import criar_preferencia_pagamento, verificar_pagamento

router = APIRouter()


@router.post("/criar-pagamento")
def criar_pagamento():
    preferencia = criar_preferencia_pagamento()
    link = preferencia.get("sandbox_init_point") or preferencia.get("init_point")
    return {"init_point": link, "preference_id": preferencia.get("id")}


@router.get("/status-pagamento/{payment_id}")
def status_pagamento(payment_id: str):
    status = verificar_pagamento(payment_id)
    return {"aprovado": status == "approved", "status": status}
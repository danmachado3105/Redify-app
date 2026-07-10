from fastapi import APIRouter, HTTPException
from models.schemas import RedacaoRequest, RedacaoResponse
from services.llm_service import corrigir_redacao

router = APIRouter()


@router.post("/corrigir", response_model=RedacaoResponse)
def corrigir(request: RedacaoRequest):
    try:
        return corrigir_redacao(request.texto)
    except Exception as erro:
        raise HTTPException(status_code=500, detail=f"Erro ao corrigir redação: {erro}")
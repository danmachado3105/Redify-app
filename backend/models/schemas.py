from pydantic import BaseModel, Field


class RedacaoRequest(BaseModel):
    texto: str = Field(..., min_length=50, description="Texto da redação a ser corrigida")


class Competencia(BaseModel):
    numero: int
    titulo: str
    nota: int
    comentario: str
    trecho_citado: str | None = None
    sugestao_reescrita: str | None = None


class RedacaoResponse(BaseModel):
    nota_total: int
    competencias: list[Competencia]
    pontos_fortes: list[str]
    pontos_melhoria: list[str]
    recado_professor: str
from pydantic import BaseModel, Field


class RedacaoRequest(BaseModel):
    """O que o frontend envia pra corrigir a redação."""
    texto: str = Field(..., min_length=50, description="Texto da redação a ser corrigida")


class Competencia(BaseModel):
    """Nota e comentário de uma das 5 competências do ENEM."""
    numero: int
    titulo: str
    nota: int  # 0 a 200 (padrão ENEM)
    comentario: str


class RedacaoResponse(BaseModel):
    """O que o backend devolve pro frontend."""
    nota_total: int  # soma das 5 competências, 0 a 1000
    competencias: list[Competencia]
    pontos_fortes: list[str]
    pontos_melhoria: list[str]
import json
import anthropic
from config import ANTHROPIC_API_KEY, MODEL_NAME, USE_MOCK
from models.schemas import RedacaoResponse


PROMPT_SISTEMA = """Voce e um corretor especializado em redacoes do ENEM.
Avalie o texto enviado seguindo rigorosamente as 5 competencias oficiais do ENEM:

1. Dominio da norma culta da lingua escrita
2. Compreensao da proposta e aplicacao de conceitos das varias areas de conhecimento
3. Capacidade de organizar e interpretar informacoes, fatos e argumentos
4. Dominio dos mecanismos linguisticos para argumentacao
5. Proposta de intervencao que respeite os direitos humanos

Cada competencia vale de 0 a 200 pontos (multiplos de 40: 0, 40, 80, 120, 160, 200).
A nota total e a soma das 5 competencias (0 a 1000).

Responda APENAS com um JSON valido, sem nenhum texto antes ou depois, no seguinte formato exato:

{
  "nota_total": 0,
  "competencias": [
    {"numero": 1, "titulo": "Dominio da norma culta", "nota": 0, "comentario": "..."},
    {"numero": 2, "titulo": "Compreensao da proposta", "nota": 0, "comentario": "..."},
    {"numero": 3, "titulo": "Organizacao de argumentos", "nota": 0, "comentario": "..."},
    {"numero": 4, "titulo": "Mecanismos linguisticos", "nota": 0, "comentario": "..."},
    {"numero": 5, "titulo": "Proposta de intervencao", "nota": 0, "comentario": "..."}
  ],
  "pontos_fortes": ["...", "..."],
  "pontos_melhoria": ["...", "..."]
}
"""


def _resposta_mock() -> RedacaoResponse:
    return RedacaoResponse(
        nota_total=760,
        competencias=[
            {"numero": 1, "titulo": "Dominio da norma culta", "nota": 160,
             "comentario": "Bom dominio da norma padrao, com poucos deslizes pontuais de concordancia."},
            {"numero": 2, "titulo": "Compreensao da proposta", "nota": 160,
             "comentario": "Compreendeu bem o tema, mas poderia aprofundar mais o repertorio sociocultural."},
            {"numero": 3, "titulo": "Organizacao de argumentos", "nota": 160,
             "comentario": "Argumentacao organizada, com progressao textual clara entre os paragrafos."},
            {"numero": 4, "titulo": "Mecanismos linguisticos", "nota": 120,
             "comentario": "Uso de conectivos poderia ser mais variado para melhorar a coesao."},
            {"numero": 5, "titulo": "Proposta de intervencao", "nota": 160,
             "comentario": "Proposta de intervencao presente, mas faltou detalhar o agente responsavel."},
        ],
        pontos_fortes=[
            "Boa estrutura dissertativo-argumentativa",
            "Repertorio sociocultural pertinente ao tema",
        ],
        pontos_melhoria=[
            "Variar mais os conectivos entre paragrafos",
            "Detalhar melhor a proposta de intervencao (agente, acao, meio, finalidade, detalhamento)",
        ],
    )


def _chamar_api_real(texto_redacao: str) -> RedacaoResponse:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    resposta = client.messages.create(
        model=MODEL_NAME,
        max_tokens=1500,
        system=PROMPT_SISTEMA,
        messages=[
            {"role": "user", "content": f"Corrija esta redacao:\n\n{texto_redacao}"}
        ],
    )

    texto_resposta = resposta.content[0].text
    dados = json.loads(texto_resposta)
    return RedacaoResponse(**dados)


def corrigir_redacao(texto_redacao: str) -> RedacaoResponse:
    if USE_MOCK:
        return _resposta_mock()
    return _chamar_api_real(texto_redacao)
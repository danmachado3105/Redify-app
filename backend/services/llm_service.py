import json
import anthropic
from config import ANTHROPIC_API_KEY, MODEL_NAME, USE_MOCK
from models.schemas import RedacaoResponse


PROMPT_SISTEMA = """Voce e um corretor especializado em redacoes do ENEM, atualizado com os
criterios reais de correcao aplicados a partir de 2025. Avalie o texto seguindo
rigorosamente as 5 competencias oficiais, com estas regras especificas:

COMPETENCIA 1 - Dominio da norma culta da lingua escrita
Avalie ortografia, concordancia, regencia, pontuacao e registro formal.

COMPETENCIA 2 - Compreensao da proposta e aplicacao de conceitos de varias areas
Avalie se o repertorio sociocultural usado e PERTINENTE e bem CONTEXTUALIZADO ao
argumento, nao apenas citado de forma solta ("repertorio de bolso"). Repertorio
generico, decorado ou desconectado do argumento deve ser penalizado tanto aqui
quanto na Competencia 3 (a mesma falha impacta as duas notas).

COMPETENCIA 3 - Capacidade de organizar e interpretar informacoes, fatos e argumentos
Avalie a autoria e o aprofundamento da argumentacao. Repertorio usado apenas como
"enfeite", sem articulacao real com a tese, penaliza esta competencia junto com a 2,
pelo mesmo motivo (nao trate como duas falhas independentes, mas como uma unica
fragilidade que rebaixa ambas as notas).

COMPETENCIA 4 - Dominio dos mecanismos linguisticos para argumentacao (coesao)
NAO avalie por contagem de conectivos. Avalie QUALITATIVAMENTE o uso de recursos
coesivos, classificando o repertorio coesivo do texto como: "pontual" (uso minimo,
repetitivo), "regular" (uso adequado mas sem variedade), "constante" (bom uso,
variado) ou "expressivo" (uso rico, preciso, que articula bem os argumentos).
Textos com conectivos repetidos ou usados de forma mecanica devem ficar no maximo
em "regular", mesmo que a quantidade de conectivos pareca suficiente.

COMPETENCIA 5 - Proposta de intervencao que respeite os direitos humanos
Exija os 5 elementos: agente, acao, meio/modo, finalidade e detalhamento.
IMPORTANTE: se o elemento "ACAO" estiver ausente ou muito vago, aplique um desconto
de 120 pontos na nota desta competencia especificamente (nao 40 pontos como em
versoes antigas do criterio) - a acao e o elemento mais penalizado quando ausente.
A falta dos demais elementos (agente, meio, finalidade, detalhamento) segue o
desconto padrao de 40 pontos cada.

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
             "comentario": "Repertorio pertinente ao tema, bem articulado com o argumento central."},
            {"numero": 3, "titulo": "Organizacao de argumentos", "nota": 160,
             "comentario": "Argumentacao organizada, com progressao textual clara entre os paragrafos."},
            {"numero": 4, "titulo": "Mecanismos linguisticos", "nota": 120,
             "comentario": "Uso regular de conectivos, mas com pouca variedade - repertorio coesivo pontual em trechos."},
            {"numero": 5, "titulo": "Proposta de intervencao", "nota": 160,
             "comentario": "Proposta completa, mas faltou detalhar melhor o elemento de acao especifica."},
        ],
        pontos_fortes=[
            "Boa estrutura dissertativo-argumentativa",
            "Repertorio sociocultural bem contextualizado ao tema",
        ],
        pontos_melhoria=[
            "Variar mais os conectivos para elevar o repertorio coesivo de regular para constante",
            "Detalhar melhor a acao da proposta de intervencao (elemento mais penalizado quando vago)",
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

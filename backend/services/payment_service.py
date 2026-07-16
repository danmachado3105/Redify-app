import mercadopago
from config import MP_ACCESS_TOKEN

print("TOKEN CARREGADO:", repr(MP_ACCESS_TOKEN))

MP_MOCK = False  # documentação aprovada, testando com sandbox real

sdk = mercadopago.SDK(MP_ACCESS_TOKEN)


PLANOS = {
    "avulso": {"title": "Correção avulsa - Redify", "price": 2.90},
    "pacote5": {"title": "Pacote 5 correções - Redify", "price": 12.90},
    "pacote15": {"title": "Pacote 15 correções - Redify", "price": 29.90},
}


def criar_preferencia_pagamento(plano: str = "avulso"):
    dados_plano = PLANOS.get(plano, PLANOS["avulso"])

    preference_data = {
        "items": [
            {
                "title": dados_plano["title"],
                "quantity": 1,
                "unit_price": dados_plano["price"],
                "currency_id": "BRL",
            }
        ],
        "back_urls": {
            "success": "http://127.0.0.1:5500/frontend/pagamento-sucesso.html",
            "failure": "http://127.0.0.1:5500/frontend/pagamento-erro.html",
            "pending": "http://127.0.0.1:5500/frontend/pagamento-erro.html",
        },
    }

    resultado = sdk.preference().create(preference_data)
    return resultado["response"]
    

def verificar_pagamento(payment_id: str) -> str:
    """Consulta o status real de um pagamento direto na API do Mercado Pago."""
    if MP_MOCK:
        return "approved"  # em modo mock, sempre aprova

    resultado = sdk.payment().get(payment_id)
    return resultado["response"]["status"]
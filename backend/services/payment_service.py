import mercadopago
from config import MP_ACCESS_TOKEN

print("TOKEN CARREGADO:", repr(MP_ACCESS_TOKEN))

MP_MOCK = False  # documentação aprovada, testando com sandbox real

sdk = mercadopago.SDK(MP_ACCESS_TOKEN)


def criar_preferencia_pagamento():
    preference_data = {
        "items": [
            {
                "title": "Correção completa - Redify",
                "quantity": 1,
                "unit_price": 2.90,
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
    print("RESPOSTA COMPLETA DO MERCADO PAGO:", resultado)
    return resultado["response"]
    

def verificar_pagamento(payment_id: str) -> str:
    """Consulta o status real de um pagamento direto na API do Mercado Pago."""
    if MP_MOCK:
        return "approved"  # em modo mock, sempre aprova

    resultado = sdk.payment().get(payment_id)
    return resultado["response"]["status"]
import mercadopago
from config import MP_ACCESS_TOKEN

MP_MOCK = True  # muda pra False quando a conta for aprovada

sdk = mercadopago.SDK(MP_ACCESS_TOKEN)


def criar_preferencia_pagamento():
    if MP_MOCK:
        # Simula o link de pagamento, sem chamar a API de verdade
        return {"init_point": "http://127.0.0.1:5500/frontend/pagamento-sucesso.html"}

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
        "auto_return": "approved",
    }

    resultado = sdk.preference().create(preference_data)
    return resultado["response"]
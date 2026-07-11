import mercadopago
from config import MP_ACCESS_TOKEN

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
            "success": "http://127.0.0.1:5500/pagamento-sucesso.html",
            "failure": "http://127.0.0.1:5500/pagamento-erro.html",
            "pending": "http://127.0.0.1:5500/pagamento-erro.html",
        },
        "auto_return": "approved",
    }

    resultado = sdk.preference().create(preference_data)
    return resultado["response"]
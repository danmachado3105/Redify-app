import os
from dotenv import load_dotenv

load_dotenv()

# Chave da API da Anthropic (fica vazia até você configurar o .env)
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# Modelo usado para a correção (Haiku é o mais barato, ideal pra esse produto)
MODEL_NAME = os.getenv("MODEL_NAME", "claude-haiku-4-5-20251001")

# Modo mock: quando True, não chama a API de verdade (não gasta nada)
# Muda pra "false" no .env quando você tiver créditos configurados
USE_MOCK = os.getenv("USE_MOCK", "true").lower() == "true"
# Redify

Correção de redação com Inteligência Artificial, focada em estudantes de ENEM e vestibular.

Sobe sua redação, recebe uma correção completa pelas 5 competências do ENEM em minutos — nota estimada, pontos fortes, pontos de melhoria e sugestões práticas.

## Status do projeto

🚧 Em desenvolvimento — MVP em construção.

## O problema

Corrigir redação com qualidade exige tempo de um professor especializado, e nem todo estudante tem acesso fácil a isso. O Redify usa IA para dar um feedback rápido, estruturado e acessível, ajudando o estudante a identificar pontos de melhoria antes da prova.

## Como funciona

1. O usuário envia o texto da redação (colado ou via arquivo)
2. A IA analisa o texto seguindo os critérios oficiais das 5 competências do ENEM
3. O usuário recebe nota estimada por competência + feedback detalhado

## Stack

- **Backend:** Python (FastAPI)
- **IA:** API de LLM (correção via prompt especializado nas competências do ENEM)
- **Frontend:** React
- **Pagamentos:** Mercado Pago / Stripe
- **Extração de arquivos:** PyMuPDF

## Rodando o projeto localmente

> Instruções serão atualizadas conforme o backend e frontend forem implementados.

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## Roadmap

- [ ] Upload de redação (texto/arquivo)
- [ ] Correção via IA com nota por competência
- [ ] Integração de pagamento
- [ ] Envio de resultado por e-mail
- [ ] Histórico de correções (fase 2)
- [ ] Assinatura mensal (fase 2)

## Licença

Este projeto é privado e de uso comercial. Todos os direitos reservados.
# Redify

Correção de redação com Inteligência Artificial, calibrada nas mudanças reportadas na correção do ENEM 2025 — feita para estudantes de ENEM e vestibular.

> 🚧 **Status: MVP funcional, projeto em pausa.** O produto está completo do frontend ao backend, com pagamento integrado e testado em ambiente sandbox. Deploy (domínio + hospedagem) ainda pendente — atualmente roda em ambiente local.

## O problema

Corrigir redação com qualidade exige tempo de um professor especializado, e nem todo estudante tem acesso fácil a isso. O Redify usa IA para dar um feedback rápido, estruturado e acessível — citando trechos reais da redação do aluno e sugerindo reescritas, como um professor apontaria em uma correção individual.

## O que o produto faz

- Recebe o texto de uma redação e avalia pelas 5 competências oficiais do ENEM
- Gera nota estimada por competência, com comentário, trecho citado da redação e sugestão de reescrita
- Calibra a correção com mudanças práticas reportadas na correção do ENEM 2025 (ex: penalização de 120 pontos por ausência do elemento "ação" na Competência 5; avaliação qualitativa da coesão na Competência 4; penalização simultânea das Competências 2 e 3 por repertório genérico)
- Paywall com nota geral gratuita e feedback detalhado desbloqueado via pagamento
- Checkout integrado com Mercado Pago (testado em ambiente sandbox)
- Landing page com explicação de cada competência (páginas individuais), planos, FAQ e política de privacidade

## Stack

**Backend**
- Python + FastAPI
- Anthropic API (Claude Haiku) para a correção
- Mercado Pago SDK para pagamentos
- Pydantic para validação de dados

**Frontend**
- HTML, CSS e JavaScript puro (sem framework, por decisão de simplicidade e velocidade de desenvolvimento)
- Identidade visual própria (tema escuro, verde como cor de marca)

## Estrutura do projeto

```
redify/
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── models/schemas.py
│   ├── services/
│   │   ├── llm_service.py       # correção via IA (com modo mock para desenvolvimento)
│   │   └── payment_service.py   # integração Mercado Pago
│   └── routes/
│       ├── correction.py
│       └── payment.py
└── frontend/
    ├── index.html                # landing page
    ├── app.html                  # tela de correção
    ├── competencia.html          # página individual por competência
    ├── privacidade.html
    ├── pagamento-sucesso.html
    ├── style.css
    └── main.js
```

## Rodando localmente

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env      # preencha suas próprias chaves de API
uvicorn main:app --reload

# Frontend
# Abra frontend/app.html com uma extensão tipo Live Server
```

O backend roda em modo mock por padrão (`USE_MOCK=true` no `.env`), sem exigir créditos de API para testar o fluxo completo.

## Decisões de projeto

- **Frontend sem framework**: para um MVP solo com prazo curto, HTML/CSS/JS puro permitiu iterar mais rápido do que configurar um projeto React completo, sem abrir mão de um resultado visual cuidado.
- **Modo mock no backend**: toda a lógica de correção e pagamento foi construída com uma camada de simulação, permitindo testar o produto de ponta a ponta sem gastar créditos de API durante o desenvolvimento.
- **Verificação de pagamento via backend**: o desbloqueio do feedback completo depende de uma confirmação real do status de pagamento consultada diretamente na API do Mercado Pago — o frontend nunca decide sozinho se o conteúdo deve ser liberado.

## Roadmap (pendente)

- [ ] Histórico do aluno (banco de dados + lógica de créditos por pacote)
- [ ] Desafios de redação com temas prováveis para o ENEM 2026
- [ ] Deploy em produção (domínio próprio + hospedagem)
- [ ] Credenciais de produção do Mercado Pago (atualmente em sandbox)

## Contexto

Projeto solo, desenvolvido com orçamento próprio limitado (bootstrap), pensado tanto como produto comercial quanto como peça de portfólio técnico.

## Licença

Projeto privado e de uso comercial. Todos os direitos reservados.
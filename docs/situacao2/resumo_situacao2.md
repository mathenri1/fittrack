# Situação de Aprendizagem 2 – FitTrack

## Objetivo
Implementar o backend e frontend integrados de um sistema para registro de treinos e refeições, utilizando Flask (Python) e HTML/CSS/JS.

## Componentes concluídos
- API RESTful em Flask com endpoints:
  - `/api/treinos/` – CRUD completo
  - `/api/refeicoes/` – CRUD completo
  - `/api/health` – teste de integridade
- Banco de dados SQLite (`instance/fittrack.sqlite3`)
- Frontend com:
  - Páginas `treino.html` e `refeicao.html` para cadastro e listagem
  - Exclusão direta com confirmação
  - Dashboard (`index.html`) com métricas semanais
- Integração via `fetch()` com retorno JSON.
- Estilo e responsivo (`style.css`).

## Tecnologias
- **Backend:** Python 3.12 + Flask
- **Banco:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript Vanilla
- **Ambiente:** Visual Studio Code + PowerShell

## Estrutura
fittrack/
├── backend/
│ ├── app.py
│ ├── models.py
│ ├── routes/
│ │ ├── treino_routes.py
│ │ └── refeicao_routes.py
│ └── instance/fittrack.sqlite3
├── frontend/
│ ├── index.html
│ ├── treino.html
│ ├── refeicao.html
│ ├── script.js
│ └── style.css
└── docs/
├── dados/schema.sql
└── situacao2/
└── resumo_situacao2.md

## Resultado
O sistema está totalmente funcional, com comunicação entre frontend e backend, e integração com banco SQLite.  

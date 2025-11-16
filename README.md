FitTrack – Controle de Treinos e Refeições
Objetivo do Projeto

O FitTrack é um sistema simples desenvolvido para ajudar pessoas que treinam a registrar seus treinos e refeições de forma prática.
A ideia é permitir que o usuário acompanhe sua evolução semanal (em volume de treino e ingestão de proteína) e tenha uma visão clara de como está sua rotina, tudo em uma interface direta e fácil de usar.

Propósito

Muitas pessoas que treinam acabam se perdendo no registro diário das atividades físicas e alimentação.
O FitTrack vem para resolver isso com uma interface leve, rápida e funcional e sem burocracia.

Funcionalidades (MVP)

O projeto vai incluir, na primeira versão (MVP):

Autenticação simples (cadastro e login do usuário)

CRUD de treinos (cadastrar, editar, excluir e visualizar treinos)

CRUD de refeições (cadastrar, editar, excluir e visualizar refeições)

Dashboard semanal (exibir treinos realizados, volume total e proteína ingerida)

Filtros e buscas (por período e nome de exercício)

Mensagens claras de erro e sucesso para orientar o usuário

Stack Utilizada

Front-end: HTML, CSS e JavaScript (com Bootstrap ou Tailwind)
Back-end: Python (Flask, padrão MVC)
Banco de Dados: SQLite (MVP) e PostgreSQL (versão final)
Testes: Pytest (back-end) e Cypress (opcional, front-end)

Como o Sistema Vai Funcionar (resumo)

O usuário Registra seus treinos (exercício, séries, repetições, carga, etc).

Registra suas refeições (itens, porções e quantidade de proteína).

Visualiza um resumo semanal com estatísticas simples.

Pode editar, excluir ou filtrar seus registros por data.

Estrutura do Projeto
docs/
  situacao1/     → Planejamento, escopo e modelagem
  situacao2/     → Codificação e testes
  situacao3/     → Validação com colegas e melhorias
  dados/         → Modelagem e dicionário de dados

frontend/        → Código do front-end
backend/         → Código do back-end (Flask)
tests/           → Testes automatizados

Backlog de Funcionalidades
ID	    História de Usuário	        Descrição
HU01	Registrar Treino	Como usuário, quero registrar um treino rapidamente.
HU02	Editar/Excluir Treino	Como usuário, quero editar ou excluir um treino.
HU03	Registrar Refeição	Como usuário, quero registrar uma refeição e acompanhar proteína diária.
HU04	Dashboard	Como usuário, quero ver um resumo dos meus treinos e alimentação.


Como Rodar o Projeto (rascunho)

Criar o ambiente virtual e instalar as dependências:
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

Executar o back-end (Flask):
python app.py

Abrir o index.html no navegador (ou servir com um servidor local).
O banco será criado automaticamente ao rodar o back-end.

Licença
Este projeto é de uso acadêmico, desenvolvido para o Projeto Integrador Transdisciplinar de Engenharia de Software II.
Licenciado sob MIT License.
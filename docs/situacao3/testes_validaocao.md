# Testes de Verificação e Validação – FitTrack

## Objetivo
Verificar se o sistema FitTrack está funcionando corretamente e se atende o que foi planejado nas situações anteriores.

## O que foi testado
Foram realizados testes em todas as funções principais:
- Cadastro, edição e exclusão de treinos
- Cadastro, edição e exclusão de refeições
- Atualização automática do dashboard
- Comunicação entre front-end e back-end via Flask API

## Ambiente de Teste
- Sistema operacional: Windows 11
- Linguagem: Python 3.12 (Flask)
- Banco de dados: SQLite
- Navegador usado: Microsoft Edge
- Testes de API feitos no PowerShell com Invoke-RestMethod

## Casos de Teste

| Caso | O que foi testado | Entrada | Resultado Esperado | Obtido | Status |
|------|-------------------|----------|--------------------|---------|--------|
| CT01 | Criar treino | observações="Peito", esforço=7 | Treino salvo e listado | OK |
| CT02 | Editar treino | esforço=8 | Atualização refletida | OK |
| CT03 | Excluir treino | id=1 | Treino removido | OK |
| CT04 | Criar refeição | descrição="Frango", proteína=40 | Salva e listada | OK |
| CT05 | Editar refeição | proteína=45 | Atualizado | OK |
| CT06 | Excluir refeição | id=1 | Removida | OK |
| CT07 | Dashboard | Acesso ao index.html | Dados atualizados | OK |
| CT08 | API health | /api/health | status “ok” | OK |

## Conclusão
Todos os testes funcionaram corretamente.  
O sistema está validado e pronto para ser apresentado.

# FitTrack – Escopo do Projeto

**Disciplina:** Projeto Integrador Transdisciplinar de Engenharia de Software II  
**Aluno:** Matheus Henrique Maciel  

---

## 1. Introdução

O **FitTrack** é um sistema web simples voltado para pessoas que treinam e desejam registrar seus treinos e refeições de forma prática.  
O objetivo é permitir que o usuário acompanhe sua evolução semanal e mensal em relação ao volume de treino e à ingestão de proteína, sem precisar de aplicativos complexos ou cheios de menus confusos.  
A proposta é unir **simplicidade, organização e feedback visual**, ajudando o usuário a entender o próprio progresso.

---

## 2. Problema

Muitas pessoas praticam atividades físicas com frequência, mas não possuem um meio prático de acompanhar o que estão fazendo ou comendo.  
Aplicativos populares costumam ser pesados, pagos ou difíceis de usar no dia a dia.  
O problema central é, portanto, **a falta de uma ferramenta simples e gratuita** para registrar treinos e refeições, com foco na **usabilidade e facilidade de uso**.

---

## 3. Objetivo Geral

Desenvolver uma aplicação web que permita **registrar e acompanhar treinos e refeições**, mostrando um **resumo semanal** da evolução de forma visual e intuitiva.

---

## 4. Objetivos Específicos

- Permitir o **cadastro e login** de usuários.  
- Implementar o **registro de treinos** com campos básicos (exercício, séries, repetições e carga).  
- Implementar o **registro de refeições** com campos de descrição e quantidade de proteína.  
- Exibir um **dashboard semanal** com os dados consolidados.  
- Permitir **edição, exclusão e busca** dos registros.  
- Garantir **mensagens claras de sucesso ou erro**.

---

## 5. Público-Alvo

O sistema é voltado para praticantes de atividades físicas de qualquer nível que desejem manter um controle simples de treinos e alimentação.  
Também pode ser útil para iniciantes que buscam organizar a rotina e entender sua evolução semanal.

---

## 6. Escopo do MVP

**Inclui:**
- Autenticação (cadastro e login).  
- CRUD de treinos.  
- CRUD de refeições.  
- Dashboard semanal com resumo (treinos, volume, proteína/dia).  
- Filtros por período (hoje, semana, mês).  
- Mensagens de feedback e validações de campos obrigatórios.

**Não inclui:**
- Metas automáticas de treino.  
- Integração com dispositivos de terceiros.  
- Cálculo automático de calorias ou macronutrientes.

---

## 7. Requisitos Funcionais

| Código | Descrição |
|--------|------------|
| RF01 | O sistema deve permitir o cadastro e login de usuários. |
| RF02 | O sistema deve permitir registrar um treino com exercício, séries, repetições e carga. |
| RF03 | O sistema deve permitir editar e excluir treinos registrados. |
| RF04 | O sistema deve permitir registrar refeições com nome, porção e proteína estimada. |
| RF05 | O sistema deve permitir editar e excluir refeições. |
| RF06 | O sistema deve exibir um dashboard semanal com resumo de treinos e proteínas. |
| RF07 | O sistema deve permitir filtrar registros por período e buscar exercícios. |
| RF08 | O sistema deve apresentar mensagens claras de sucesso ou erro. |

---

## 8. Requisitos Não Funcionais

| Código | Descrição |
|--------|------------|
| RNF01 | A interface deve ser simples, direta e responsiva. |
| RNF02 | As respostas do sistema devem ocorrer em menos de 500ms em ambiente local. |
| RNF03 | As senhas devem ser armazenadas com hash. |
| RNF04 | O sistema deve ser executável com um único comando. |
| RNF05 | O sistema deve garantir acessibilidade mínima (rótulos, contraste e feedback visual). |

---

## 9. Critérios de Aceite

- O usuário deve conseguir se cadastrar, logar e registrar ao menos um treino e uma refeição.  
- O dashboard deve exibir corretamente os dados da semana.  
- O sistema deve impedir o envio de campos obrigatórios vazios.  
- Mensagens de feedback devem aparecer após cada ação.  
- O sistema deve funcionar localmente com apenas um comando.

---

## 10. Modelo de Dados (Conceitual)

**Usuário**  
- id_usuario (PK)  
- nome  
- email  
- senha_hash  
- criado_em  

**Treino**  
- id_treino (PK)  
- usuario_id (FK → Usuario)  
- data_hora  
- observacoes  
- percepcao_esforco  

**Exercicio**  
- id_exercicio (PK)  
- nome  
- grupo_muscular  

**TreinoExercicio**  
- id_treino_exercicio (PK)  
- treino_id (FK → Treino)  
- exercicio_id (FK → Exercicio)  

**Serie**  
- id_serie (PK)  
- treino_exercicio_id (FK → TreinoExercicio)  
- repeticoes  
- carga  
- duracao_seg  

**Refeicao**  
- id_refeicao (PK)  
- usuario_id (FK → Usuario)  
- data_hora  
- descricao  
- proteina_g  
- carbo_g  
- gordura_g  

---

## 11. Critérios de Usabilidade (IHC)

Durante o desenvolvimento, o sistema seguiu princípios básicos de boa interface:

- Clareza nas informações exibidas.  
- Consistência visual entre telas.  
- Simplicidade (menos cliques possíveis).  
- Feedback visual rápido após ações.  
- Opções de correção (editar/excluir).

---

## 12. Métricas de Sucesso

- Registrar um treino em menos de 30 segundos.  
- 95% dos fluxos principais funcionando sem erro nos testes.  
- Cobertura mínima de testes de back-end de 60%.

---

## 13. Conclusão

O **FitTrack** é um projeto funcional e acessível que permite registrar treinos e refeições de maneira prática.  
Esta primeira versão (MVP) serve como base para futuras melhorias, incluindo gráficos, metas automáticas e dark mode — conforme os feedbacks coletados na Situação 3.

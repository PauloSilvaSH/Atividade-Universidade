> **Portfólio:** [Índice geral dos projetos](https://github.com/PauloSilvaSH/Project_finance_pucrs/blob/main/PORTFOLIO.md) · [README de perfil pronto para publicação](https://github.com/PauloSilvaSH/Project_finance_pucrs/blob/main/README_PROFILE.md)

# Atividades de Programação e Análise de Dados — Universidade

Repositório com exercícios acadêmicos em Python e análise de dados meteorológicos. Os arquivos identificados incluem um script interativo de temperaturas, um exercício com dados simulados de alunos e um notebook que consulta registros meteorológicos a partir de CSV.

## 1. Análise meteorológica — `projeto_puc_2.ipynb`
### Atividades implementadas
- Lê `projeto_puc.csv` com Pandas.
- Converte a coluna de data para datetime e deriva ano e mês.
- Permite informar datas inicial e final para filtrar o período analisado.
- Calcula indicadores de precipitação, temperatura mínima/máxima, umidade relativa e velocidade do vento.
- Oferece opções de saída e cria gráficos de médias de temperatura mínima por ano e por mês.

### Pontos de atenção
- As datas digitadas são comparadas com a coluna datetime; converter as entradas para datetime antes do filtro torna a comparação consistente.
- A atribuição da variável de velocidade do vento deve ser conferida: no trecho identificado, a expressão parece não chamar o método `.max()`.
- Algumas mensagens descrevem médias enquanto o código usa máximo; alinhar rótulos, cálculos e interpretação.
- Validar período vazio e valores ausentes antes de calcular estatísticas.

## 2. Temperaturas máximas mensais — `Projeto_1.py`
- Solicita ao usuário uma temperatura máxima para cada mês.
- Valida os valores no intervalo de -60 °C a 50 °C e solicita novamente entradas inválidas.
- Calcula média anual das máximas, conta meses com temperatura acima de 33 °C e identifica os meses de maior e menor temperatura.

## 3. Simulação de idade e curso — `Idade e trabalho`
- Gera 50 registros simulados, sorteando idade entre 18 e 60 anos, curso e semestre.
- Calcula média inteira de idade, identifica o curso associado ao registro de maior idade e conta registros no quinto semestre.
- O arquivo usa o módulo `random`; é necessário importá-lo antes da execução.

## Tecnologias identificadas
Python, Pandas, Matplotlib e dados CSV.

## Como reproduzir
- Para o notebook meteorológico, mantenha `projeto_puc.csv` no diretório de execução e instale `pandas` e `matplotlib`.
- Para `Projeto_1.py`, execute em terminal com Python 3.
- Para o exercício `Idade e trabalho`, acrescente `import random` caso não esteja definido em outra célula/arquivo.

## Melhorias recomendadas
- Organizar os exercícios em diretórios e adicionar instruções de execução.
- Padronizar nomes de variáveis e separar entrada, processamento e saída.
- Acrescentar testes para limites de temperatura, períodos sem dados e valores ausentes.
- Registrar a origem e o significado das colunas do CSV meteorológico.

## Arquivos principais
- [Notebook meteorológico](projeto_puc_2.ipynb)
- [Script de temperaturas](Projeto_1.py)
- [Exercício de simulação](Idade%20e%20trabalho)
- [Dados meteorológicos](projeto_puc.csv)

## Limitações
A documentação foi preparada a partir do código disponível no repositório. Os notebooks e scripts não foram executados integralmente nesta etapa.

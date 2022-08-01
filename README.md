![image](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Rossmann_Logo.svg/2560px-Rossmann_Logo.svg.png)

**Dirk Rossmann GmbH** (usual: Rossmann) é uma das maiores redes de drogarias da Europa, com cerca de 56.200 funcionários e mais de 4.000 lojas em toda a Europa.

**“Quanto cada loja da rede irá vendar em 6 semanas?”**

Esse foi o questionamento do CEO da ROSSMANN para os seus gerentes e diretores, o mesmo planeja realizar uma grande reforma em sua rede. A motivação? Padronizar todas as drogarias, tanto com estoque, quanto esteticamente, com a finalidade de todas terem o rendimento parecido uma com as outras. O método atual que a empresa utiliza para prever esse comportamento é um método de média simples, atrelado em algumas planilhas com dados no excel. Foi solicitado o serviço de um Cientista de Dados para a implementação de um modelo mais robusto para a empresa, utilzando modelos de Machine Learning.

***'Projeto Fictício'***

# Ferramentas Utilizadas

- Python
- Jupyter Notebook
- Sklearn
- BORUTA
- Seaborn


# Premissas do Negócio
- Dias em que as lojas estavam fechadas, não foram utilizados.
- Descartados valores de vendas (Sales) igual a 0.
- Os clientes(‘Customers`) possuem uma variação enorme e são difíceis de prever, nesse primeiro ciclo do CRISP-DM, eles não foram utilizados.
- Lojas que não possuíam informações de competidores próximos, foi utilizado a maior distância de algum já existente.


# Lista de Atributos:

| Atributos                        | Explicação                                                      |
| -------------------------------- | ------------------------------------------------------------ |
| store                            | Identificação da loja                                   |
| day_of_week                      | Dia da semana       |
| sales                            | O valor arrecado em vendas do dia.                         |
| customers                        | Fluxo de clientes que realizaram compras no dia                       |
| cpen                             | Funcionamento da loja 0 = Fechada, 1 = Aberta |
| state_holiday                     | Indica um feriado estadual. a = public_holiday (Feriados Normais), b = easter_holiday (feriado da Páscoa), c = christmas (Natal).
| school_holiday                    | Informa se a loja se manteve aberta ou fechada duranto os feriados escolares. |
| store_type                        | Diferencia entre 4 modelos de loja diferentes: a, b, c, d  |
| assortment                       | Informa a variedade de estoque da loja (Ex: Extended possui mais itens váriados que o Basic.): a = Basic, b = Extra, c = Extended |
| competition_distance              | Distancia em metros do competidor mais proximo           |
| competition_open_since[Month/Year] | Informa ano e mês em que o concorrente mais próximo foi inaugurado |
| promo                            | Informa se a loja está realizando promoção no dia.         |
| promo2                           | Informa uma continuido de promoção para algumas lojas, indicando: 0 = Loja não participa, 1 = Loja está participando |
| promo2_since_year_week           | Descreve o ano e a semana em que a loja começou a participar da Promo2 |
| promo_interval                    | Descreve os intervalos consecutivos de início da promoção 2, nomeando os meses em que a promoção é iniciada novamente. Por exemplo. "Fev, maio, agosto, novembro" significa que cada rodada começa em fevereiro, maio, agosto, novembro de qualquer ano para aquela loja |

***Informação retirada e traduzida do desafio postado no Kaggle***

Link: https://www.kaggle.com/competitions/rossmann-store-sales/discussion

# Estratégia da solução

**Passo 01**  – Descrição dos Dados: Etapa onde renomeamos colunas, verificamos dimensões, tipos, checa-se dados faltantes e os preenche, também se verifica os tipos, os dados números e categóricos.

**Passo 02** – Feature Engineering: Etapa onde criamos um mapa mental do projeto, para verificar o fenômeno, agentes e atributos. A partir deles, começamos a criar hipóteses para serem validadas depois.

<a href="https://ibb.co/2vFZ4Y5"><img src="https://i.ibb.co/tqHLrP3/download.png" alt="download" border="0"></a>

**Passo 03** – Filtragem de Dados: Etapa onde filtramos dados para serem analisados por modelos, um exemplo foi a retirada das vendas com valor nulo.

**Passo 04** – Análise Exploratória de dado: Etapa mais importante do projeto, onde ganhamos experiência de negócio, validamos hipóteses e percebemos quais variáveis serão importantes para o modelo.

**Passo 05** – Preparação de dados: Etapa onde preparamos os dados para os modelos de aprendizado de máquina, Rescaling, Enconding, Nature Transformation, entre outras transformações.

**Passo 06** – Feature Selection – Etapa onde se seleciona os atributos mais relevantes para o projeto, nesse passo utilizamos o método BORUTA e realizamos um comparativo com o que o BORUTA selecionou mais as hipóteses validadas no passo 04.

**Passo 07** – Machine Learning Modelling – Etapa onde se treina os modelos de aprendizado de máquina.

**Passo 08** – Hyperparamenter Fine Tunning: Etapa onde se escolhe os melhores parâmetros para o modelo escolhido no passo anterior.

**Passo 09** – Conversão de resultado: Etapa onde transformamos o resultado do modelo em valores para o negócio.
<a href="https://ibb.co/7WnKfZh"><img src="https://i.ibb.co/Xs7tQKH/machine-learning-perfomance.jpg" alt="machine-learning-perfomance" border="0"></a>

**Passo 10** – Deploy do modelo para produção: Etapa da criação da classe e publicação na nuvem para que outros tenham acesso e utilizem a ferramenta para melhorias de negócio.

**Passo 11** – Telegram Bot: Etapa da criação da API que vai servir para consultar as previsões que o modelo teve, fácil acesso para o time de negócios.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/jbhnjZX/CAPTURA2.jpg" alt="CAPTURA2" border="0"></a>

Para acessar, só clicar ao lado.
[<img alt="Telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>](https://t.me/rossmanndacbot)


# Data Insights

#### Hipótese 12 – Lojas deveriam vender menos durante os feriados escolares.

**FALSA** - Lojas vendem mais durante os feriados.

#### Hipótese 6 – Lojas com mais promoções consecutivas vendem mais.

**FALSA** - Lojas com promoções consecutivas vendem menos.

#### Hipótese 11 – Lojas deveriam vender menos nos finais de semana.

**VERDADEIRA** – Lojas vendem menos no final de semana, sendo o sábado o pior dia.




#  Modelos de Machine Learning aplicados
Teste foram realizados usando os seguintes algoritmos:

**Average Model**

**Linear Regression Model**

**Linear Regression Regularized Model - Lasso**

**Random Forest Regressor**

**XGBoost Regressor**

# Machine Learning Model Performance

## Single Performance

| Model Name | MAE    | MAPE      | RMSE |
|-----------|---------|-----------|---------|
|  Random Forest Regressor  | 678.3939 | 0.0998  | 1009.0086 |
|  Average Model  	  | 1354.8004 | 0.2065   | 1835.1355 |
|  Linear Regression | 1867.0898 | 0.2927   | 2671.0492 |
|  Linear Regression - Lasso  | 1891.7049 | 0.2891 | 2744.4517|
|  XGBoost	  | 6994.5139| 0.9999	   | 7628.1868|

## Real Performance - Cross Validation

|Model Name|	MAE CV	|MAPE CV	                      |  RMSE CV |
|------------------|---------------|-----------|---------------|
|	Linear Regression|	1992.27+/-41.68|	0.29+/-0.01|	2846.37+/-87.77|
|	Lasso|	2035.84+/-54.02	|0.29+/-0.0	|2964.68+/-89.66|
|	Random Forest Regressor|	829.99+/-105.58|	0.12+/-0.02|	1263.55+/-191.19|
|	XGBoost Regressor	|7267.6+/-110.34|	1.0+/-0.0|	7906.3+/-126.36|

Apesar do XGBoost ter o pior performance nessa analise, decidi apostar nela na próxima, visto que o XGBoost e mais compacto e ocupa menos espaço para ser publicado na nuvem.
Para utilizar esse método levamos em que um modelo que ocupa muito espaço, acaba custando muito a empresa.

## Final Performance - Hyperparameter Fine Tunning Cross Validation

Após encontrar os melhores parâmetros para o modelo através do metódo Random Search as métricas finais para o modelo foram as seguintes:

| Model Name | MAE CV   | MAPE CV      | RMSE CV |
|-----------|---------|-----------|---------|
|  XGBoost Regressor	  | 640.9477 | 0.0936   | 934.5904 |

## Modelo com XGBoost Regressor

| Cenário | Valores   |
|-----------|---------|
|  Predições	  | R$284,345,472.00 |
|  Pior Cenário	  | R$283,626,861.83 |
|  Melhor Cenário	  | R$285,064,088.07 |


#  Conclusão

Para o primeiro ciclo o XGBoost, obteve um excelente resultado e bem aceitável, no quarto gráfico, da para perceber que existem algumas lojas que nao estão centralizadas no cone, essas lojas por algum motivo apresentaram
um erro um pouco alto comparado com as outras lojas, em um segundo ciclo da metodologia (CRISP-DM) será analisado a risca para entender o que está afetando esse fenômeno.



#  Próximos Passos

Iniciar um segundo ciclo para analisar o problema buscando abordagens diferentes, tendo em vista principalmente as lojas com o comportamento difíceis de serem previsto.

Possíveis pontos para serem abordados no segundo ciclo:

- **Utilizar novos atributos.**

- **Entender os fenomenos das lojas que ficaram fora do padrão da maioria.**

- **Com o primeiro ciclo rodando e entregue, podemos treinar um segundo modelo e realizar as comparações com o primeiro, provavelmente iremos utilizar o Random Forest Regressor, que apresentou bons resultados mesmo sem passar pela etapa de Fine Tunning.**


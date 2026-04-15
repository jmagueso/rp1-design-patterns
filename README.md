# Roteiro Prático: Padrões de Projeto em Pipelines de Dados

## Objetivo
Nesta prática, você irá experimentar o uso dos principais padrões de projeto existentes, aplicando-os à arquitetura de pipelines de dados.

## Requisitos
* **Git SCM**: [https://git-scm.com/](https://git-scm.com/)
* **Visual Studio Code** ([https://code.visualstudio.com/](https://code.visualstudio.com/)) ou **PyCharm Community Edition** ([https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)). Essas IDEs são apenas recomendações. O projeto foi construído utilizando a sua estrutura. Fique à vontade para utilizar outra, caso queira.
* **Python 3.9+**

## Entrega
O roteiro deverá ser entregue utilizando o mecanismo de pull-request.

1.  Faça o fork do projeto para a sua conta ([https://github.com/jemaf/dcc603-rp-design-patterns-ds/fork](https://github.com/jemaf/dcc603-rp-design-patterns-ds/fork)).
2.  Implemente sua solução no fork associado à sua conta. Não se esqueça de fazer os commits à medida em que implementar as tarefas pendentes.
3.  Certifique-se de que você realizou o push com todos os commits.
4.  Realize o Pull Request do seu projeto. Para isso, acesse o repositório original, e clique no botão "Compare & Pull Request", presente no banner amarelo do topo da página. Para mais informações veja: [Documentação GitHub - Criando um Pull Request](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

## Avaliação
Cada implementação de padrão será avaliada em 1 ponto.

* **Total**: se sua implementação passar por todos os testes.
* **50%**: se sua implementação passar por metade dos casos de teste.
* **25%**: se sua implementação passar por pelo menos um caso de teste.

---

## Padrão Singleton
**Classes presentes no pacote `singleton`**

O padrão de projeto Singleton é utilizado como forma de disponibilizar apenas uma instância de uma determinada classe. Na Engenharia de Dados, esse tipo de comportamento é fundamental em situações onde um recurso "caro" deve ser compartilhado em diferentes partes do pipeline, como a conexão com um Data Lake.

> **Atividade:** Altere a classe `singleton.DataLakeConnection` para que sua instância seja disponibilizada por meio de um singleton, garantindo que o sistema não estoure o limite de conexões simultâneas ao carregar diferentes lotes de dados.

## Padrão Decorator
**Classes presentes no pacote `decorator`**

A equipe de Processamento de Linguagem Natural (NLP) da sua empresa entrou em contato requisitando seus serviços. Eles desejam implementar uma funcionalidade flexível para limpar e transformar textos de comentários de clientes (tweets, reviews) antes de jogá-los no modelo. Na solução implementada atualmente, os projetistas criaram uma classe geral denominada `ProcessadorTexto`, e então derivaram uma série de subclasses para cada combinação de limpeza, tais como `ApenasMinusculas`, `MinusculasESemPontuacao`, etc. Rapidamente você observou que esse problema é grave, pois o número de classes aumentaria vertiginosamente de acordo com a combinação de filtros.

Ao analisar o problema mais de perto, você percebeu que ele poderia ser tratado pelo padrão decorador. 

**Atividade:**
Implemente uma demonstração desse padrão para a equipe de NLP com base no modelo já existente no pacote `text_decorator`. Essa implementação deverá conter as quatro classes de filtro: `LowerCase` (minúsculas), `RemovePunctuation` (remove pontuação), `RemoveStopWords` (remove pronomes e preposições) e `Stemming` (extrai a raiz das palavras). Ainda, as classes deverão reimplementar os métodos `processarTexto` e `tempoEstimadoProcessamento`, de acordo com as seguintes informações:

* O texto deve ser modificado sequencialmente por cada filtro aplicado.
* Os filtros possuem o seguinte custo computacional (em milissegundos por palavra): `LowerCase` custa 0.25, `RemovePunctuation` custa 0.50, `RemoveStopWords` custa 1.00 e `Stemming` custa 1.50.

> **Importante:** Você deverá criar e implementar o arquivo filtros.py, contendo todas as classes de filtro necessárias. Não é necessário alterar nenhum outro arquivo do projeto.

## Padrão Strategy
**Classes presentes no pacote `strategy`**

Você foi designado como responsável por desenvolver o módulo de Tratamento de Dados Ausentes (Missing Values) de uma biblioteca interna da sua empresa. Como os tipos de dados variam muito entre os departamentos, o módulo deve ser genérico o suficiente para aceitar variados métodos de preenchimento (imputação), além de respeitar o princípio de aberto/fechado para facilitar a adição de novas técnicas no futuro.

Ao estudar o problema, você chegou à conclusão de que essa lógica pode ser encapsulada utilizando o padrão strategy. 

**Atividade:**
Implemente este padrão com base nos arquivos já existentes no pacote `strategy`. Seu padrão deverá suportar três estratégias diferentes de imputação para colunas numéricas:

* `MeanImputationStrategy`: Preenche os valores ausentes com a média da coluna.
* `MedianImputationStrategy`: Preenche os valores ausentes com a mediana da coluna.
* `ZeroImputationStrategy`: Preenche os valores ausentes com o valor 0.

Para isso, suas classes de imputação deverão herdar a classe abstrata `ImputationStrategy`. Você ainda deverá alterar a classe `DataCleaner` para que ela faça o tratamento utilizando as estratégias criadas. Essa classe deverá implementar um `setStrategy(ImputationStrategy)` para definir a técnica atual e um método `clean_column` para chamar a execução da estratégia definida.

> **Importante:** Você deverá criar e implementar o arquivo strategies.py e alterar apenas o arquivo data_cleaner.py. Não é necessário modificar nenhum outro arquivo do projeto.

## Padrão Observer
**Classes presentes no pacote `observer`**

Treinar modelos de Machine Learning pode levar horas. É crucial que o sistema avise diferentes serviços (como painéis de visualização e arquivos de log) sempre que uma nova "época" (epoch) de treinamento for concluída.

> **Atividade:** Dado o código do padrão observer presente no pacote `observer`, implemente os trechos que estão faltando para conectar o sujeito `ModelTrainer` aos observadores `ConsoleLogger` e `MetricsDashboard`, garantindo que eles recebam as métricas de acurácia em tempo real.

## Padrão Template Method
**Classes presentes no pacote `template_method`**

O fluxo de avaliação de modelos preditivos da sua equipe está sendo padronizado e sua ajuda foi solicitada. O objetivo é praticar conceitos do padrão Template Method, separando um fluxo fixo de operações de validação da variação de comportamento entre diferentes tipos de modelos (Classificação vs. Regressão).

**Contexto:**
O sistema possui o pipeline `ModelEvaluator`, cujo processo de avaliação segue sempre os mesmos passos:
1. Dividir os dados em treino e teste (Train-Test Split).
2. Treinar o modelo com os dados de treino.
3. Fazer as predições com os dados de teste.
4. Calcular as métricas de erro/acerto.

**Atividade:**
Sua tarefa é completar os trechos de código faltantes para o correto funcionamento do sistema:
* A classe abstrata `ModelEvaluator` já define o esqueleto no método `evaluate()`. Seu trabalho é implementar o método abstrato `calculate_metrics()` nas subclasses concretas `ClassificationEvaluator` e `RegressionEvaluator`.
* Na classe `ClassificationEvaluator`, a métrica calculada deve ser a Acurácia (Accuracy).
* Na classe `RegressionEvaluator`, a métrica calculada deve ser o Erro Quadrático Médio (MSE).

## Padrão Adapter
**Classes presentes no pacote `adapter`**

A infraestrutura de dados da empresa agora exige que todas as rotinas leiam arquivos em formato JSON. No entanto, o departamento de vendas ainda utiliza um serviço legado (`LegacyCSVReader`) que extrai relatórios brutos do banco antigo em formato CSV e possui uma interface incompatível.

**Atividade:**
Implemente a classe `CSVToJsonAdapter` que implementa a interface moderna `JSONDataSource` e chama o serviço legado `LegacyCSVReader`.

**Dicas:**
* O Adapter deve adaptar a interface antiga (`read_csv_lines`) para a interface nova (`get_json_records`).
* O objetivo é utilizar o `LegacyCSVReader` sem alterar seu código-fonte.
* Pense no Adapter como um "tradutor" de dicionários que permite ao novo pipeline de Machine Learning ingerir os dados do sistema de vendas perfeitamente.

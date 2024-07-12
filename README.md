## Projeto de Predição de Churn
#### Introdução:

Este projeto tem como objetivo desenvolver um aplicativo web para prever a rotatividade de clientes (churn) de uma empresa de telecomunicações. O aplicativo utiliza um modelo de aprendizado de máquina treinado para identificar clientes com alto risco de churn, permitindo que a empresa tome medidas proativas para retê-los.

#### Ambiente de Desenvolvimento:

* Linguagem de programação: Python 3.12
* IDE: Visual Studio Code
* Bibliotecas:
As bibliotecas necessárias estão listadas no arquivo requirements.txt.
#### Instruções para Execução Local:

* Clone o repositório do GitHub.
* Crie um ambiente conda com Python 3.12 no terminal.
* Instale as bibliotecas do arquivo requirements.txt usando o comando pip install -r requirements.txt.
* Navegue até o diretório do aplicativo (app).
* Execute o aplicativo no terminal usando o comando streamlit run app/app.py.
#### Dados:

* O dicionário de dados utilizado neste projeto pode ser encontrado [neste link](https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset)

* A fonte original dos dados pode ser acessada [aqui](https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113)

#### Análise e Pré-processamento de Dados:

A análise e o pré-processamento de dados foram realizados de acordo com a metodologia CRISP-DM e estão documentados no notebook notebooks/note.ipynb. Este notebook contém comentários detalhados, documentação completa e gráficos ilustrativos. O pipeline do modelo treinado foi salvo no formato .pkl usando a biblioteca joblib e é utilizado no aplicativo app.py.

#### Aplicativo Web

O aplicativo web está disponível no seguinte [link:](https://churnpredictor-oeqzx8kgmnsfbe9rtxernq.streamlit.app)

O aplicativo permite que o usuário faça previsões de churn para vários clientes simultaneamente, utilizando um arquivo CSV como entrada. O resultado da previsão pode ser visualizado no próprio aplicativo ou baixado em formato CSV. O aplicativo também indica se o cliente está em risco de churn e qual a probabilidade de churn prevista.

#### Recursos Adicionais:

O notebook notebooks/note.ipynb contém informações detalhadas sobre a análise e o pré-processamento de dados, a seleção e o treinamento do modelo, a otimização de hiperparâmetros e a avaliação do modelo.
O arquivo requirements.txt lista todas as bibliotecas necessárias para executar o projeto.

#### Contribuições:

Sinta-se à vontade para contribuir com este projeto abrindo issues no GitHub ou enviando pull requests com melhorias.

**Para saber mais:**

* [Conecte-se comigo no LinkedIn](https://www.linkedin.com/in/daniel-braga-reis-725aa012a/)
* [Explore meus projetos no GitHub](https://github.com/Danielbrgs?tab=repositories)

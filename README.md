# monitoramento_mercado_seguros_brasil
Construção de um pipeline de dados para ingestão, transformação, modelagem e análise dos dados públicos do mercado de seguros no Brasil
# 📊 Monitoramento do Mercado de Seguros no Brasil

## 📌 Visão Geral
Este projeto tem como objetivo construir um pipeline de dados para ingestão, transformação, modelagem e análise dos dados públicos da **SUSEP (Superintendência de Seguros Privados)**, com foco exclusivamente em **seguros**.

A partir da base **SES (Sistema de Estatísticas da SUSEP)**, o projeto organiza e estrutura os dados em um **Data Warehouse** no modelo dimensional estrela, permitindo calcular indicadores de mercado como:

- 📈 Evolução de prêmios e sinistros
- 🔍 Índice de Sinistralidade (Loss Ratio)
- 🏆 Market Share por seguradora e ramo
- 💰 Eficiência Comercial (Despesas / Prêmios)

O resultado final inclui **dashboards interativos** e documentação clara para uso como **portfólio de engenharia de dados**.

---

## 🎯 Objetivos do Projeto
- Ingerir e tratar os CSVs da SUSEP.
- Modelar um **Data Warehouse** analítico.
- Criar **KPIs financeiros do mercado de seguros**.
- Construir dashboards de acompanhamento.
- Demonstrar habilidades práticas em **engenharia de dados**.

---

## 🛠️ Stack de Ferramentas

- **Linguagem:** Python (pandas, requests, sqlalchemy)
- **Banco de Dados (DW):** PostgreSQL
- **Transformação:** SQL / dbt
- **Visualização:** Power BI ou Metabase
- **Versionamento:** Git + GitHub
- **Documentação:** Markdown + Diagramas ERD/Estrela

---

## 📂 Estrutura de Pastas

monitoramento-seguros-brasil/
│
├── data/ # Dados brutos e tratados
│ ├── raw/ # CSVs originais
│ └── processed/ # Dados tratados
│
├── notebooks/ # Análises exploratórias
│ ├── 01_download.ipynb
│ ├── 02_limpeza.ipynb
│ └── 03_analise.ipynb
│
├── src/ # Scripts Python
│ ├── ingestao/ # Download e carga inicial
│ ├── transformacao/ # Limpeza e padronização
│ └── carga/ # Inserção no banco
│
├── models/ # Modelagem SQL/dbt
│ ├── dim_empresa.sql
│ ├── dim_ramo.sql
│ ├── dim_tempo.sql
│ └── fato_seguros.sql
│
├── dashboards/ # Dashboards e prints
│ ├── dashboard.pbix
│ └── imagens/
│
├── docs/ # Documentação extra
│ ├── diagramas/ # ERD e modelo estrela
│ └── relatorio.md
│
├── requirements.txt # Dependências Python
├── README.md # Explicação do projeto
└── LICENSE # Licença 


---

## 🧩 Modelo Dimensional

**Dimensões:**
- `dim_empresa` (Seguradoras – Ses_cias)
- `dim_ramo` (Ramos de Seguros – Ses_ramos)
- `dim_tempo` (derivada de `damesano`)

**Fato:**
- `fato_seguros` (Prêmios, Sinistros, Despesas – Ses_seguros)

---

## 📊 KPIs Principais

- **Índice de Sinistralidade (Loss Ratio):**  
  `sinistros_retidos / prêmios_ganhos`

- **Market Share por Seguradora:**  
  `prêmios_diretos da empresa / total do mercado`

- **Eficiência Comercial:**  
  `despesas_comerciais / prêmios_diretos`

- **Evolução Temporal:**  
  Crescimento mês a mês e ano a ano de prêmios e sinistros.

---

## 🚀 Passos de Execução

1. **Preparação**  
   - Clonar repositório  
   - Criar ambiente virtual  
   - Instalar dependências:
     ```bash
     pip install -r requirements.txt
     ```

2. **Ingestão**  
   - Rodar script para baixar dados SUSEP:
     ```bash
     python src/ingestao/baixar_dados.py
     ```

3. **Transformação**  
   - Rodar notebooks de limpeza em `notebooks/`.

4. **Carga**  
   - Carregar dados tratados no PostgreSQL:
     ```bash
     python src/carga/load_postgres.py
     ```

5. **Modelagem**  
   - Executar queries SQL/dbt para criar tabelas fato e dimensões.

6. **Visualização**  
   - Abrir dashboard no Power BI ou Metabase.

---

## 📈 Dashboards
Os dashboards apresentam:
- Evolução mensal de prêmios e sinistros por ramo
- Ranking de seguradoras por participação de mercado
- Índice de sinistralidade comparativo
- Despesas comerciais vs. prêmios diretos

*(Imagens e arquivos estão disponíveis em `/dashboards/`)*

---

## 📜 Licença
Este projeto é distribuído sob a licença **MIT**.  
Você pode usá-lo livremente para estudos, portfólio e adaptações.

---

## 👤 Autor
**Vanderlândio Zeferino da Rocha (Vando)**  
Analista de Sistemas e Desenvolvedor SQL | Especialista em Bancos de Dados  

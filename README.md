# 📊 Pipeline ETL com Python + SQLite + Docker

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-ETL-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Status](https://img.shields.io/badge/Status-Funcional-success)

---

## 🚀 Visão Geral

Pipeline ETL completo desenvolvido em Python com foco em **Engenharia de Dados**, simulando um fluxo real de:

- Geração de dados fictícios
- Extração (CSV / Excel)
- Transformação e limpeza
- Carga em banco SQLite
- Geração de relatórios automatizados
- Execução em Docker

---

## 🧱 Arquitetura do Pipeline


            ┌─────────────────────┐
            │  Geração de Dados   │
            │      (Faker)        │
            └─────────┬───────────┘
                      ↓
            ┌─────────────────────┐
            │     Extração        │
            │   CSV / Excel       │
            └─────────┬───────────┘
                      ↓
            ┌─────────────────────┐
            │  Transformação      │
            │     (Pandas)        │
            └─────────┬───────────┘
                      ↓
            ┌─────────────────────┐
            │      Carga          │
            │     (SQLite)        │
            └─────────┬───────────┘
                      ↓
            ┌─────────────────────┐
            │    Relatórios       │
            │  CSV / Excel BI     │
            └─────────────────────┘

            
---


## ⚙️ Como executar o projeto



### 🐍 Execução local

```bash
pip install -r requirements.txt
python main.py



Execução com Docker
docker build -t etl-python .
docker run --rm -v ${PWD}:/app etl-python


🐳 Execução com Docker Compose

docker compose up --build


📊 Saídas do Pipeline
📂 Dados gerados
clientes.xlsx
produtos.csv
vendas.csv

🗄️ Banco de dados
banco/empresa.db (SQLite)

📈 Relatórios
relatorio.csv
relatorio.xlsx (múltiplas abas)

📜 Logs
logs/pipeline.log

📌 Métricas geradas
💰 Faturamento total
🏆 Top clientes
📦 Produtos mais vendidos
🏙️ Faturamento por cidade
📊 Faturamento por categoria
📅 Análise temporal de vendas
🧠 Tecnologias utilizadas

Python 3.11
Pandas
Faker
SQLite
XlsxWriter
Docker
CSV / Excel

🐳 Docker

O projeto é totalmente containerizado.

✔ Ambiente isolado
✔ Reprodutível
✔ Sem necessidade de instalação local

🎯 Objetivo

Simular um pipeline real de Engenharia de Dados com:

boas práticas de ETL
modularização de código
tratamento de dados
persistência em banco
geração de relatórios analíticos
execução em container


## 🧪 Consultas SQL

Exemplos disponíveis em sql/consultas.sql:
-- Faturamento total
SELECT SUM(Valor) FROM vendas;

-- Top produtos
SELECT ProdutoID, SUM(Valor)
FROM vendas
GROUP BY ProdutoID
ORDER BY SUM(Valor) DESC;

## 👨‍💻 Pablo Riquelme Santana de Souza

Projeto desenvolvido para portfólio de Engenharia de Dados com Python.


---


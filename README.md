# 📊 Pipeline ETL com Python, SQLite, Docker e Power BI

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-ETL-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)
![Status](https://img.shields.io/badge/Status-Concluído-success)

---

# 📌 Sobre o projeto

Este projeto implementa um Pipeline ETL (Extract, Transform, Load) completo utilizando Python, simulando um ambiente de Engenharia de Dados.

O pipeline gera dados fictícios, realiza validação, transformação, carga em banco de dados SQLite e produz relatórios analíticos. Os dados também são utilizados para construção de um dashboard interativo no Power BI.

---

# 🚀 Tecnologias

- Python 3.11
- Pandas
- Faker
- SQLite
- Docker
- XlsxWriter
- Power BI
- Git
- GitHub

---

# 🏗 Arquitetura

```
          Geração de Dados
                 │
                 ▼
        CSV / Excel (Extract)
                 │
                 ▼
     Limpeza e Transformação
             (Pandas)
                 │
                 ▼
        Banco SQLite (Load)
                 │
                 ▼
      Relatórios Excel / CSV
                 │
                 ▼
        Dashboard Power BI
```

---

# 📂 Estrutura do Projeto

```
Pipeline-ETL-Python/
│
├── banco/
│   └── empresa.db
│
├── dados/
│   ├── clientes.xlsx
│   ├── produtos.csv
│   └── vendas.csv
│
├── logs/
│   └── pipeline.log
│
├── powerbi/
│   ├── dashboard.pbix
│   ├── dashboard.png
│   └── dashboard.pdf
│
├── relatorios/
│   ├── relatorio.csv
│   └── relatorio.xlsx
│
├── scripts/
│
├── Dockerfile
├── docker-compose.yml
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Executando Localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

---

# 🐳 Executando com Docker

Criar imagem:

```bash
docker build -t etl-python .
```

Executar:

```bash
docker run --rm -v ${PWD}:/app etl-python
```

---

# 📊 Dados Gerados

O pipeline gera automaticamente:

- Clientes (Excel)
- Produtos (CSV)
- Vendas (CSV)
- Banco SQLite
- Relatório CSV
- Relatório Excel
- Log de execução

---

# 📈 Dashboard Power BI

O projeto inclui um dashboard desenvolvido no Power BI utilizando os dados produzidos pelo pipeline ETL.

### Indicadores

- 💰 Receita Total
- 📦 Produtos Mais Vendidos
- 👥 Top Clientes
- 🏙 Receita por Cidade
- 📈 Evolução Mensal
- 📊 Ticket Médio

### Preview

> Adicione aqui uma captura de tela do dashboard.

```md
![Dashboard](powerbi/dashboard.png)
```

Arquivos disponíveis:

- `powerbi/dashboard.pbix`
- `powerbi/dashboard.pdf`

---

# 📌 Principais Funcionalidades

✔ Geração automática de dados

✔ Processo ETL completo

✔ Limpeza e transformação de dados

✔ Banco SQLite

✔ Relatórios automáticos

✔ Dashboard Power BI

✔ Execução via Docker

✔ Estrutura modular

---

# 🎯 Objetivo

Demonstrar conhecimentos em:

- Engenharia de Dados
- ETL
- Python
- Pandas
- Docker
- Power BI
- Modelagem de Dados
- Git e GitHub

---

# 🚀 Próximas Melhorias

- PostgreSQL
- Apache Airflow
- API com FastAPI
- Deploy em Azure
- Deploy em AWS
- Atualização automática do Power BI
- Testes automatizados

---

# 👨‍💻 Autor

Desenvolvido por **Pablo Riquelme** como projeto de portfólio para a área de Dados.

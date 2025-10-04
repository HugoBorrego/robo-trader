# Robô Trader com Python

Este projeto é um robô trader que permite ao usuário digitar o ticker de uma ação, buscar dados via API, analisar indicadores técnicos e visualizar gráficos interativos em uma página web.

## 🌐 Link do site (Deploy)
🔗 [Robo Trader Deploy](https://robo-trader-ebon.vercel.app/) 

## 🚀 Funcionalidades

- Busca de dados históricos de ações com `yfinance`
- Cálculo de indicadores como RSI e médias móveis
- Gráficos interativos com `plotly`
- Interface web com `Flask`
- Análise básica de investimento

## 🛠️ Tecnologias

- Python
- Flask
- yFinance
- Plotly
- Pandas
- HTML/CSS

## 📦 Instalação

```bash
git clone https://github.com/HugoBorrego/Robo-Trader.git
cd robo_trader
pip install -r requirements.txt
python app.py
http://127.0.0.1:5000/
```

## 📁 Pasta
```bash
robo_trader/
├── app.py                 # Backend Flask
├── docs/
│   ├── images/            # Imagens
│       └── foto.png      
├── templates/
│   └── index.html         # Página web
├── static/
│   └── style.css          # Estilo da página
├── utils/
│   ├── fetch_data.py      # Função para buscar dados da ação
│   ├── analyze.py         # Função para analisar se é bom investimento
│   └── plot.py            # Função para gerar gráficos
├── requirements.txt       # Dependências
└── README.md              # Documentação do projeto
```

## 📷 Imagens
![Imagem da Análise e do Robô](docs/images/Robo.png)
![Imagem do gráfico](docs/images/Grafico.png)
![Imagem das principais ações](docs/images/Acoes.png)

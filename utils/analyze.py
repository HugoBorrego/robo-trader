# Função para analisar o risco
def calcular_rsi(series, period=14):
    delta = series.diff()
    ganho = delta.clip(lower=0)
    perda = -delta.clip(upper=0)

    media_ganho = ganho.rolling(window=period).mean()
    media_perda = perda.rolling(window=period).mean()

    rs = media_ganho / media_perda
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Função para analisar se é bom investimento
def analyze_data(df):
    rsi = calcular_rsi(df['Close'])
    rsi_valid = rsi.dropna()
    media_movel = df['Close'].rolling(window=20).mean()
    media_valid = media_movel.dropna()

    return {
        'RSI': round(rsi_valid[-1], 2) if not rsi_valid.empty else 'Indefinido',
        'MediaMovel': round(media_valid[-1], 2) if not media_valid.empty else 'Indefinido'
    }

""" 
    Índice de Força Relativa (RSI) - indica se um ativo está sobrecomprado ou sobrevendido

    delta = series.diff(): calcula a variação diária dos preços de fechamento.

    ganho = delta.clip(lower=0): mantém apenas os ganhos (valores positivos).

    perda = -delta.clip(upper=0): mantém apenas as perdas, invertendo o sinal para deixá-las positivas.

    media_ganho = ganho.rolling(window=period).mean(): média móvel dos ganhos em um período (por padrão, 14 dias).

    media_perda = perda.rolling(window=period).mean(): média móvel das perdas no mesmo período.

    rs = media_ganho / media_perda: razão entre ganhos e perdas.

    rsi = 100 - (100 / (1 + rs)): fórmula do RSI. O valor varia de 0 a 100:

        Abaixo de 30 → sobrevendido (possível oportunidade de compra).

        Acima de 70 → sobrecomprado (possível alerta de venda).

"""

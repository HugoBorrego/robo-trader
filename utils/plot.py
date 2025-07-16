import plotly.graph_objects as go


# Função para gerar gráficos
def plot_chart(df):
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    )])
    return fig.to_html(full_html=False)


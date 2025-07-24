from flask import Flask, render_template, request
from utils.fetch_data import get_data
from utils.analyze import analyze_data
from utils.plot import plot_chart

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    chart = None
    analysis = None
    ticker = None  # Novo

    if request.method == 'POST':
        ticker = request.form['ticker']
        try:
            df = get_data(ticker)
            analysis = analyze_data(df)
            chart = plot_chart(df)
        except Exception as e:
            analysis = {'erro': f'Erro ao buscar dados: {e}'}

    return render_template('index.html', chart=chart, analysis=analysis, ticker=ticker)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from data import scrape_poll_data

app = Flask(__name__)

@app.route('/')
def render_dashboard():
    poll_data = scrape_poll_data()

    return render_template('index.html', poll_data=poll_data)

if __name__ == '__main__':
    app.run(debug=True)
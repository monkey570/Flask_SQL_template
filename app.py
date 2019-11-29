from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, text

app = Flask(__name__)
con = open('.\connection_config.txt').read()
app.config['SQLALCHEMY_DATABASE_URI'] = con
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/docs', methods = ['GET', 'POST'])
def show_all():
    if request.method == 'POST':
        query = request.form['query']
    else:
        return render_template('./show_all.html', results = 0)
    results = db.session.execute(text(query))
    return render_template('./show_all.html', results = results)


if __name__ == "__main__":
    app.run(host='localhost', port=3000)

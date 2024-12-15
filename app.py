from flask import Flask, render_template
from app.models import initialize_database, Session, Article

app = Flask(__name__)

@app.route("/")
def index():
    session = Session()
    articles = session.query(Article).all()
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    initialize_database()
    app.run()
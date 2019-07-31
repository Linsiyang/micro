from kanado import Kanado
from kanado import render_template
app = Kanado(__name__)
@app.route('/kami')
def home():
    return render_template("home.html")
@app.route('/lin/<id>')
def home(id):
    return "hello"
from flask import Blueprint

app_route = Blueprint('route', __name__)


"Функция отображения индексной страницы"
@app_route.route('/')
@app_route.route('/index')
@app_route.route('/index.php')
@app_route.route('/index.htm')
@app_route.route('/index.html')
def index():
  return 'Hello, my world!'

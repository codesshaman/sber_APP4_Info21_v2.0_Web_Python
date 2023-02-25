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

"Функция отображения страницы 'о нас'"
@app_route.route('/about')
@app_route.route('/about.php')
@app_route.route('/about.htm')
@app_route.route('/about.html')
def index():
  return 'О нас'

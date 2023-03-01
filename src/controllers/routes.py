from flask import Blueprint, render_template

app_route = Blueprint('route', __name__)

@app_route.route('/')
@app_route.route('/index')
@app_route.route('/index.php')
@app_route.route('/index.htm')
@app_route.route('/index.html')
def index():
  "Функция отображения индексной страницы"
  return render_template('index.html')


@app_route.route('/about')
@app_route.route('/about.php')
@app_route.route('/about.htm')
@app_route.route('/about.html')
def about():
  "Функция отображения страницы 'о нас'"
  return render_template('about.html')

@app_route.route('/test')
@app_route.route('/test.php')
@app_route.route('/test.htm')
@app_route.route('/test.html')
def test():
  "Функция отображения страницы 'о нас'"
  return render_template('test.html')

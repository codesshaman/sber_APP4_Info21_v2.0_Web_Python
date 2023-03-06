from flask import Blueprint, render_template
from model.templates.datapage import table_data
app_route = Blueprint('route', __name__)

@app_route.route('/')
@app_route.route('/index')
@app_route.route('/index.php')
@app_route.route('/index.htm')
@app_route.route('/index.html')
def index():
  "Функция отображения индексной страницы"
  return render_template('index.html')

@app_route.route('/data')
@app_route.route('/data.php')
@app_route.route('/data.htm')
@app_route.route('/data.html')
def data():
  "Функция отображения страницы 'дынне'"
  # data = sql_execute("SELECT tp.checkingPeer, tp.checkedPeer, tp.pointsamount FROM TransferredPoints;")
  data = table_data()
  return render_template('data.html', data=data)

@app_route.route('/operations')
@app_route.route('/operations.php')
@app_route.route('/operations.htm')
@app_route.route('/operations.html')
def operations():
  "Функция отображения страницы 'операции'"
  return render_template('operations.html')

@app_route.route('/about')
@app_route.route('/about.php')
@app_route.route('/about.htm')
@app_route.route('/about.html')
def about():
  "Функция отображения страницы 'о нас'"
  return render_template('about.html')


from flask import Blueprint, render_template, request, redirect, url_for
from model.templates.datapage import *
import sys
from model.database.sql_query import fetchall_query

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
  "Функция отображения страницы 'данные'"
  tables = all_tables()
  return render_template('data.html', tables=tables)


@app_route.route('/data/<path:table_name>')
def table(table_name):
  "Функция отображения страницы таблицы"
  columns = table_titles(table_name)
  rows = table_rows(table_name)
  name = table_name

  return render_template('table.html', rows=rows, columns=columns, name=name)

@app_route.route('/delete_table', methods=['GET', 'POST'])
def delete_table():
    if request.method == 'POST':
        table_name = request.form['table_name']
        drop_table(table_name)
    return redirect(url_for('route.data'))

@app_route.route('/operations')
@app_route.route('/operations.php')
@app_route.route('/operations.htm')
@app_route.route('/operations.html')
def operations():
  "Функция отображения страницы 'операции'"
  return render_template('operations.html')

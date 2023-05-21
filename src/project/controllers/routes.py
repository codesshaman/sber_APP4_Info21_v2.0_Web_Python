from typing import Union

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
    flash,
    Response,
)
from model.templates.datapage import (
    table_rows,
    table_titles,
    all_tables,
    drop_table,
    save_table,
    import_table,
    delete_row_query,
    insert_row_query,
    update_row_query,
)
from model.templates.operations import (
    custom_query,
    dispaly_descr
)
import sys
import os

app_route = Blueprint("route", __name__)


@app_route.route("/")
@app_route.route("/index")
@app_route.route("/index.php")
@app_route.route("/index.htm")
@app_route.route("/index.html")
def index() -> str:
    """Функция отображения индексной страницы"""
    return render_template("index.html")


@app_route.route("/data")
@app_route.route("/data.php")
@app_route.route("/data.htm")
@app_route.route("/data.html")
def data() -> str:
    """Функция отображения страницы 'данные'"""
    tables = all_tables()
    return render_template("data.html", tables=tables)


@app_route.route("/data/<table_name>", methods=["GET"])
def table(table_name: str) -> str:
    """Функция отображения страницы таблицы"""
    columns = table_titles(table_name)
    rows = table_rows(table_name)
    name = table_name
    return render_template(
        "table.html",
        table_name=table_name,
        rows=rows,
        columns=columns,
        name=name
    )


@app_route.route("/delete_table", methods=["POST"])
def delete_table() -> Response:
    if request.method == "POST":
        table_name = request.form["table_name"]
        drop_table(table_name)
    return redirect(url_for("route.data"))


@app_route.route("/save_table", methods=["POST"])
def download_table() -> Response:
    if request.method == "POST":
        table_name = request.form["table_name"]
        save_table(table_name)
        return send_file(f"/app/data/{table_name}.csv", as_attachment=True)


@app_route.route("/delete_row", methods=["POST"])
def delete_row() -> Response:
    if request.method == "POST":
        table_name = request.form["table_name"]
        row = request.form["row"]
        delete_row_query(table_name, eval(row))
        return redirect(url_for("route.table", table_name=table_name))


@app_route.route("/import_csv", methods=["POST"])
def import_csv() -> Response:
    if request.method == "POST":
        table_name = request.form["table_name"]
        if "file" not in request.files:
            return redirect(url_for("route.table", table_name=table_name))

        file = request.files["file"]

        if not file.filename.endswith(".csv"):
            return redirect(url_for("route.table", table_name=table_name))

        filename = os.path.join("./data/", table_name + ".csv")
        file.save(filename)

        import_table(table_name)
        return redirect(url_for("route.table", table_name=table_name))


@app_route.route("/update_row", methods=["POST"])
def update_row() -> Response:
    table_name = request.form["table_name"]
    try:
        if request.method == "POST":
            old_value = request.form["old_value"]
            new_value = request.form["text"]
            update_row_query(table_name, eval(old_value), eval(new_value))
    except Exception as err:
        print(err, file=sys.stderr)
    return redirect(url_for("route.table", table_name=table_name))


@app_route.route("/insert_row", methods=["POST"])
def insert_row() -> Response:
    table_name = request.form["table_name"]
    if request.method == "POST":
        row = request.form
        insert_row_query(table_name, row)
        flash("File saved.")
        # for k, v in row.items():
        #     print(f"{k}:{v}", file=sys.stderr, sep='#')
    return redirect(url_for("route.table", table_name=table_name))


@app_route.route("/operations/custom_sql", methods=["POST"])
def custom_sql() -> (Union[Response, str]):
    try:
        if request.method == "POST":
            rows = custom_query(request.form["sql"])
            return render_template(
                "table.html",
                table_name="Custom",
                rows=rows,
                columns=list(range(len(rows[0]))),
                name=None,
            )
    except Exception as err:
        print(err, file=sys.stderr)
    return redirect(url_for("route.operations"))


@app_route.route("/operations")
@app_route.route("/operations.php")
@app_route.route("/operations.htm")
@app_route.route("/operations.html")
def operations() -> str:
    """Функция отображения страницы 'операции'"""
    tables = dispaly_descr()
    return render_template("operations.html", tables=tables)

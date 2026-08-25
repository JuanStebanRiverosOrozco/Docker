import os

import pymysql
from flask import Flask


sample = Flask(__name__)

@sample.route("/")
def home():
    try:
        conn = pymysql.connect(
            host=os.environ.get("DB_HOST", "servidor-bd-ejemplo"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", ""),
            database=os.environ.get("DB_NAME", "082_db"),
        )
        conn.close()
        db_status = "Conexión exitosa a la base de datos"
    except Exception as e:
        db_status = f"Error al conectar a la base de datos: {e}"

    return f"<h1>Bienvenido a mi aplicación Flask Ok</h1><p>{db_status}</p> arreglado todo hoy"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=False)  # nosec B104
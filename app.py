import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    # Este valor viene de una "variable de entorno" cargada en Coolify.
    equipo = os.environ.get("NOMBRE_EQUIPO", "equipo1")
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hola desde Coolify</title>
  <style>
    body {{ font-family: sans-serif; max-width: 640px; margin: 4rem auto; padding: 0 1rem; }}
    h1 {{ margin-bottom: .25rem; }}
    .caja {{ background: #eef6ee; border: 1px solid #9c9; padding: 1rem; border-radius: 8px; }}
  </style>
</head>
<body>
  <h1>Hola, {equipo}</h1>
  <p>Si ves esta página, tu proyecto se publicó correctamente en el servidor.</p>
  <div class="caja">
    <p><strong>Lenguaje:</strong> Python (Flask)</p>
    <p><strong>Variable de entorno NOMBRE_EQUIPO:</strong> {equipo}</p>
  </div>
</body>
</html>"""


@app.route("/salud")
def salud():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

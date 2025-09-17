from flask import Flask, jsonify, abort

dias = [
    {"id": 1, "name": "Lunes"},
    {"id": 2, "name": "Martes"},
    {"id": 3, "name": "Miércoles"},
    {"id": 4, "name": "Jueves"},
    {"id": 5, "name": "Viernes"},
    {"id": 6, "name": "Sábado"},
    {"id": 7, "name": "Domingo"},
]

app = Flask(__name__)


@app.route("/", methods=["GET"])
# Método para obtener los días
def get_days():
    return jsonify(dias)


@app.route("/<int:day_id>", methods=["GET"])
def get_day(day_id):
    day = [day for day in dias if day["id"] == day_id]
    if len(day) == 0:
        abort(404)
    return jsonify({"day": day[0]})

@app.route("/<string:day_name>", methods=["GET"])
def get_day_by_name(day_name):
    day = [day for day in dias if day["name"] == day_name]
    if len(day) == 0:
        abort(404)
    return jsonify({"day": day[0]})


@app.route("/", methods=["POST"])
def post_days():
    return jsonify({"success": True}), 201


if __name__ == "__main__":
    app.run(debug=True)

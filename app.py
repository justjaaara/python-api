from flask import Flask, jsonify, abort, request

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

@app.route("/new-day", methods=["POST"])
def post_new_day():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Falta el nombre del día"}), 400

    new_id = dias[-1]['id'] + 1
    new_day = {"id": new_id, "name": data["name"]}
    dias.append(new_day)
    return jsonify({"success": True, "day": new_day}), 201


if __name__ == "__main__":
    app.run(debug=True)

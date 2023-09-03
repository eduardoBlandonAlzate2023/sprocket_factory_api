from app.auth.authentication import authenticate
from app.schemas import sprocket_schema
from flask import request, jsonify
from app import app, db
from app.models.sprocket import Sprocket

@app.route("/sprockets/<int:sprocket_id>", methods=["GET"])
@authenticate
def get_sprocket_by_id(sprocket_id):
    sprocket = Sprocket.query.get_or_404(sprocket_id)
    return jsonify(
        {
            "teeth": sprocket.teeth,
            "pitch_diameter": sprocket.pitch_diameter,
            "outside_diameter": sprocket.outside_diameter,
            "pitch": sprocket.pitch,
        }
    )

@app.route("/sprockets", methods=["POST"])
@authenticate
def create_sprocket():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid data"}), 400
    
    errors = sprocket_schema.SprocketSchema().validate(data)
    if errors:
        return jsonify(errors), 400
    
    sprocket = Sprocket(**data)
    db.session.add(sprocket)
    db.session.commit()
    return jsonify({"message": "Sprocket created successfully"}), 201

@app.route("/sprockets/<int:sprocket_id>", methods=["PUT"])
@authenticate
def update_sprocket(sprocket_id):
    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid data"}), 400
    
    sprocket = Sprocket.query.get_or_404(sprocket_id)
    for key, value in data.items():
        setattr(sprocket, key, value)
    db.session.commit()
    return jsonify({"message": "Sprocket updated successfully"}), 200

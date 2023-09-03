from app.auth.authentication import authenticate
from flask import request, jsonify
from app import app
from app.models.factory import Factory

@app.route("/factories", methods=["GET"])
@authenticate
def get_all_factories():
    factories = Factory.query.all()
    return jsonify([f.chart_data for f in factories])

@app.route("/factories/<int:factory_id>", methods=["GET"])
@authenticate
def get_factory_by_id(factory_id):
    factory = Factory.query.get_or_404(factory_id)
    return jsonify(factory.chart_data)

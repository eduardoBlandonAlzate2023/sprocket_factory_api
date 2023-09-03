import json
from app import app, db
from app.models.factory import Factory
from app.models.sprocket import Sprocket

def seed_data():
    if not Factory.query.first():
        with open("data/seed_factory_data.json", "r") as f:
            factories_data = json.load(f)
        for factory_data in factories_data["factories"]:
            factory = Factory(chart_data=factory_data["factory"]["chart_data"])
            db.session.add(factory)
    if not Sprocket.query.first():
        with open("data/seed_sprocket_types.json", "r") as f:
            sprockets_data = json.load(f)
        for sprocket_data in sprockets_data["sprockets"]:
            sprocket = Sprocket(**sprocket_data)
            db.session.add(sprocket)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_data()
    app.run(debug=True, host="0.0.0.0")

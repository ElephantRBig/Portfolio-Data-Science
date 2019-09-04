 # importing Flask
from flask import Flask, jsonify

# Importing SQL Alchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflecting an existing database into a new model
Base = automap_base()
# reflect the tables 
Base.prepare(engine, reflect = True)
# Save referecnes to each table 
measurement = Base.classes.measurement
station = Base.classes.station

sesssion = Session(engine)


# Creating the app
app = Flask(__name__)

# Creating the route
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate API! <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def query():
    practise = session.query(measurement.date, measurement.prcp).all()

    for row in practise:
        dict = {row[0]:row[1]}
        
        return jsonify[dict]
    


#@app.route("/api/v1.0/stations")

#@app.route("/api/v1.0/tobs")

#@app.route("/api/v1.0/<start>")

#@app.route("/api/v1.0/<start>/<end>")

# Defining the main behaviour 
if __name__ == "__main__":
    app.run(debug = True)
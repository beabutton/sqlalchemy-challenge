# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func



#################################################
# Database Setup
#################################################
#
engine = create_engine('sqlite:///C:/Users/beabutton/Desktop/data_class/homework/10-SQL/Starter_Code/SurfsUp/Resources/hawaii.sqlite')
# reflect an existing database into a new model
base = automap_base()

# reflect the tables
base.prepare(autoload_with = engine)

# Save references to each table
measure = base.classes.measurement
station = base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# latest = (session.query(measure.date).order_by(measure.date.desc()).first())

# latest = list(np.ravel(latest))[0]

# latest = dt.datetime.strptime(latest, '%Y-%m-%d')
# latesty = int(dt.datetime.strftime(latest, '%Y'))
# latestm = int(dt.datetime.strftime(latest, '%m'))
# latestd = int(dt.datetime.strftime(latest, '%d'))

# befyear = dt.date(latesty, latestm, latestd) - dt.timedelta(days = 365)
# befyear = dt.datetime.strftime(befyear, '%y-%m-%d')
def lastyear():
    session = Session(engine)
    recent = session.query(func.max(measure.date)).first()[0]
    first = dt.datetime.strptime(recent, '%Y-%m-%d') - dt.timedelta(days = 365)
    session.close()
    return(first)
#################################################
# Flask Routes
#################################################
@app.route('/')
def home():
    return """
    <h1 style = 'text-align:center'> Kowabunga Welcome to Surf's Up</h1><br/>
    <pre style='text-align:center'>
                    .       .  ~   . ~  -  ~  . = .  ~
                ~        ~  __.---~~_~~_~~_~~_~ ~ ~~_~~~
              .    .     .-'  ` . ~_ = ~ _ =  . ~ .    ~
                       .'  `. ~  -   =      ~  -  _ ~ `
              ~    .  }` =  - _ ~  -  . ~  ` =  ~  _ . ~
                    }`   . ~   =    ~  =  ~   -  ~    - _
          .        }   ~ .__,~O     ` ~ _   ~  ^  ~  -
                 `}` - =    /#/`-'     -   ~   =   ~  _ ~
            ~ .   }   ~ -   |^\   _ ~ _  - ~ -_  =  _
                 }`  _____ /_  /____ - ~ _   ~ _
         aac   }`   `~~~~~~~~~~~~~~~`_ = _ ~ -
       _ _ _ }` `. ~ . - _ = ~. ~ = .   -   =
    </pre>
    <h2 style = 'text-align:center'>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</h2><br/>
    <h3> Routes you can surf on these interwaves are:</h3><br/>
    <a href = '/api/v1.0/precipitation'> Precipitation</a><br/>
    <a href = '/api/v1.0/stations'> Stations</a><br/>
    <a href = '/api/v1.0/tobs'> TOBS (Temp)</a><br/>
    <a href = '/api/v1.0/<start>'> Start Date</a><br/>
    



    <pre style = 'text-align:center'>
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣴⠂⢀⡀⠀⢀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣄⣠⣀⠀⠘⠋⠉⠉⠁⠀⠺⣿⡷⣿⣿⣿⡿⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣛⠛⠉⠀⠀⠀⠀⠺⣷⣦⠀⠀⠀⠙⠛⠉⠀⠀⠈⣿⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣆⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠙⠉⠀⠀⢸⣦⠀⠀⠀⢀⣼⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡆⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣷⠄⠀⠀⠀⠀⠀
⢠⣾⣷⣦⡀⠘⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⢠⣿⣿⣿⡿⠟⠛⠋⠁⣀⣠⣤⣄⣀⠀
⠘⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣾⣶⣿⣿⣿⣿⣿⣿⣟⠘⣿⣷⡀⠀⠀⠘⠿⡿⠉⠀⠀⣀⣴⣾⣿⣿⣿⣿⡿⡂
⠀⠈⠿⢟⣿⣿⣆⠀⠀⠀⠀⢀⣤⣤⣿⣿⣿⣿⣿⣎⠛⢫⣿⣿⣿⣷⡘⢿⣿⣆⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁
⠀⠀⠀⢺⣿⣿⣿⣷⡄⠀⢰⣿⣿⣿⣯⠹⣿⣿⣿⣷⣶⡜⢿⣿⣿⣿⣷⡄⠹⣿⣷⣄⠀⠀⣴⣼⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢻⣿⣿⣿⣦⡘⢿⣿⣿⣿⣃⠉⢿⣿⣿⣿⣿⡌⢻⣝⠻⠿⢃⡀⣿⣿⣿⣷⣶⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣷⣄⠛⣿⣿⣿⣿⣄⠻⣿⣿⣿⣿⡆⠙⠷⠶⠟⢠⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡇⠈⠻⣿⣿⣿⣷⠘⠧⣉⣁⡴⠀⢠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣷⣄⠙⠧⣍⣩⡜⢀⣀⣀⠄⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣷⣦⣄⣀⣤⣾⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠻⠛⠛⠁⠉⠙⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    </pre>
    """
@app.route('/api/v1.0/precipitation')
def prec():
    session = Session(engine)
    prcpdata = session.query(measure.date, measure.prcp).filter(measure.date >= lastyear()).all()
    session.close()

    prcpl = []
    for date, prcp in prcpdata:
        prcpdc = {}
        prcpdc['date'] = date
        prcpdc['prcp'] = prcp
        prcpl.append(prcpdc)
    return jsonify(prcpl)


@app.route('/api/v1.0/stations')
def stat():
    session = Session(engine)
    statdata = session.query(station.station).all()
    session.close()

    allstat = list(np.ravel(statdata))
    return jsonify(allstat)

@app.route('/api/v1.0/tobs')
def tobs():
    actsta = 'USC00519281'
    tobsdatas = session.query(measure.date, measure.tobs).filter(measure.station == actsta).filter(measure.date >= lastyear()).all()
    session.close()

    tobsdb = []
    for date, tobs in tobsdatas:
        tobsdc = {}
        tobsdc['date'] = date
        tobsdc['tobs'] = tobs
        tobsdb.append(tobsdc)
    return jsonify(tobsdb)


#not fully working ran out of time 
@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')
def starend(start = None, end = None):
    session = Session(engine)

    temps = [func.min(measure.tobs), func.avg(measure.tobs), func.max(measure.tobs)]
    if end == None: 
        startdata = session.query(*temps).filter(measure.date >= start).all()
        startdb = list(np.ravel(startdata))
        return jsonify(startdb)
    
    else: 
        enddata = session.query(*temps).filter(measure.date >= start).filter(measure.date <= end).all()
        enddb = list(np.ravel(enddata))
        return jsonify(enddb)
    
    session.close()

if __name__ == '__main__':
    app.run(debug = True)



#
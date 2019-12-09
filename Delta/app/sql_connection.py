import sqlalchemy
from sqlalchemy.orm import sessionmaker
import pandas as pd 
from app import app
from flask import jsonify, request
import json
import csv


@app.route('/firstpage')
def firstpage():
	origin = request.args.get('origin')
	#print(origin)
	destination = request.args.get('dest')
	#print(destination)
	df = pd.read_csv('flights_data.csv', names=['id','created_at','updated_at','flight_identifier','flt_num',
	'scheduled_origin_gate','scheduled_destination_gate','out_gmt','in_gmt','off_gmt','on_gmt','destination','origin',
	'destination_full_name','origin_full_name'])
	df1=df[(df['origin']==origin) & (df['destination']==destination)]
	jsonData = df1.to_json(orient="records")
	return jsonData 
	# return {'error':False}
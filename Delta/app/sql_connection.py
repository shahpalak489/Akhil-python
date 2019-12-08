import sqlalchemy
from sqlalchemy.orm import sessionmaker
import pandas as pd 
from app import app
from flask import jsonify, request
import json
import csv


@app.route('/firstpage')
def firstpage():
	df = pd.read_csv('flights_data.csv', names=['id','created_at','updated_at','flight_identifier','flt_num',
	'scheduled_origin_gate','scheduled_destination_gate','out_gmt','in_gmt','off_gmt','on_gmt','destination','origin',
	'destination_full_name','origin_full_name'])
	df1=df[df['id']=='291480']
	jsonData = df1.to_json(orient="records")
	return jsonData 
	
	# # name = request.args.get("firstname")
	# engine = sqlalchemy.create_engine('mssql+pyodbc://LAPTOP-6ESE1JO3/master?driver=SQL+Server+Native+Client+11.0')
	# connection = engine.connect()
	# metadata = sqlalchemy.MetaData()
	# sqlQ = sqlalchemy.Table('userinfo', metadata, autoload=True, autoload_with=engine) # print(sqlQ.columns.keys())

	# qAns = sqlalchemy.select([sqlQ])  ### select q
	# ResultProxy = connection.execute(qAns)
	# ResultSet = ResultProxy.fetchall()
	# df = pd.DataFrame(ResultSet, columns=['firstname', 'lastname', 'ID'])
	# # df = df[df['firstname']==name]
	# print(df)
	# jsonData = df.to_json(orient="records")
	# return jsonData 
	return {'error':False}
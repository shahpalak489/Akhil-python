import csv
import pandas as pd

df = pd.read_csv('flights_data.csv', names=['id','created_at','updated_at','flight_identifier','flt_num',
	'scheduled_origin_gate','scheduled_destination_gate','out_gmt','in_gmt','off_gmt','on_gmt','destination','origin',
	'destination_full_name','origin_full_name'])
df1=df[df['id']=='291480']
return df1


def firstpage():
	with open('flights_data.csv') as csvfile:
		readCSV = csv.reader(csvfile,delimiter=',')
		for row in readCSV:
			if row[11]=='AUH' and row[12]=='FRA' :
				#print(row)
				df=pd.DataFrame(row,columns=['zero'])
				#df=pd.DataFrame(row,columns=['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen'])
				print(df)
				jsonData = df.to_json(orient="records")
	return jsonData 
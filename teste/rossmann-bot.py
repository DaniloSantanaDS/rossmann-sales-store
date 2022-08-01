import json
import requests
import pandas as pd
import os

from flask import Flask, request, Response

# constants
TOKEN = '5490394066:AAF46mzahAGMRLkODGHv-9tfp75HTZ8i_e4'

# Info about the bot
#https://api.telegram.org/bot5490394066:AAF46mzahAGMRLkODGHv-9tfp75HTZ8i_e4/getMe

#get updates
#https://api.telegram.org/bot5490394066:AAF46mzahAGMRLkODGHv-9tfp75HTZ8i_e4/getUpdate

#send message 
#https://api.telegram.org/bot5490394066:AAF46mzahAGMRLkODGHv-9tfp75HTZ8i_e4/sendMessage?chat_id=671687097&text=Hi Danilo, I am doing good, tks!

#webhook

#https://api.telegram.org/bot5490394066:AAF46mzahAGMRLkODGHv-9tfp75HTZ8i_e4/setWebhook?url=https://rossmann-bot-original.herokuapp.com/

def send_message(chat_id, text):
	url = 'https://api.telegram.org/bot{}/'.format(TOKEN)
	url = url + 'sendMessage?chat_id={}'.format(chat_id)
	
	r = requests.post(url, json={'text': text})
	print('Status Code {}'.format(r.status_code))
	
	return None

def load_dataset(store_id):
	# loading dataset
	df10 = pd.read_csv('test.csv')
	df_store_raw = pd.read_csv('store.csv')

	df_test = pd.merge(df10, df_store_raw, how='left', on='Store')

	#choose store for predction

	df_test = df_test[df_test['Store'] == store_id]
	
	if not df_test.empty:

		# remove closed day
		df_test = df_test[df_test['Open'] != 0]
		df_test = df_test[~df_test['Open'].isnull()]
		df_test = df_test.drop('Id', axis=1)

		# convert Dataframa to json

		data = json.dumps(df_test.to_dict(orient='records'))
	else:
		data = 'error'
		
	return data
	
def predict(data):

	# api call
	url = 'https://rossmann-model-danilo.herokuapp.com/rossmann/predict'
	header = {'Content-type':'application/json'}
	data = data

	r = requests.post(url, data=data, headers=header)
	print('Status Code {}'.format(r.status_code))

	# convert json to dataframe
	d1 = pd.DataFrame(r.json(), columns=r.json()[0].keys())
	
	return d1
# api initialize
	
app = Flask(__name__)
def parse_message(message):
	chat_id = message['message']['chat']['id']
	store_id = message['message']['text']
	
	store_id = store_id.replace('/', '')
	
	try:
		store_id = int(store_id)
	
	except ValueError:
		store_id = 'error'
		
		
	return chat_id, store_id
	
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		message = request.get_json()
		
		chat_id, store_id = parse_message(message)
		
		if store_id != 'error':
			#loading data
			data = load_dataset(store_id)
			
			if data != 'error':
				#prediction
				d1 = predict(data)
				#calculation
				d2 = d1[['store', 'prediction']].groupby('store').sum().reset_index()

				msg = 'Store number {} will sell R${:,.2f} in the next 6 weeks'.format(
					   d2['store'].values[0],
					   d2['prediction'].values[0])
					   
				send_message(chat_id, msg)	
				return Response('OK', status=200)		
			#send message
			else:
				send_message(chat_id, 'Store Not Available')
				return Response('OK', status=200)		
		else:
			send_message(chat_id, 'Store Id is Wrong')
			return Response('OK', status=200)		
	else:
		return '<h1> Rossmann Telegram Bot </h1>'

if __name__ == '__main__':
	port = os.environ.get('PORT', 5000)
	app.run(host='0.0.0.0', port=port)

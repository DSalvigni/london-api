# importing the requests library (Written by DSalvigni)
import requests 

# api-endpoint (id Found via postman)
# Bikepoint found via POSTMAN
# BikePointsID -> https://api.tfl.gov.uk/BikePoint?app_id={{app_id}}&app_key={{app_key}} to find the list of bike points (In our Case "Bank of England")
# In our case the id is the 340.
id = "BikePoints_340"
# URL available in the set of GET API request under #insert APP id from https://api.tfl.gov.uk
URL = "https://api.tfl.gov.uk/BikePoint/"+id
#insert APP id from https://api.tfl.gov.uk
app_id = "---" 
#insert APP key from https://api.tfl.gov.uk
app_key = "---"

  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'app_id':app_id, 'app_key':app_key} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

# I am happy to print if the response is OK otherwise I print the error
if (r.status_code == 200):
	data = r.json()
	print('API RESPONSE -> 200')
	print('Last TS -> '+data['additionalProperties'][6]['modified'])
	for i in range(len(data['additionalProperties'])):
		print(data['additionalProperties'][i]['key']+' -> '+data['additionalProperties'][i]['value'])
else:
	print('ERROR -> '+r.status_code )

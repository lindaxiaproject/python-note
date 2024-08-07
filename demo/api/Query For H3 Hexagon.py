import requests



if __name__ == '__main__':
	url = "https://vanitysoft-boundaries-io-v1.p.rapidapi.com/rest/v1/public/boundary/h3/zipcode/location/boundary"

	querystring = {"latitude": "41.81623879474455", "longitude": "-88.11097032902904", "resolution": "10"}

	headers = {
		"x-rapidapi-key": "132b3ed5f2msh853aa69ccad0031p159665jsn733833fd522f",
		"x-rapidapi-host": "financial-modeling-prep.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	print(response.json())
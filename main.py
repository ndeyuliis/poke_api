import requests

def get_data():
    response = requests.get('https://pokeapi.co/api/v2/pokemon')
    print(response.status_code, response.content)

if __name__=="__main__":
    get_data()
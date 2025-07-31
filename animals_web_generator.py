import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

name = ('fish')
API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)

def main():
    response = requests.get(API_URL, headers={'X-Api-Key':API_KEY})
    if response.status_code == requests.codes.ok:
        print(response.json())
        print(len(response.json()))
    else:
        print("Error:", response.status_code, response.json())


if __name__ == '__main__':
    main()
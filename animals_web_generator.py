import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_info_from_api(name):
    """
    Get the information from the animals API as JSON
    """
    API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(API_URL, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return "Error:", response.status_code, response.json()


def load_html(file_path):
    """Load the content of an HTML file"""

    with open(file_path, "r", encoding='utf-8') as handle:
        return handle.read()


def save_html(file_path, content):
    """Save the content to an HTML file"""

    with open(file_path, "w", encoding='utf-8') as handle:
        return handle.write(content)


def collect_animal_data(data: dict) -> str:
    """
    Reads the content of  a single animals, collects its data
    :return: a string for an HTML card with the gathered information
    """

    output = ""
    output += '<li class="cards__item">'
    if "name" in data:
        output += '<div class="card__title">' + f'{data["name"]}</div>\n'
    if "scientific_name" in data["taxonomy"]:
        output += (f'<dic class="card_subtitle"><i> '
                   f'{data["taxonomy"]["scientific_name"]}</i></div>\n')
    output += '<p class ="card__text">'
    output += '<ul>'
    if "diet" in data["characteristics"]:
        output += ('<li><strong>Diet:</strong>' +
                   f' {data["characteristics"]["diet"]}</li>\n')
    if "locations" in data:
        output += ('<li><strong>Location:</strong>' +
                   f' {data["locations"][0]}</li>\n')
    if "type" in data["characteristics"]:
        output += ('<li><strong>Type:</strong>' +
                   f' {data["characteristics"]["type"]}</li>\n')
    output += '</ul>'
    output += '</p>'
    if "slogan" in data["characteristics"]:
        output += (f'<div class="slogan">'
                   f'<cite>{data["characteristics"]["slogan"]}'
                   f'</cite></div>\n')
    output += '</li>'
    return output


def main():
    """
    Read the content with the api and read the html template
    Get user input which animal they want to see
    Gather all data
    Gather data about the animals
    Create a new html file
    """

    while True:
        name = input("Enter a name of an animal:")
        animals_data = get_info_from_api(name)
        if animals_data:
            break
        else:
            print("Couldn't find any data, please try another input.")

    html_content = load_html("animals_template.html")

    output = ""
    for data in animals_data:
        output += collect_animal_data(data)

    replace_info = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
    save_html("animals.html", replace_info)
    print("Website was successfully generated to the file animals.html.")

if __name__ == '__main__':
    main()
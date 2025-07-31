import data_fetcher as df


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


def handle_output(html_content, animals_data, name):
    """
    Handle the output whether data was found or not.
    Return the info to save in the html.
    """

    if not animals_data:
        output = ('<div class="animal__not__found">'
                  + f' The animal {name} was not found. '
                    f'Try another! </div>\n')
        replace_info = html_content.replace("__REPLACE_ANIMALS_INFO__",
                                            output)

    else:
        output = ""
        for data in animals_data:
            output += collect_animal_data(data)
        replace_info = html_content.replace("__REPLACE_ANIMALS_INFO__",
                                            output)

    return replace_info


def main():
    """
    Read the content with the api and read the html template
    Get user input which animal they want to see
    Create a new html file with output data
    """

    html_content = load_html("animals_template.html")

    name = input("Enter a name of an animal:")
    animals_data = df.get_info_from_api(name)

    replace_info = handle_output(html_content,animals_data, name)

    save_html("animals.html", replace_info)
    print("Website was successfully generated to the file animals.html.")


if __name__ == '__main__':
    main()
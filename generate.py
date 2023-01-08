import json
import os
import requests


def main():
    if not os.path.exists("_site"):
        os.makedirs("_site")


    mentors = read_json_files('mentors')
    with open("_site/index.html", "w") as fh:
        fh.write("<h1>OSDC 2023.01 Public</h1>\n")
        fh.write("<h2>Mentors</h2>\n")
        fh.write("<ul>\n")
        for mentor in mentors:
            fh.write(f"<li>{mentor['name']}<br>\n")
            fh.write(f'''GitHub: <a href="https://github.com/{mentor['github']}">{mentor['github']}</a><br>\n''')
            fh.write(f"</li>\n")
        fh.write("</ul>\n")

def read_json_files(folder):
    people = []
    for filename in os.listdir(folder):
        if filename == '.gitkeep':
            continue
        elif not filename.endswith('.json'):
           raise JsonError("file does not end with .json")
        with open(os.path.join(folder, filename)) as fh:
            person = json.load(fh)
        people.append(person)
    return people

def check_url_for_participant(url: str) -> bool:
    # params: URL of the participant for github / linkedin.
    # Linkedin does not allow to get requests from their website:
    # https://stackoverflow.com/questions/18704429/python-requests-library-added-an-additional-header-accept-encoding-identity
    headers = {'Accept-Encoding': 'gzip, deflate'}
    r = requests.head(url, headers=headers)
    return r.status_code == requests.codes.ok

if __name__ == "__main__":
    main()

class JsonError(Exception):
    pass

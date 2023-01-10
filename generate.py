import json
import os
import pathlib
from jinja2 import Environment, FileSystemLoader
import requests

def read_course_json():
    with pathlib.Path(__file__).parent.joinpath('course.json').open() as fh:
        return json.load(fh)


def main():
    if not os.path.exists("_site"):
        os.makedirs("_site")

    mentors = read_json_files('mentors')
    participants = read_json_files('participants')
    course = read_course_json()

    template = 'index.html'
    templates_dir = pathlib.Path(__file__).parent.joinpath('templates')
    env = Environment(loader=FileSystemLoader(templates_dir), autoescape=True)
    html_template = env.get_template(template)
    html_content = html_template.render(
        mentors = mentors,
        participants = participants,
        course = course,
        title = course['title'],
    )
    with open('_site/index.html', 'w') as fh:
        fh.write(html_content)



def read_json_files(folder):
    people = []
    for filename in os.listdir(folder):
        if filename == '.gitkeep':
            continue
        if not filename.endswith('.json'):
           raise JsonError("file does not end with .json")
        if filename != filename.lower():
            raise Exception(f"filename {filename} should be all lower-case")
        with open(os.path.join(folder, filename)) as fh:
            person = json.load(fh)
        people.append(person)
    return people

def check_github_acc_for_participant(url: str) -> bool:
    # params: URL of the participant for github.
    headers = {'Accept-Encoding': 'gzip, deflate'}
    r = requests.head(url, headers=headers)
    return r.status_code == requests.codes.ok

if __name__ == "__main__":
    main()

class JsonError(Exception):
    pass

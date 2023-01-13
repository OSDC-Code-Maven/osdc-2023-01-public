import json
import os
import pathlib
from jinja2 import Environment, FileSystemLoader
import requests
import forem
import github
import time
#import datetime

def read_course_json():
    with pathlib.Path(__file__).parent.joinpath('course.json').open() as fh:
        return json.load(fh)

def update_devto_posts(people):
    for person in people:
        if 'posts' not in person:
            continue
        for page in person['posts']:
            #print(page['url'])
            page['details'] = forem.fetch(page['url'])
            time.sleep(0.2) # self imposed rate limit

def update_github_data(people):
    for person in people:
        person['gh'] = github.get_user_info(person['github'])
        time.sleep(0.2) # self imposed rate limit

def render(template, filename, **args):
    templates_dir = pathlib.Path(__file__).parent.joinpath('templates')
    env = Environment(loader=FileSystemLoader(templates_dir), autoescape=True)
    html_template = env.get_template(template)
    html_content = html_template.render(**args)
    with open(filename, 'w') as fh:
        fh.write(html_content)


def main():
    mentors = read_json_files('mentors')
    participants = read_json_files('participants')
    course = read_course_json()

    prod = os.environ.get('GITHUB_ACTIONS')
    outdir = "_site"
    if not prod:
        outdir = os.path.join(outdir, course['id'])
    os.makedirs(outdir, exist_ok=True)
    os.makedirs(os.path.join(outdir, "p"), exist_ok=True)
    if not prod:
        with open(os.path.join('_site', 'index.html'), 'w') as fh:
            fh.write(f'<a href="{course["id"]}/">{course["id"]}</a>')

    update_devto_posts(mentors)
    update_devto_posts(participants)
    update_github_data(mentors)
    update_github_data(participants)

    posts = []
    for person in mentors + participants:
        if 'posts' in person:
            for post in person['posts']:
                if post['details']:
                    post['details']['author'] = person['name']
                    posts.append(post['details'])
                else:
                    posts.append({
                        'url': post['url'],
                        'title': post['title'],
                        'description': '',
                        'author': person['name'],
                        'published_at': post['published_at'],
                    })
    posts.sort(key=lambda post: post['published_at'], reverse=True)

    participants.sort(key=lambda person: person['name'])


    for person in mentors + participants:
        render('person.html', os.path.join(outdir, 'p', f'{person["github"].lower()}.html'),
            title = person['name'],
            mentors = mentors,
            participants = participants,
            course = course,
            person = person,
        )

    render('index.html', os.path.join(outdir, 'index.html'),
        mentors = mentors,
        participants = participants,
        course = course,
        title = course['title'],
    )
    render('articles.html', os.path.join(outdir, 'articles.html'),
        mentors = mentors,
        participants = participants,
        articles = posts,
        course = course,
        title = 'Articles',
    )



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

        if 'github' not in person:
            raise Exception(f"github field is missing from {filename}")
        if person['github'].lower() != filename[:-5]:
            raise Exception(f"value of github fields '{person['github']}' is not the same as the filename '{filename}'")


        people.append(person)
    return people

def check_github_acc_for_participant(url: str) -> bool:
    print(url)
    # params: URL of the participant for github.
    headers = {'Accept-Encoding': 'gzip, deflate'}
    r = requests.head(url, headers=headers)
    return r.status_code == requests.codes.ok

if __name__ == "__main__":
    main()

class JsonError(Exception):
    pass

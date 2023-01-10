import re

from generate import read_json_files
from generate import check_github_acc_for_participant

GITHUB_URL: str = "https://github.com/"
GITLAB_URL: str = "https://gitlab.com/"

VALID_FIELDS = ['name', 'linkedin', 'github', 'gitlab', 'devto', 'posts']

def test_json():
    for folder in ['mentors', 'participants']:
        people = read_json_files(folder)
        for person in people:
            for field in person.keys():
                assert field == field.lower()
                assert field in VALID_FIELDS
                assert person[field] != "", f"field '{field}' in file '{person['github']}.json' is empty"
                for field in ['linkedin', 'github', 'gitlab', 'devto']:
                    if field in person:
                        if person['github'] == 'ilayni' and field == 'linkedin':
                            continue
                        match = re.search(r'^[a-zA-Z0-9-\.]+$', person[field])
                        assert match, f"Invalid format for '{field}'='{person[field]}' in file '{person['github']}.json'"

            assert 'name' in person

            assert 'github' in person

def test_urls():
    for folder in ['mentors', 'participants']:
        people = read_json_files(folder)
        for person in people:
            assert check_github_acc_for_participant(GITHUB_URL + person['github']), f"Checking {GITHUB_URL + person['github']}"
            if 'gitlab' in person:
                assert check_github_acc_for_participant(GITLAB_URL + person['gitlab']), f"Checking {GITLAB_URL + person['gitlab']} for '{person['github']}.json'"


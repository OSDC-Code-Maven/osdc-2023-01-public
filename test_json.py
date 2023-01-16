import re

from generate import read_json_files


VALID_FIELDS = ['name', 'linkedin', 'github', 'gitlab', 'devto', 'posts']
REQURED_FIELD = ['name', 'github']

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
                        match = re.search(r'^[a-zA-Z0-9-.]+$', person[field])
                        assert match, f"Invalid format for '{field}'='{person[field]}' in file '{person['github']}.json'"
            if 'posts' in person:
                assert person['posts'].__class__.__name__ == 'list'
                for post in person['posts']:
                    if post['url'].startswith('https://dev.to/'):
                        assert list(post.keys()) == ['url']
                    else:
                        assert sorted(post.keys()) == ['published_at', 'title', 'url']

            for field in REQURED_FIELD:
                assert field in person


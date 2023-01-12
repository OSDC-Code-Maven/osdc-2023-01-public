import re

from generate import read_json_files


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
                        match = re.search(r'^[a-zA-Z0-9-.]+$', person[field])
                        assert match, f"Invalid format for '{field}'='{person[field]}' in file '{person['github']}.json'"
            if 'posts' in person:
                assert person['posts'].__class__.__name__ == 'list'
                for post in person['posts']:
                    assert sorted(post.keys()) == ['title', 'url']

            assert 'name' in person

            assert 'github' in person


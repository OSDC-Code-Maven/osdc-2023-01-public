from generate import read_json_files
from generate import check_url_for_participant

GITHUB_URL: str = "https://github.com/"

def test_json():
    for folder in ['participants', 'mentors']:
        people = read_json_files(folder)
        for person in people:
            assert 'name' in person
            assert 'linkedin' in person
            assert 'github' in person
            assert check_url_for_participant(GITHUB_URL + person['github']) == True



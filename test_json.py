from generate import read_json_files
from generate import check_github_acc_for_participant

GITHUB_URL: str = "https://github.com/"

def test_json():
    for folder in ['mentors', 'participants']:
        people = read_json_files(folder)
        for person in people:
            for field in person.keys():
                assert field == field.lower()
            assert 'name' in person
            assert 'github' in person
            assert check_github_acc_for_participant(GITHUB_URL + person['github']), f"Checking {GITHUB_URL + person['github']}"


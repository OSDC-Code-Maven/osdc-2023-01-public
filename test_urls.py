from generate import read_json_files
from generate import check_github_acc_for_participant

GITHUB_URL: str = "https://github.com/"
GITLAB_URL: str = "https://gitlab.com/"


def test_urls():
    for folder in ['mentors', 'participants']:
        people = read_json_files(folder)
        for person in people:
            assert check_github_acc_for_participant(GITHUB_URL + person['github']), f"Checking {GITHUB_URL + person['github']}"
            if 'gitlab' in person:
                assert check_github_acc_for_participant(GITLAB_URL + person['gitlab']), f"Checking {GITLAB_URL + person['gitlab']} for '{person['github']}.json'"


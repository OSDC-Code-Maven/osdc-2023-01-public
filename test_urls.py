from generate import read_json_files
from generate import check_github_acc_for_participant

GITHUB_URL: str = "https://github.com/"
GITLAB_URL: str = "https://gitlab.com/"
LINKEDIN_URL: str = "https://www.linkedin.com/in/"


def test_urls():
    for folder in ['mentors', 'participants']:
        people = read_json_files(folder)
        for person in people:
            assert check_github_acc_for_participant(GITHUB_URL + person['github']), f"Checking {GITHUB_URL + person['github']}"
            if 'gitlab' in person:
                assert check_github_acc_for_participant(GITLAB_URL + person['gitlab']), f"Checking {GITLAB_URL + person['gitlab']} for '{person['github']}.json'"

            #if 'linkedin' in person:
            #    assert check_github_acc_for_participant(LINKEDIN_URL + person['linkedin'] + "/"), f"Checking {LINKEDIN_URL + person['linkedin']} for '{person['github']}.json'"
            # LinkedIn seem to respond with an HTTP 999 status code when accessing with curl or requests. We might change the User-Agent to fake a browser, but I am not sure it is worth the effort.
            # Maybe there is an API request to check if that user exists.

            if 'posts' in person:
                for post in person['posts']:
                    assert check_github_acc_for_participant(post['url']), f"Checking {post['url']} for '{person['github']}.json'"


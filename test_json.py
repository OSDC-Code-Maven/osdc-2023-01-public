from generate import read_json_files
<<<<<<< HEAD
from generate import check_github_acc_for_participant
=======
from generate import check_url_for_participant
>>>>>>> 8c2635361e04be06ed4a00913080c2abc4c043cf

GITHUB_URL: str = "https://github.com/"

def test_json():
    for folder in ['participants', 'mentors']:
        people = read_json_files(folder)
        for person in people:
            assert 'name' in person
<<<<<<< HEAD
            assert 'github' in person
            assert check_github_acc_for_participant(GITHUB_URL + person['github']) == True
=======
            assert 'linkedin' in person
            assert 'github' in person
            assert check_url_for_participant(GITHUB_URL + person['github']) == True


>>>>>>> 8c2635361e04be06ed4a00913080c2abc4c043cf

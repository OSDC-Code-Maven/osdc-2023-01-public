from generate import read_json_files
from generate import check_url_for_participant

def test_json():
    for folder in ['participants', 'mentors']:
        people = read_json_files(folder)
        for person in people:
            assert 'name' in person
            assert 'linkedin' in person
            assert 'github' in person
            assert True in check_url_for_participant(person['linkedin'])
            assert True in check_url_for_participant(person['github'])



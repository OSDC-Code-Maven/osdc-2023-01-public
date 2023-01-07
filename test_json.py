from generate import read_json_files

def test_json():
    for folder in ['participants', 'mentors']:
        people = read_json_files(folder)
        for person in people:
            assert 'name' in person



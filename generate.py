import json
import os


def main():
    if not os.path.exists("_site"):
        os.makedirs("_site")


    mentors = read_json_files('mentors')
    with open("_site/index.html", "w") as fh:
        fh.write("<h1>OSDC Skeleton</h1>\n")
        fh.write("<h2>Mentors</h2>\n")
        fh.write("<ul>\n")
        for mentor in mentors:
            fh.write(f"<li>{mentor['name']}<br>\n")
            fh.write(f'''GitHub: <a href="https://github.com/{mentor['github']}">{mentor['github']}</a><br>\n''')
            fh.write(f"</li>\n")
        fh.write("</ul>\n")

def read_json_files(folder):
    people = []
    for filename in os.listdir(folder):
        if filename == '.gitkeep':
            continue
        #print(filename)
        with open(os.path.join(folder, filename)) as fh:
            person = json.load(fh)
        people.append(person)
    return people

if __name__ == "__main__":
    main()

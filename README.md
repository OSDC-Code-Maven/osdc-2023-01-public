# Open Sorce Development Course

https://osdc.code-maven.com/osdc-2023-01-public/

* Start day: 2023.01.08

## TOC

* [Session 1 - Welcome - Version Control - Journal - Slack](#session-1---welcome---version-control---journal---slack)
* [Assignment 1](#assignment-1)
* [Session 2 - Create GitHub Pages using the GitHub UI, Markdown](#session-2---create-github-pages-using-the-github-ui-markdown)
* [Assignment 2](#assignment-2)
* [Session 3 - git client](#session-3---git-client)
* [Session 4 - next week](#session-4---next-week)

## Session 1 - Welcome - Version Control - Journal - Slack

* Welcome
    * overview of the [course](https://osdc.code-maven.com/)
        * git
        * GitHub
        * (GitLab)
        * Markdown
        * Docker
        * Testing
        * Static analysis
        * Communication
        * Slack
    * a little about myself
        * Self employed
        * Training
        * Introducing testing, CI etc.
    * If you'd like to send me an email reply to the one I sent you. Keep the subject line. Remove the irrelevant content.
      Without this it is **very** difficult for me to associate all the emails with the different courses I teach.
    * Assignments
        * Will be in some public GitHub or GitLab repositories
        * At the end of each assignment you'll write a report - a blog post / journal entry.
        * You will add it to your personal JSON file and send a Pull-Request with the change. (We'll learn these soon)
    * The more you participate, the more you learn in this course.
    * The more effort you put in this course, the more you will gain.
        * Ask questions!
        * Try to help others! The more you help others the more you will learn.
    * Grades: (if relevant) are based on the work done during the course. There is no end-project or exam at the end.

* Version Control
    * Why use version control?
    * Wikipedia and the verion control there. Recommended to watch:
        * [How to edit wikipedia](https://code-maven.com/edit-wikipedia)
        * [How to edit wikipedia (in Hebrew)](https://he.code-maven.com/edit-wikipedia)
        * [Como editar una página en Wikipedia](https://es.code-maven.com/editar-wikipedia)

* [GitHub](https://github.com/): process of contributing to an Open Source project using the GitHub web site. Editing and sending a Pull-Request. Use a the `cm-demo` user to make a change in the README of this repository and then to add the json file. Show how the CI fails when we add an incorrectly formatted file.
* What is [JSON](https://www.json.org/)?

* Show the Git repository of the project and the web site generated from it.

* [Video](https://youtu.be/GFNQVWYCeb8)

* After the video recording also mentioned https://kantoniko.com/
* [issues](https://github.com/kantoniko/ladino-diksionaryo-code/issues)

### Assignment 1

* You will have to publish a journal of your process. You can use any blogging platform, but let me suggest a few:
    * [DEV](https://dev.to/) - shared blogging platform. See [my account](https://dev.to/szabgab/)
    * [Hashnode](https://hashnode.com/) - shared blogging platform with individual address. See [my side](https://hash.code-maven.com/)
    * [Wordpress](https://wordpress.com/) - individual platform.
    * [Wix](https://www.wix.com/) - more like a web-site builder than a blogging platform.
* Create an account on the blogging platform you selected. (if you already have one, you can use that)
* Create an account on [GitHub](https://github.com/) (if you already have one, use that)
* Create an account on [GitLab](https://gitlab.com/) (if you already have one, use that)
* Add a picture to all these accounts. It is preferably a picture of you, but it can be a drawing of you, or some other avatar you might want to use.
* Send a pull-request to the GitHub repository of the course adding a JSON file. The name of the file should be your GitHub username and it should include key-value pairs as in the example. (The `posts` will be an empty list.) Check the result of GitHub Actions.
* Join the Slack workspace (I send invitations to everyone to their email address.) and say hi.
* Write a blog post about the course. In your post link to your GitHub and GitLab accounts and to your Pull-Request. If you encountered any issue, write about that and how you solved it. If you use an avatar instead of your own picture, describe how you created the avatar.
* In the blog post tell us a bit about your background.
    * What programming language(s) you use?
    * Which interesting 3rd-party libraries do you use? You can mention big ones, but it is probably more interesting if you mention more esoteric ones.
    * Include links to the home-page of each project and the GitHub/GitLab repository of each project.
    * What would you like to accomplish in the course?
    * Which open source projects would you like to contribute to.
* Update your Pull-request adding the URL to the blog post to the `posts` field in the json file.

* There are 3 GitHub repositories with lists of GitHub organization published by [higher education institutions](https://github.com/szabgab/open-source-by-higher-education), [governments](https://github.com/szabgab/open-source-by-government), and [corporations](https://github.com/szabgab/open-source-by-corporations). Find at least 5 more organizations that share some of their code using an open source license in GitHub or GitLab. An organization can be a corporation, a university, a college, a research institute, or a government. (e.g. find a list of universities and use the search feature of GitHub to find **organizations** that belong to the institute).

### Comments

* The first sessions should be longer. Maybe two parts of 45 minutes and I should cover a number of topics that were now postponed to the 2nd session

## Session 2 - Create GitHub Pages using the GitHub UI, Markdown

* Show the results so far.
    * Our web site
    * Some of the blog posts
    * Missing project links,
    * Missin PRs for the data collection projects

* Remind everyone to check the results of the CI and if they don't understand the meaning ask it on the Slack channel.
    * If the CI fails, fix it in the same branch. That will update the PR. Do NOT start a new branch.

* Why is contributing to Open Source important?
    * You received a gift, you give a gift.
    * Your code will be checked by others as well.
    * You get credit in the open source world and you can also show to your (future) employers.
    * These days we like it or not our "brand" has value.
    * You get a better product next time you use it (at the same organization or elsewhere).
    * You will be able to easily upgrade to the new version of this project.
* Why blogging about your process is important?
    * improves skills
    * helps clarify thoughts
    * explaining things to others always helps
    * you will be able to look back
    * Build your personal "brand".

* Show blogging platform
    * [DEV](https://dev.to/) - See [my account](https://dev.to/szabgab/)
    * [Hashnode](https://hashnode.com/) - See [my side](https://hash.code-maven.com/)

* Version Control
    * Show the repo of [Flask](https://github.com/pallets/flask):
        * commits, committers, sha
        * diffs
        * show blame of the README file
        * Comment on a commit
        * Open issue: on our  project, on flask there are templates in th

* [HTML - Hyper Text Markup Language](https://en.wikipedia.org/wiki/HTML)
    * just view source in a browser

* [Markdown](https://en.wikipedia.org/wiki/Markdown).
    * Subtitle
    * Bullet points
    * Links
    * Bold

* We mentioned **static website generators**
    * By deafult GitHub Pages used [Jekyll](https://jekyllrb.com/)
    * There is also [Hugo](https://gohugo.io/) we could use. The [Hugo Academic Theme](https://academic-demo.netlify.app/) was mentioned.
    * Our own web site is generated by a home-made site generator that also collects data.

* Show how to create GitHub pages for the user `username.github.io` first using only the GitHub web site.
    * Show URL that does http://cm-demo.github.io/
    * Create repository with README file https://github.com/cm-demo/cm-demo.github.io
    * Create docs/index.md  with Hello World
    * Configure Pages to be served from the docs/ folder
    * See the URL now shows the new page.
* [GitHub flavored Markdown](https://github.github.com/gfm/) that can be used in Markdown files and elsewhere on GitHub.

* [Video 2.1](https://youtu.be/m05n94cxdDI)
* [Video 2.2](https://youtu.be/oJfMSgotdxM)


### Assignment 2

* Create a web site using GitHub pages with Markdown. At first using the interface on the website of GitHub:
    * Create your own GitHub repository  `username.github.io`.
    * Create the `docs` folder and in the `docs` folder create a file called `index.md`.
    * Include links to your GitHub and GitLab repositories.
    * Include links to your blog and to the course at https://osdc.code-maven.com/ .
    * Include a picture of you (or if you prefer not to have your picture then a picture you took of something nice.) Describe the source of that picture. Bevare of reusing images you found on the Internet. We don't want you to infringe on the copyright of someone else.
* Add your CV in Markdown
    * Create a new file called docs/cv.md
    * Start writing your CV there.
* In a blog post describe your experience. Include a link to your new GitHub pages site.
* Link from your new web GitHub pages based web-site to your blogging account and the article you wrote.
* Mention all the people from the course whom you know and link to their journal.

* Submit by adding the link of your new blog post to your personal JSON file in the project and adding a field called "github_page" to your personal JSON file with a value of "true". See the example of szabgab.json if unclear how.

## Session 3 - git client

* Show the drawing of the GitHub PR process in the cloud we have used in the previous session.

* Show [Slack](https://code-maven.slack.com/)

* [GitLab](https://gitlab.com/): just show that it exists

* Show how to use Git on the command line to update the GitHub pages [git slides](https://code-maven.com/slides/git/) use a new Windows machine for this.
* Git - use the following commands:

```
git config --global --add user.name "Foo Bar"
git config --global --add user.email foo@bar.com
```

These commands created the `~/.gitconfig` file.


Generate private-key public-key pair. Put the public-key in your GitHub user.

```
sh-keygen  Add public key to GitHub
```


```
git clone

git status
git diff
git add
git commit
git show SHA
git push
git remote -v
```

We also saw:

```
gitk --all
```

We also saw some dangerous commands:

```
git reset HEAD~1   # remove the most recent commit
```

```
git push --force   # forcibly overwrite what is in the remote
```

* [Video 3.1](https://youtu.be/jkB2fO-D4X0)
* [Video 3.2](https://youtu.be/v1b1F_BTfrA)


## Assignment

* Clone the repository of your github pages.
* Update the files. (add new files).
* Commit the changes.
* Push the changes out


## Session 4 - next week



* Demo project https://github.com/zarr-developers/zarr-python/ and PR https://github.com/zarr-developers/zarr-python/pull/1299


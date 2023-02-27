# Open Sorce Development Course

https://osdc.code-maven.com/osdc-2023-01-public/

* Start day: 2023.01.08

## TOC

* [Session 1 - Welcome - Version Control - Journal - Slack](#session-1---welcome---version-control---journal---slack)
* [Assignment 1](#assignment-1)
* [Session 2 - Create GitHub Pages using the GitHub UI, Markdown](#session-2---create-github-pages-using-the-github-ui-markdown)
* [Assignment 2](#assignment-2)
* [Session 3 - git client](#session-3---git-client)
* [Assignment 3](#assignment-3)
* [Session 4 - Upload your own project - testing](#session-4---upload-your-own-project---testing)
* [Assignment 4](#assignment-4)
* [Assignment 5](#assignment-5)
* [Assignment 6](#assignment-6)
* [Session 7](#session-7)
* [Assignment 6](#assignment-6)
* [Session 8](#session-8)

## Videos

* [Playlist](https://www.youtube.com/playlist?list=PLm2NBp4tb5F20b5mGbNXFOzQWtbd5K5IH)

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


## Assignment 3

* Clone the repository of your github pages.
* Update the files. (add new files).
* Commit the changes.
* Push the changes out

A couple of suggestions for the blog posts
* Use a title that can sound interesting to others as well eg. **How to contribute to an open source project** or  **How to Send a pull request on GitHub**.
* Add `osdc` tag and other relevant tags.
* Add the `series:` field to the `Jekyll front matter` (the header of each post on DEV.to)
* Use Markdown in the post.
* Include links to the relevant sites and pages such as the web site of the [Open Source Development Course](https://osdc.code-maven.com/) and the web site of our course: [Open Source Development Course in Hebrew](https://osdc.code-maven.com/c/osdc-2023-01-public).


## Session 4 - Upload your own project - testing

### Find the GitHub repositories of packages.

* Python `import requests` via [PyPI](https://pypi.org/).
* Perl `use WWW::Mechanize;`  via [MetaCPAN](https://metacpan.org/).
* NodeJS `express` via [NPM](https://www.npmjs.com/).
* JavaScript `React` or `Vue` via [NPM](https://www.npmjs.com/).
* Java `GSON` via [Maven Central](https://search.maven.org/)

* My list of [Registries of 3rd party libraries / packages / modules](https://code-maven.com/package-registry)

### Process to add an existing repository to your own GitHub account.

* Create Git repository locally.
    `git init`
* Add files to the local git repository
    `git add`
    `git commit`
* Create an empty Git repository on GitHub
* Connect the two, `push` out the local repo.
* Add tests to the project.
    * [Python testing demo](https://code-maven.com/slides/python/testing-demo)
    * [Perl testing demo](https://code-maven.com/slides/perl/testing-demo)
    * [NodeJS testing demo](https://code-maven.com/slides/nodejs/testing-demo)
* Push out the changes.

* Generate test coverage report.

### Notes from the meeting

* [SO with drawing about Git staging](https://stackoverflow.com/questions/13072111/gits-local-repository-and-remote-repository-confusing-concepts)
* [The slides](https://code-maven.com/slides/)
* [Source of the slides](https://github.com/szabgab/slides)
* [Demo repo](https://github.com/OSDC-Code-Maven/osdc-2023-01-public-testing-demo)
* [PyDigger](https://pydigger.com/)

* [Video 4-1](https://youtu.be/e6Dc1SGhOQw)
* [Video 4-2](https://youtu.be/bdYXs7Szadg)

## Assignment 4

* Update the JSON file and inlcude a list of GitHub and GitLab repositories of projects that you use.
    * If you write Python and you have `import requests` then include the link `https://github.com/psf/requests`.
    * If you write Perl and you have `use WWW::Mechanize;` in your code then include `https://github.com/libwww-perl/WWW-Mechanize`
    * If you write NodeJS and you have `require('express')` in your code then include `https://github.com/expressjs/express`
    * If you write JavaScript e.g. Vue then include `https://github.com/vuejs/` as it is an organization with several repositories.
    * If you write Java and you have  in your code then include `https://github.com/google/gson`

* If you don't have any projects on GitHub (GitLab) yet. Upload one.
    * If you had a project in an earlier course with me, you can use that.
    * If you have a project in your lab that can be published with and open source license (which is not on GitHub yet) then use that.
* If you don't have any personal project yet. Start one now. A few ideas are listed at the bottom of [this page](https://code-maven.com/exercises).
* Include a README file explaining how to use the project.

* Once you pushed out the first version to GitHub share the link in our Slack channel.

* Monitor the Slack channel and when you see others post their project try to run the code.
    * If something is unlcear in the instructions feel free to ask questions in our Slack channel (e.g. in the thread of the annuncement of each project).
    * Open an issue on the project you are trying to use to report problems and/or ask for features.


* Write a blog post about the work you have done with plenty of links. Add it to your JSON file.



## Session 5 - clone, fork, push, pr

* Slack
    * paste link
    * edit message
    * Add link with text
    * Use threads

* Go over the few project people have submitted and comment. Can you get the answer to the follow questions? If not, open an issue asking about it.
    * What does this project do?
    * How do I install dependencies?
    * How do I run the tests?
    * How do I use this project?


* Add requirements to the project of Shuly.

* `clone`
* git checkout -b branch/name
* git push
* git remote add

We used the following to map the name "origin" for the purpuses of `push` to the forked repository.

```
git remote set-url origin --push git@github.com:szabgab/LIMS_results_validation.git
```

* `git pull` is `git fetch` followed by either `merge` or `rebase`
In the `~/.gitconfig` file there can be an entry that will set this

This will make `pull = fetch + merge`
```
[pull]
    rebase = false
```

This will make `pull = fetch + rebase`

```
[pull]
    rebase = true
```

`merge` vs. `rebase` only impacts the history of the repository and not the code.


* [Video 5-1](https://youtu.be/RlTkt5kjH7o)
* [Video 5-2](https://youtu.be/f6L9FsrmDio)


## Assignment 5

## Session 6 - testing R, Docker, gitignore, GitHub Actions

* Firs we saw an example writing a test in R

* Then we had an introduction to Docker

Running a plain Ubuntu-based image:

```
docker run --rm -it ubuntu:22.04 bash
```

Installing stuff

```
apt-get update
apt-get install python3
```

Running an image with Python 3.11 in it:

```
docker run --rm -it python:3.11
```

* Then we looked at the [Dockerfile for mydocker of Gabor](https://github.com/szabgab/mydocker)


* [Docker HUB](https://hub.docker.com/)
* [Docker Images based on Ubuntu](https://hub.docker.com/_/ubuntu)
* [Docker Images for Python](https://hub.docker.com/_/python)
* [Docker Images for R](https://hub.docker.com/_/r-base)

* Using [PyDigger](https://pydigger.com/) we found a simple python project called [Python-tools](https://github.com/zguillez/python-toolz) that had a [link to GitHub but no CI](https://pydigger.com/search/has-github-no-ci).
* We found it has some file in the `__pycache__` folder added. Reported it in this [issue](https://github.com/zguillez/python-toolz/issues/1).
* The added it to [.gitignore PR](https://github.com/zguillez/python-toolz/pull/2)

```
git clone git@github.com:zguillez/python-toolz.git
docker run -v/home/gabor/os/python-toolz:/opt --rm -it python:3.11 bash
git remote add fork git@github.com:szabgab/python-toolz.git
```

* We also wrote a test that executed the already existing example and configured GitHub Actions to run it on 3 versions of Python on macOS and on Linux. On Windows the tests failed due to newline issues. We sent a [Pull Request](https://github.com/zguillez/python-toolz/pull/3) with that.


* We used the [GitHub Actions skeleton for Python](https://github.com/szabgab/github-actions-python).
* There are more [GitHub Actions skeletons](https://code-maven.com/github-actions).

* Similar to the PyDigger there are also:
* [Ruby Digger](https://ruby-digger.code-maven.com/)
* [CPAN Digger](https://cpan-digger.perlmaven.com/) for Perl
* [CI Challenge of December 2022](https://code-maven.com/2022-december-ci-challenge) in which every I sent a PR adding GitHub Actions to an open source project written in Python, Perl, or Ruby.

* [Video 6-1](https://youtu.be/9cgcgKXH72g)
* [Video 6-2](https://youtu.be/chTGh4pFJhk)

## Assignment 6

* Pick a few projects in your favorite programming language and try to run its tests locally in a Docker container.
* If you encounter any problems, report them. Feel free to first report them in our Slack and report them after we discussed them.
    * Files added that should be ignored with .gitignore
    * Generated files not listed in .gitignore
    * No instructions on how to run tests.
    * No tests.
    * Tests failing on your local system (inside a Docker is safer).
    * If you can set up GitHub Actions.


## Session 7

* Alex invited you to look at his project and start contributing there. I'd say look at [our web site](https://osdc.code-maven.com/osdc-2023-01-public/). You have links to the GitHub and GitLab accounts to each one of the participants of the course. Find something that interests you and try to contribute.

* We looked at the source code of [DEV.to](https://dev.to/) that is called [Forem](https://www.forem.com/) and is located [here in GitHub](https://github.com/forem/forem)
After some failed searches among the issues we found the [discussion Shuly opened](https://github.com/forem/forem/discussions?discussions_q=author%3AShulyAvraham), the [discussion about auto-save](https://github.com/forem/forem/discussions/15862). We also [searched the issues](https://github.com/forem/forem/issues?q=is%3Aissue+is%3Aopen+autosave) and found [this](https://github.com/forem/forem/issues/18462) issue about the topic. It is unfortuate that the project does not provide enough response to these discussions and issues.


* We also looked at the [zarr-python](https://github.com/zarr-developers/zarr-python/) project and specifically at [this PR](https://github.com/zarr-developers/zarr-python/pull/1299) that is related to [this issue](https://github.com/zarr-developers/zarr-python/issues/538) We found that it has not been touched for 2 months.

* We then discussed the idea of creating a fork and accepting some of the PRs there for our private use. Here are the instruction to do that:


```
git clone URL                             # clone the project locally
git checkout -b mymain                    # Create a branch that we will maintain. It is better not use the original main or master branches for this. (we use the branch-name szabgab for this in the video)

git fetch origin pull/1299/head           # Use the PR number to fetch the code from the pull-request
git checkout -b pr-1299 FETCH_HEAD        # Create a branch (using the PR number can be a good idea) based on what we have just fetched.
git checkout mymain                       # Go to mymain
git merge pr-1299                         # Merge the PR into "mymain"
```

There is actually a shorter version:

```
git fetch origin pull/PR/head:NAME_OF_LOCAL_BRANCH
```

Like this:

```
git fetch origin pull/1351/head:p-1351
```


First I showed this using a [simple PR](https://github.com/zarr-developers/zarr-python/pull/1357) and it worked.

Then I tried with the one [we actually wanted](https://github.com/zarr-developers/zarr-python/pull/1299) and it had a nasty merge-conflict.

Resolving that would require deep knowledge of the project so we have not tried to do that.

We discuessed that it is probably the responsibilit of the PR-sender to make sure the PR can be merged without a conflict, but then it is very diffictul to do if the PR is not accepted quickly. We saw that there was a merge inside the PR. I mentioned that I would have used rebase there.


* We saw a simple merge conflict resolution.

```
mkdir demo
cd demo
# edit README, add a line
git init
git add .
git commit -m init

git checkout -b first
# edit README, add a line at the top
git add .
git commit -m first


git checkout main
# edit READEME, add a line at the bottom
git add .
git commit -m main


git merge first   # this will open the default editor so you can type in the commit message for the merge.
```

Do the above, but this time change the middle line in both branches.
The `git merge` will complain and create a file with markers showing which version came from which branch. You have to edit the file with your favorite editor to resolve the merge conflicts.
There are various GUI-based editors that will make the experience nicer.

However the better solution is to reduce the chances of conflict or even to avoid them. This can be done by working on the same `main` branch and pulling and pushing code frequently.

Working in a separate branch is less ideal, but when preparing a PR that's the way to work. In that case try to make the PR as small as possible and try to get it merged as soon as possible. Follow the project and keep rebasing your branch to be up-to-date with the main development branch of the project.


* We mentioned the Dockerfile I use to run projects locally. It can be found [here](https://github.com/szabgab/mydocker)
* [R-base](https://hub.docker.com/_/r-base) Docker images for R

* [testthat](https://testthat.r-lib.org/) for testing R code

* How to find projects on GitHub:
    * Either sort them by popularity (stars) ot by recent activity: (Recently update)
    * Looking at popular project can help understanding how such projects are managed
    * Looking at recently update projects with few stars will probably provide more easy opportunities to contribute tests, documentation, CI, etc.
    * [Projects in R](https://github.com/topics/r?l=r&o=desc&s=stars)
    * [Projects in PHP](https://github.com/topics/php?l=php&o=desc&s=stars)

* One thing I'd expect from each project either in its README file or in the CONTRIBUTION file is an explanation
    * how to set up the local development environment
    * how to install the dependencies of the project (both dependencies in the programming language of the project and potential other dependencies)
    * how to run the tests of the project locally
    * Ideally there might be a Dockerfile to make it easy to run the whole thing locally.

* A sugestion by Alex was: Take a project in some language an convert to another language.

* I showed the [Kantoniko](https://kantoniko.com/) web site - a multilingual Ladino dictionary.
    * I mentioned the [Rashi script](https://en.wikipedia.org/wiki/Rashi_script)
    * and also [Solitreo](https://en.wikipedia.org/wiki/Solitreo)
    * We have an example in Rashi, the word [abashar](https://kantoniko.com/words/ladino/abashar)

* [Video 7-1](https://youtu.be/8iG0cd7TU6s)
* [Video 7-2](https://youtu.be/byJYSCO2oaQ)

### Assignment 7

* Set up locally and contribute to [Kantoniko](https://kantoniko.com/) and/or [PyDigger](https://pydigger.com/)
* Pick one (or more) open source projects in your favorite language and run the tests locally.
* If you can open an issue, send a PR to these projects

## Session 8

* Pick up a project (Python, R, or PHP), set up the local environemt, run the tests locally.



* dev.to mention the setting to use the Markdown editor

* Testing PHP
* Testing R

* GitHub Actions for each one of them.


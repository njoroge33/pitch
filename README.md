# PITCH
An application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.
## Built By [John Gichuhi](https://github.com/njoroge33/)
## Description
Pitches is a web application that allow user to post a pitch of any title, be it business ,potitics or lifestyle, he/she can vote or devote other people pitches, add comments by signing.
You can view the site at: https://njoropitches.herokuapp.com/
## User Stories
These are the behaviours/features that the application implements for use by a user.
As a user I would like to:
- See the pitches other people have posted
- Vote on the pitch they liked and give it a downvote or upvote
- Signed in for me to leave a comment
- View the pitches i have created in profile page
- Comment on different pitches and leave and leave a feedback
- Submit a pitch in any category
- view different categories
## Specifications
| Behaviour                                  |            Input             |                                                               Output |
| :----------------------------------------- | :--------------------------: | -------------------------------------------------------------------: |
| Display comments                           |       **On page load**       |           List of various comments sources is displayed per category |
| Display comments from people who signed in |  **Click on Add comments**   |         Redirected to a page with a list of comments from the source |
| Display the pitches and comments           |       **On page load**       |                 Each pitch displays an title, description and author |
| Read an entire pitch                       | **pitch category sub-title** | Redirected to the picked category source's site to read entire pitch |
| Go back to pick category you need          |        **Click Home**        |                                  Redirected to the post a pitch area |
## SetUp / Installation Requirements
### Prerequisites
- python3.6
- pip
- virtualenv
### Cloning
- In your terminal:
  $ git clone https://github.com/njoroge33/pitch.git
        $ cd news
## Running the Application
- Creating the virtual environment
  $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
- Installing Flask and other Modules
  $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
  $ python3.6  pip install flask-migrate
        $ python3.6 manage.py db init
  $ python3.6 manage.py db migrate -m "Initial Migration"
        $ python3.6 manage.py db upgrade
  $ pip install flask-SQLAlchemy
        $ pip install psycopg2
- To run the application, in your terminal:
  \$./start.sh or python3.6 manage.py server
## Testing the Application
- To run the tests for the class files:
  $ cd app
        $ python3.6 test_user.py
## Technologies Used
- Python3.6
- Flask
## License
MIT &copy;2019 [John Gichuhi](https://github.com/njoroge33)
PITCHES VOTES - Is web application for users to express the views and interest about particular topics in selected category

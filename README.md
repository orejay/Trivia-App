# Trivia App
This project is a trivia app. Players are allowed to:
* Display questions - both all questions and by category. Question cards show the question, category, and difficulty rating and players can show/hide the answer.
* Delete questions.
* Add questions and require that they include the question and answer text.
* Search for questions based on a text query string.
* Play the quiz game, randomizing either all questions or within a specific category.

This project is part of the ALX Udacity Full Stack Nanodegree program.

All backend code follows [PEP8 style guidelines](https://peps.python.org/pep-0008/).

## Getting Started

**Pre-requisites and Local Development**
Developers cloning this project on their computers should already have Python3, pip and node installed.

**Front End**

From the frontend directory run `npm install`. This command installs all the front end dependencies.

This project is currently run on localhost so the proxy is set to `http://127.0.0.1:5000` for all requests.

**Back End**

From the backend folder create a virtual environment by running

  `virtualenv env`
  
Activate the virtual environment by running 

  `env/Scripts/activate`
  
Run `pip install requirements.txt`. This command installs all required packages which are included in the requirements file.

After installing the requirements, start the app by running

  `export FLASK_APP=flaskr
  export FLASK_ENV=development
  flask run`

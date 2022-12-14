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

To start the front end app run

  `npm start`

This project is currently run on localhost `http://127.0.0.1:3000` the proxy is set to `http://127.0.0.1:5000` for all requests to the backend.

**Back End**

From the backend folder create a virtual environment by running

  `virtualenv env`
  
Activate the virtual environment by running 

  `env/Scripts/activate`
  
Run `pip install requirements.txt`. This command installs all required packages which are included in the requirements file.

After installing the requirements, start the app by running

  ```
  export FLASK_APP=flaskr
  export FLASK_ENV=development
  flask run
  ```

The application is run on localhost `http://127.0.0.1:5000/`.

**Tests**

In order to run tests you need to create a test database that mirror the original database by running

  ```
  dropdb trivia_test
  createdb trivia_test
  psql trivia_test < trivia.psql
  python test_flaskr.py
  ```
  
  **Do not** include the drop database line the first time you run the block of code as the database has **not yet** been created
  
  ## API Reference
  
  **Getting Started**
  
* Base URL: The backend app is hosted locally at http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
* API Key: This app currently doesnt use any API keys.

**Error Handling**

Errors are returned as JSON objects in the following format:

  ```
  {
    'success': False,
    'error': 500,
    'message': 'Internal server error'
  }
  ```
  
The API will return four error types when requests fail:

* 400: Bad Request
* 404: Resource Not Found
* 422: Not Processable
* 500: Internal server error

**End points**

**GET/questions**

* General:
  * Returns an object containing an object of categories, a list of questions, success value, and total number of questions.
  * Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

* Sample: `curl http://127.0.0.1:5000/questions`

  ```
    {
      "categories": {
        "1": "Science", 
        "2": "Art", 
        "3": "Geography", 
        "4": "History", 
        "5": "Entertainment", 
        "6": "Sports"
      }, 
      "questions": [
        {
          "answer": "Maya Angelou", 
          "category": 4, 
          "difficulty": 2, 
          "id": 5, 
          "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        }, 
        {
          "answer": "Muhammad Ali", 
          "category": 4, 
          "difficulty": 1, 
          "id": 9, 
          "question": "What boxer's original name is Cassius Clay?"
        }, 
        {
          "answer": "Apollo 13", 
          "category": 5, 
          "difficulty": 4, 
          "id": 2, 
          "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }, 
        {
          "answer": "Tom Cruise", 
          "category": 5, 
          "difficulty": 4, 
          "id": 4, 
          "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        }, 
        {
          "answer": "Edward Scissorhands", 
          "category": 5, 
          "difficulty": 3, 
          "id": 6, 
          "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }, 
        {
          "answer": "Brazil", 
          "category": 6, 
          "difficulty": 3, 
          "id": 10, 
          "question": "Which is the only team to play in every soccer World Cup tournament?"
        }, 
        {
          "answer": "Uruguay", 
          "category": 6, 
          "difficulty": 4, 
          "id": 11, 
          "question": "Which country won the first ever soccer World Cup in 1930?"
        }, 
        {
          "answer": "George Washington Carver", 
          "category": 4, 
          "difficulty": 2, 
          "id": 12, 
          "question": "Who invented Peanut Butter?"
        }, 
        {
          "answer": "Lake Victoria", 
          "category": 3, 
          "difficulty": 2, 
          "id": 13, 
          "question": "What is the largest lake in Africa?"
        }, 
        {
          "answer": "The Palace of Versailles", 
          "category": 3, 
          "difficulty": 3, 
          "id": 14, 
          "question": "In which royal palace would you find the Hall of Mirrors?"
        }
      ], 
      "success": true, 
      "total_questions": 22
    }
  ```
  
 **GET/categories**
 
 * General:
   * Returns an object containing an object of categories and a success value.
 
 * Sample: `curl http://127.0.0.1:5000/categories`
 
  ```
  {
    "categories": {
      "1": "Science", 
      "2": "Art", 
      "3": "Geography", 
      "4": "History", 
      "5": "Entertainment", 
      "6": "Sports"
    }, 
    "success": true
  }
  ```
  
**GET/categories/category_id/questions**

* General:
  * Returns an object containing a success value, a list of question objects, total number of questions and the current category.
  * Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

* Sample: `curl http://127.0.0.1:5000/categories/2/questions`

  ```
  {
    "current_category": "Art", 
    "questions": [
      {
        "answer": "Escher", 
        "category": 2, 
        "difficulty": 1, 
        "id": 16, 
        "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
      }, 
      {
        "answer": "Mona Lisa", 
        "category": 2, 
        "difficulty": 3, 
        "id": 17, 
        "question": "La Giaconda is better known as what?"
      }, 
      {
        "answer": "One", 
        "category": 2, 
        "difficulty": 4, 
        "id": 18, 
        "question": "How many paintings did Van Gogh sell in his lifetime?"
      }, 
      {
        "answer": "Jackson Pollock", 
        "category": 2, 
        "difficulty": 2, 
        "id": 19, 
        "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
      }
    ], 
    "success": true, 
    "total_questions": 4
  }
  ```
  
**POST/questions**

* General:
  * Creates a new question using the submitted question, answer, difficulty and category. Returns a `{'success': True}` json response

* `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"What country is often called 'the greatest country in the world'?", "answer":"Nigeria", "difficulty":"3", "category":"4" }'`

  ```
  {
    'success': True
  }
  ```
  
**POST/search**

* General:
  * Performs a case insensitive search for questions that contain the keyword searched for.

* `curl http://127.0.0.1:5000/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": "who"}'`

  ```
   "questions": [
      {
        "answer": "Maya Angelou",
        "category": 4,
        "difficulty": 2,
        "id": 5,
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
        "answer": "George Washington Carver",
        "category": 4,
        "difficulty": 2,
        "id": 12,
        "question": "Who invented Peanut Butter?"
      },
      {
        "answer": "Alexander Fleming",
        "category": 1,
        "difficulty": 3,
        "id": 21,
        "question": "Who discovered penicillin?"
      },
      {
        "answer": "Ronaldo",
        "category": 4,
        "difficulty": 5,
        "id": 25,
        "question": "who is the goat?"
      }
    ],
    "success": true,
    "total_questions": 4
  }
  ```
  
**POST/quizzes**

* General:
  * Returns one question at a time for the user to answer, depending on the category selected.
 
* `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"id":"3"}}'`

  ```
  {
    "question": {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    "success": true
  }
  ```
  
**DELETE/questions/question_id**

* General
  * Deletes the question with the given id if it exists and returns a success value.

* `curl -X DELETE http://127.0.0.1:5000/questions/2`

  ```
  {
    'success': True
  }
  ```
  
## Deployment N/A

## Authors

Oreoluwa Jaiyesimi and Udacity

## Acknowledgement

The awesome team at Udacity.

import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from settings import TEST_DB_NAME, DB_USER, DB_PASSWORD


from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = TEST_DB_NAME
        self.database_path = 'postgresql://{}:{}@{}/{}'.format(
            DB_USER, DB_PASSWORD, 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            "answer": "Nigeria",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "What country is often referred to as 'the best country in the world'?"
        }

        self.search_term = {
            "searchTerm": "who"
        }

        self.quiz_request_body = {
            "previous_questions": [],
            "quiz_category": {"id": "3"}
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))

    def test_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    def test_invalid_pages(self):
        res = self.client().get('/kiiwtcfy')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Page not found')

    def test_search_question(self):
        res = self.client().get('/categories/2/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['current_category'])
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))

    def test_add_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_search_question(self):
        res = self.client().post('/search', json=self.search_term)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(len(data['questions']))

    def test_get_quiz_question(self):
        res = self.client().post('/quizzes', json=self.quiz_request_body)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])

    def test_delete(self):
        res = self.client().delete('/questions/32')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 32).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(question, None)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

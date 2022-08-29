import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, questions):
    page = request.args.get('page', 1, type=int)
    start = (page-1)*QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    question_list = [question.format() for question in questions]
    current_questions = question_list[start:end]
    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )

        return response

    @app.route('/categories')
    def get_categories():
        categories = Category.query.all()
        category_list = {}
        for category in categories:
            category_list[category.id] = category.type

        return jsonify({
            "success": True,
            "categories": category_list
        })

    @app.route("/questions")
    def home_page():
        questions = Question.query.all()
        page_questions = paginate_questions(request, questions)
        categories = Category.query.all()
        category_store = {}
        for category in categories:
            category_store[category.id] = category.type

        return jsonify({
            "success": True,
            "questions": page_questions,
            "total_questions": len(questions),
            "categories": category_store,
        })

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        question = Question.query.get(question_id)
        question.delete()

        return jsonify({
            'success': True
        })

    @app.route('/questions', methods=['POST'])
    def add_question():
        body = request.get_json()
        new_question = body.get('question')
        new_answer = body.get('answer')
        new_difficulty = body.get('difficulty')
        new_category = body.get('category')
        question = Question(question=new_question, answer=new_answer,
                            difficulty=new_difficulty, category=new_category)
        question.insert()

        return jsonify({
            "success": True,
        })

    @app.route('/search', methods=['POST'])
    def search_question():
        body = request.get_json()
        search_term = body.get('searchTerm')
        questions = Question.query.filter(
            Question.question.ilike('%'+search_term+'%')).all()
        page_questions = paginate_questions(request, questions)

        return jsonify({
            "success": True,
            "questions": page_questions,
            "total_questions": len(questions),
        })

    @app.route('/categories/<int:category_id>/questions')
    def get_by_category(category_id):
        questions = Question.query.filter_by(category=category_id).all()
        page_questions = paginate_questions(request, questions)
        category = Category.query.get(category_id)

        return jsonify({
            "success": True,
            "questions": page_questions,
            "total_questions": len(questions),
            "current_category": category.type,
        })

    @app.route('/quizzes', methods=['POST'])
    def play_quiz():
        body = request.get_json()
        category = body.get('quiz_category')
        previous_questions = body.get('previous_questions')
        if (category['id'] != 0):
            questions = Question.query.filter_by(
                category=category['id']).order_by(Question.question).all()
            quiz_number = random.randint(0, len(questions)-1)
            if previous_questions == []:
                question = questions[quiz_number]
            else:
                while quiz_number in previous_questions:
                    quiz_number = random.randint(0, len(questions)-1)
                question = questions[quiz_number]
        else:
            questions = Question.query.order_by(Question.question).all()
            quiz_number = random.randint(0, len(questions)-1)
            while quiz_number in previous_questions:
                quiz_number = random.randint(0, len(questions)-1)
            question = questions[quiz_number]
        next_question = {
            "answer": question.answer,
            "category": question.category,
            "difficulty": question.difficulty,
            "id": question.id,
            "question": question.question
        }

        return jsonify({
            "success": True,
            "question": next_question
        })

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Page not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable_request(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable request'
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal server error'
        }), 500

    return app

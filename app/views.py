from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify


'''
Blueprints
'''


api_bp = Blueprint('api_bp', __name__)


'''
Routes
'''


@api_bp.route('/api/')
def apiHome():
    return jsonify({"about": "this is the api page"})

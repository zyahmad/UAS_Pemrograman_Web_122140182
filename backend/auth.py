from pyramid.view import view_config
from pyramid.response import Response
from ..db import Session
from ..models import User
import bcrypt
import json

@view_config(route_name='login', renderer='json', request_method='POST')
def login(request):
    try:
        data = request.json_body
        email = data.get('email')
        password = data.get('password')
        session = Session()
        user = session.query(User).filter_by(email=email).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
            return {'status': 'success', 'message': 'Logged in'}
        else:
            return Response(json_body={'error': 'Invalid credentials'}, status=401)
    except Exception as e:
        return Response(json_body={'error': str(e)}, status=500)

@view_config(route_name='register', renderer='json', request_method='POST')
def register(request):
    try:
        data = request.json_body
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return Response(json_body={'error': 'Missing required fields'}, status=400)
        session = Session()
        existing_user = session.query(User).filter(User.email == email).first()
        if existing_user:
            return Response(json_body={'error': 'User already exists'}, status=400)
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()
        return {'status': 'success', 'message': 'Registration successful'}
    except Exception as e:
        return Response(json_body={'error': str(e)}, status=500)

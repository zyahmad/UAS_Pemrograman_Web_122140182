from pyramid.view import view_config
from pyramid.response import Response
from .views.models import Profile, User
from .views.db import DBSession
from ..utils.file_upload import save_uploaded_file

@view_config(route_name='get_profile', request_method='GET', renderer='json')
def get_profile(request):
    try:
        user_id = request.authenticated_userid
        if not user_id:
            return Response(json_body={'error': 'Unauthorized'}, status=401)
        profile = DBSession.query(Profile).filter_by(user_id=user_id).first()
        if not profile:
            return Response(json_body={'error': 'Profile not found'}, status=404)
        return {
            'image': profile.image,
            'display_name': profile.display_name,
            'address': profile.address,
            'birthdate': profile.birthdate,
            'gender': profile.gender,
            'email': profile.user.email,
            'phone_number': profile.user.phone_number,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
        }
    except Exception as e:
        request.logger.error(f"Error getting profile: {e}")
        return Response(json_body={'error': 'Internal server error'}, status=500)

@view_config(route_name='edit_profile', request_method='PATCH', renderer='json')
def edit_profile(request):
    try:
        user_id = request.authenticated_userid
        if not user_id:
            return Response(json_body={'error': 'Unauthorized'}, status=401)
        profile = DBSession.query(Profile).filter_by(user_id=user_id).first()
        if not profile:
            return Response(json_body={'error': 'Profile not found'}, status=404)

        data = request.POST
        if 'image' in data:
            image_file = data['image']
            filename = save_uploaded_file(image_file)
            profile.image = filename

        profile.display_name = data.get('display_name', profile.display_name)
        profile.address = data.get('address', profile.address)
        profile.birthdate = data.get('birthdate', profile.birthdate)
        profile.gender = data.get('gender', profile.gender)
        profile.first_name = data.get('first_name', profile.first_name)
        profile.last_name = data.get('last_name', profile.last_name)

        DBSession.add(profile)
        return {'message': 'Profile updated successfully'}
    except Exception as e:
        request.logger.error(f"Error editing profile: {e}")
        return Response(json_body={'error': 'Internal server error'}, status=500)

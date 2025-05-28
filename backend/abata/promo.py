from pyramid.view import view_config
from pyramid.response import Response
from .views.models import Promo
from .views.db import DBSession
from ..utils.file_upload import save_uploaded_file

@view_config(route_name='get_promos', request_method='GET', renderer='json')
def get_promos(request):
    try:
        promos = DBSession.query(Promo).all()
        promos_list = []
        for promo in promos:
            promos_list.append({
                'id': promo.id,
                'title': promo.title,
                'description': promo.description,
                'discount_percentage': promo.discount_percentage,
                'image_path': promo.image_path,
                'start_date': promo.start_date.isoformat() if promo.start_date else None,
                'end_date': promo.end_date.isoformat() if promo.end_date else None,
            })
        return {'promos': promos_list}
    except Exception as e:
        request.logger.error(f"Error retrieving promos: {e}")
        return Response(json_body={'error': 'Internal server error'}, status=500)

# Implement POST, PATCH, DELETE for promos with image upload handling.
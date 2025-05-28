from pyramid.view import view_config
from pyramid.response import Response
from .views.models import Product, Category
from .views.db import DBSession
from ..utils.file_upload import save_uploaded_file
import json

@view_config(route_name='get_products', request_method='GET', renderer='json')
def get_all_products(request):
    try:
        category_id = request.params.get('category', None)
        order_by = request.params.get('orderBy', None)
        sort = request.params.get('sort', None)
        search_by_name = request.params.get('searchByName', None)
        limit = int(request.params.get('limit', 10))
        page = int(request.params.get('page', 1))

        query = DBSession.query(Product)
        if category_id:
            query = query.filter(Product.category_id == category_id)
        if search_by_name:
            query = query.filter(Product.name.ilike(f"%{search_by_name}%"))
        if order_by:
            if hasattr(Product, order_by):
                if sort == 'desc':
                    query = query.order_by(getattr(Product, order_by).desc())
                else:
                    query = query.order_by(getattr(Product, order_by).asc())
        total = query.count()
        products = query.offset((page - 1) * limit).limit(limit).all()

        products_list = []
        for prod in products:
            products_list.append({
                'id': prod.id,
                'name': prod.name,
                'price': prod.price,
                'category_id': prod.category_id,
                'description': prod.description,
                'image_path': prod.image_path,
            })
        return {'total': total, 'products': products_list}
    except Exception as e:
        request.logger.error(f"Error retrieving products: {e}")
        return Response(json_body={'error': 'Could not retrieve products'}, status=500)

@view_config(route_name='product_by_id', request_method='GET', renderer='json')
def get_product_by_id(request):
    try:
        product_id = request.matchdict.get('id')
        product = DBSession.query(Product).filter_by(id=product_id).first()
        if not product:
            return Response(json_body={'error': 'Product not found'}, status=404)
        return {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'category_id': product.category_id,
            'description': product.description,
            'image_path': product.image_path,
        }
    except Exception as e:
        request.logger.error(f"Error retrieving product: {e}")
        return Response(json_body={'error': 'Internal server error'}, status=500)

# Implement POST, PATCH, DELETE for products with image upload handling.
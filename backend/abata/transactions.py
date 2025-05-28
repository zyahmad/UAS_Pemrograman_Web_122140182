from pyramid.view import view_config
from pyramid.response import Response
from .views.models import Transaction, TransactionDetail, Product, TransactionStatus
from .views.db import DBSession
import json

@view_config(route_name='create_transaction', request_method='POST', renderer='json')
def create_transaction(request):
    try:
        data = request.json_body
        payment_id = data.get('payment_id', 1)
        delivery_id = data.get('delivery_id', 1)
        status_id = data.get('status_id', 3)
        address = data.get('address', '')
        notes = data.get('notes', '')
        products = data.get('products', [])
        user_id = request.authenticated_userid

        if not user_id:
            return Response(json_body={'error': 'Unauthorized'}, status=401)

        transaction = Transaction(
            user_id=user_id,
            payment_id=payment_id,
            delivery_id=delivery_id,
            status_id=status_id,
            address=address,
            notes=notes
        )
        DBSession.add(transaction)
        DBSession.flush()

        for prod in products:
            product_id = prod.get('product_id')
            quantity = prod.get('quantity', 1)
            product = DBSession.query(Product).filter_by(id=product_id).first()
            if not product:
                continue
            detail = TransactionDetail(
                transaction_id=transaction.id,
                product_id=product_id,
                quantity=quantity,
                price=product.price
            )
            DBSession.add(detail)

        return {'transaction_id': transaction.id}
    except Exception as e:
        request.logger.error(f"Error creating transaction: {e}")
        return Response(json_body={'error': 'Internal server error'}, status=500)

# Implement other transaction views similarly.
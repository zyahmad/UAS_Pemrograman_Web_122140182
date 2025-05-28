from pyramid.view import view_config
from pyramid.response import Response
from .views.db import DBSession
from sqlalchemy import func
from .views.models import Transaction
import datetime

@view_config(route_name='monthly_report', request_method='GET', renderer='json')
def monthly_report(request):
    try:
        # Example: aggregate total sales per month
        results = DBSession.query(
            func.date_trunc('month', Transaction.created_at).label('month'),
            func.count(Transaction.id).label('total_transactions')
        ).group_by('month').order_by('month').all()

        report = [{'month': r.month.strftime('%Y-%m'), 'total_transactions': r.total_transactions} for r in results]
        return {'monthly_report': report}
    except Exception as e:
        request.logger.error(f"Error generating monthly report: {e}")
        return Response(json_body={'error': 'Internal server error'}, status=500)

@view_config(route_name='admin_reports', request_method='GET', renderer='json')
def admin_reports(request):
    try:
        view = request.params.get('view', 'monthly')
        # Implement different report types based on 'view' param
        # For simplicity, return monthly report same as above
        return monthly_report(request)
    except Exception as e:
        request.logger.error(f"Error generating admin reports: {e}")
        return Response(json_body={'error': 'Internal server error'}, status=500)

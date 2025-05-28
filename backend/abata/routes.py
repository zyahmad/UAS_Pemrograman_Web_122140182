def includeme(config):
    # Auth routes
    config.add_route('login', '/apiv1/auth/login')
    config.add_route('register', '/apiv1/auth/register')
    config.add_route('forgotPass', '/apiv1/auth/forgotPass')
    config.add_route('resetPass_get', '/apiv1/auth/resetPass')
    config.add_route('resetPass_patch', '/apiv1/auth/resetPass')
    config.add_route('logout', '/apiv1/auth/logout')

    # Products routes
    config.add_route('get_products', '/apiv1/products')
    config.add_route('product_by_id', '/apiv1/products/{id}')

    # Transactions routes
    config.add_route('create_transaction', '/apiv1/transactions')
    config.add_route('get_transactions', '/apiv1/transactions')
    config.add_route('update_transaction_status', '/apiv1/transactions/changeStatus')
    config.add_route('transaction_detail', '/apiv1/transactions/{transactionId}')
    config.add_route('user_transactions', '/apiv1/userPanel/transactions')

    # User Profile routes
    config.add_route('get_profile', '/apiv1/userPanel/profile')
    config.add_route('edit_profile', '/apiv1/userPanel/profile')

    # Admin routes
    config.add_route('monthly_report', '/apiv1/adminPanel/monthlyReport')
    config.add_route('admin_reports', '/apiv1/adminPanel/reports')

    # Promo routes
    config.add_route('get_promos', '/apiv1/promos')
    config.add_route('promo_by_id', '/apiv1/promos/{id}')
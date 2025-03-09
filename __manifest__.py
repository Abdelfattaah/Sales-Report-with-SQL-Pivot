# -*- coding: utf-8 -*-
{
    'name': "pivot_report",

    'summary': """
        SQL-based pivot report that consolidates data from Sales Orders (sale.order.line)
         and POS Orders (pos.order.line) into a single structured report.
    """,

    'author': "Abdelfattah Mohamed",
    'website': "https://abdelfattaah.github.io/",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','sale','point_of_sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

}

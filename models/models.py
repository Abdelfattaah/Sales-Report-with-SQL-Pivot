# -*- coding: utf-8 -*-
from odoo import models, fields, tools

class PivotReport(models.Model):
    _name = 'pivot.report'
    _description = 'Sales Pivot Report'
    _auto = False

    date_order = fields.Date(string="Date")
    product_name = fields.Char(string="Product Name")
    order_quantity = fields.Float(string="Order Quantity")
    total_order_amount = fields.Float(string="Total Order Amount")

    def init(self):

        tools.drop_view_if_exists(self._cr, 'pivot_report')
        self._cr.execute("""
        CREATE VIEW pivot_report AS 
        SELECT 
            md5(concat(pt.id, so.date_order::DATE::TEXT))::TEXT AS id,
            so.date_order::DATE AS date_order,
            pt.name->>'en_US' AS product_name,
            SUM(sol.product_uom_qty) AS order_quantity,
            SUM(sol.price_total) AS total_order_amount
        FROM sale_order_line sol
        JOIN sale_order so ON sol.order_id = so.id
        JOIN product_product pp ON sol.product_id = pp.id
        JOIN product_template pt ON pp.product_tmpl_id = pt.id
        WHERE so.state IN ('sale', 'done')
        GROUP BY so.date_order::DATE, pt.id, pt.name
        
        UNION ALL
        
        SELECT 
            md5(concat(pt.id, po.date_order::DATE::TEXT))::TEXT AS id,
            po.date_order::DATE AS date_order,
            pt.name->>'en_US' AS product_name,
            SUM(pol.qty) AS order_quantity,
            SUM(pol.price_subtotal_incl) AS total_order_amount
        FROM pos_order_line pol
        JOIN pos_order po ON pol.order_id = po.id
        JOIN product_product pp ON pol.product_id = pp.id
        JOIN product_template pt ON pp.product_tmpl_id = pt.id
        WHERE po.state IN ('paid', 'done')
        GROUP BY po.date_order::DATE, pt.id, pt.name;
        """)

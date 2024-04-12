# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplates(models.Model):
    _inherit = 'product.template'

    product_avg_cost = fields.Float(compute='_compute_avg_cost')

    def _compute_avg_cost(self):
        """Function defined for Compute Average Cost of each product"""
        for record in self:
            record.product_avg_cost = 0.0
            product_purchase = (self.env['purchase.order.line']
                                .search([('product_id', '=', record.id)]))
            total_cost = 0.0
            total_quantity = 0.0
            for product in product_purchase:
                total_cost += product.product_uom_qty * product.price_unit
                total_quantity += product.product_uom_qty
                if total_quantity > 0:
                    record.product_avg_cost = total_cost / total_quantity
                else:
                    record.product_avg_cost = 0.0

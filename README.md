## Sales & POS Pivot Report

This report aggregates **Sales Orders (SO)** and **Point of Sale Orders (POS)** into a unified **Pivot View** in Odoo.

### Demo

A 1-minute demo video of the functionality is available here:  
[![Watch the demo](https://img.youtube.com/vi/nagXNvWXH20/0.jpg)](https://youtu.be/nagXNvWXH20)

### Query Breakdown

The SQL view retrieves data from two sources:

- **Sales Orders** (`sale_order_line`)
- **Point of Sale Orders** (`pos_order_line`)

### Joins

The query uses **JOINs** to link orders with their respective products:

- **Sales Orders (`sale_order_line`)** → Linked to `sale_order`, `product_product`, and `product_template`.
- **POS Orders (`pos_order_line`)** → Linked to `pos_order`, `product_product`, and `product_template`.

This ensures that each order is mapped to the correct product details.

### UNION 

Since **Sales Orders** and **POS Orders** are stored in separate tables, we use `UNION ALL` to merge both datasets into a single report.

### Unique Row Identifier

We generate a **unique ID** for each row to prevent duplicate records and maintain data integrity in Odoo:

```sql
md5(concat(pt.id, so.date_order::TEXT))::TEXT AS id
```

This ensures stable record identification when fetching or exporting data.

### Optimizations for Large Datasets
- Filters only relevant records (state IN ('sale', 'done', 'paid')) to reduce query load.
- Aggregates data at the database level (SUM()) before sending it to Odoo, reducing processing time.

### Usage in Odoo
- Available in Pivot View for interactive analysis.
- Supports filtering by Start Date & End Date using Odoo's built-in search.
- Can be exported as an Excel file for further analysis.


USE sql_invoicing;
CREATE TABLE invoices_archive AS
SELECT 
     i.invoice_id,
     i.number,
     c.name AS client,
     i.invoice_total,
     invoice_date,
     payment__date,
     due_date,
     due_date
FROM invoices i
JOIN clients c
USING (client_id)
WHERE payment_date IS NOT NULL

ALTER TABLE trans03
ADD CONSTRAINT fk_customer_id
FOREIGN KEY (customer_id) REFERENCES customers (customer_id)

-- Use the provided database (assumed to be passed as argument)
USE alx_book_store;

-- Delete any existing customer with customer_id = 2
DELETE FROM Customers WHERE customer_id = 2;

-- Insert a single row into the Customers table
INSERT INTO Customers (customer_id, customer_name, email, address)
VALUES (2, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');

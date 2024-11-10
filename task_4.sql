-- Use the provided database (assumed to be passed as argument)
USE alx_book_store;

-- Get full description of the books table including the column type
SELECT COLUMN_NAME,
       COLUMN_TYPE,
       IS_NULLABLE,
       COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';

CREATE TABLE financial_sample(
    id SERIAL PRIMARY KEY,
    segment VARCHAR(30) NOT NULL,
    country VARCHAR(50) NOT NULL,
    product VARCHAR(50),
    discount_band VARCHAR(15),
    units_sold NUMERIC (10, 1) NOT NULL,
    manufacturing_price INTEGER NOT NULL,
    gross_sales NUMERIC (10, 2) NOT NULL,
    discounts NUMERIC(10, 1) NOT NULL,
    sales NUMERIC(10, 1) NOT NULL,
    cogs NUMERIC(1) NOT NULL,
    profit (10, 2) NOT NULL,
    date_sales TIMESTAMP,
    month_number VARCHAR(2),
    month_name VARCHAR(20),
    year VARCHAR(4)


);
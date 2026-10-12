# Product Search App

A simple phone search app built with FastAPI, MySQL, and Jinja2 templates.

## Features
- Search phones by company name (e.g. samsung, apple, google)
- Results shown in an HTML table that adjusts to the number of rows
- Parameterized SQL queries to prevent SQL injection

## Tech Stack
Python, FastAPI, MySQL, Jinja2, HTML

## Project Structure
product_project/
├── main.py
├── index.html
└── templates/
    └── show_product.html

## Setup

1. Install dependencies:
   pip install fastapi uvicorn mysql-connector-python python-multipart jinja2

2. Create the database and table:
   CREATE DATABASE IF NOT EXISTS product_db;
   USE product_db;
   CREATE TABLE product (
     id INT AUTO_INCREMENT PRIMARY KEY,
     prod_name VARCHAR(100),
     price INT,
     company VARCHAR(100)
   );
   INSERT INTO product (prod_name, price, company) VALUES
   ("samsung s23", 52000, "samsung"),
   ("iphone 17", 70000, "apple"),
   ("pixel 11", 90000, "google");

3. Update the MySQL credentials in `main.py`
   (better: use environment variables or a `.env` file).

4. Run the server:
   uvicorn main:app --reload

5. Open `index.html` in your browser, enter a company name, and submit.

## Endpoints
| Method | Route     | Description                          |
|--------|-----------|--------------------------------------|
| POST   | /product  | Search phones by company, show table |

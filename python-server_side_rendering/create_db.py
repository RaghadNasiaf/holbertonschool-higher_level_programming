#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Create and populate the SQLite database for products.

Database file:
- products.db

Table:
- Products (id, name, category, price)
"""

import sqlite3


def create_database():
    """Create products.db and populate it with initial data."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insert sample data (safe re-run using INSERT OR REPLACE)
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()

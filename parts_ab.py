#!/usr/bin/python3.6
import sqlite3
import string
from primefac import isPrime
import time

def prob1(cur):
    '''Get the total number of rows in Sales'''
    # YOUR CODE HERE
    pass

def prob2(cur):
    '''Get the number of different agent_ids in Sales'''
    # YOUR CODE HERE
    pass

def prob3(cur):
    '''For each letter in the alphabet,
    get the number of rows associated with an agent
    whose name started with that letter'''
    # YOUR CODE HERE
    pass

def prob3a(fchar_counts):
    '''Find which letter of the alphabet had the most rows
    where the agent's name started with that letter'''
    # YOUR CODE HERE
    pass

def prob3b(fchar_counts):
    '''Find which letters of the alphabet *did not* start the names
    of any agents'''
    # YOUR CODE HERE
    pass

def get_clean_sales(cur):
    '''Get all the rows in Sales where the amount was a positive, non-prime integer'''
    # YOUR CODE HERE
    pass

def write_clean_sales(cur, con, clean_sales):
    '''Create a new table called Clean_Sales(row_id INT, agent_id INT, agent TEXT, amount INT)
    containing all the rows of Sales where the amount was a positive, non-prime integer'''
    # YOUR CODE HERE
    pass

def prob5(cur):
    '''After creating Clean_Sales, get the name of the agent with the
    highest total amount in Clean_Sales'''
    # YOUR CODE HERE
    pass

def prob6(cur):
    '''Get the name of the agent who had the highest ratio of total amount
    in clean sales to total amount in sales.'''
    # YOUR CODE HERE
    pass

def main():
    with sqlite3.connect("fake_sales.sqlite") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Sales")
        dirty_sales = cur.fetchall()
        p1 = prob1(cur)
        print(f"prob1: {p1}")
        p2 = prob2(cur)
        print(f"prob2: {p2}")
        counts = prob3(cur)
        p3a = prob3a(counts)
        print(f"prob3a: {p3a}")
        p3b = prob3b(counts)
        print(f"prob3b: {p3b}")
        t0 = time.perf_counter()
        clean_rows = get_clean_sales(cur)
        write_clean_sales(cur, con, clean_rows)
        print(f"Time for synchronous creation of clean_sales: {time.perf_counter() - t0}")
        p5 = prob5(cur)
        print(f"prob5: {p5}")
        p6 = prob6(cur)
        print(f"prob6: {p6}")
        cur.close()
    con.close()

if __name__ == '__main__':
    main()
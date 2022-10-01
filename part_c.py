#!/usr/bin/python3.6
import asyncio
import aiosqlite
import sqlite3
from primefac import isPrime
import time
# use the same functions from parts A and B to answer questions,
# because the answers should be the same
from parts_ab import prob1, prob2, prob3, prob3a, prob3b, prob5, prob6

async def get_rows(con, x, dirty_rows):
    '''Gets all the rows from the fake_sales database where agent_id equals x.
con: aiosqlite Connection object.
x: int, the value of agent_id to filter for.
Adds the rows found to dirty_rows, all the uncleaned data found so far'''
    # DO NOT CHANGE THIS FUNCTION
    await asyncio.sleep(0.05) # add a 50ms wait to simulate a slow connection
    cur = await con.execute("SELECT * FROM Sales WHERE agent_id = ?", (x,))
    dirty_rows.extend(await cur.fetchall())

def clean_sales(dirty_rows):
    '''Returns all rows from dirty_rows where the amount (third column) is prime
Returns: None'''
    # YOUR CODE HERE

async def insert_clean_rows(con, clean_rows):
    '''Insert all of the rows in clean_rows into the database.
con: aiosqlite Connection object.'''
    # YOUR CODE HERE

async def create_prime_db():
    '''
1. Create a new table, Clean_Sales(row_id INT, agent_id INT, agent TEXT, amount INT)
2. Using the get_rows function (and NO OTHER functions) to query the database,
    get every row in Sales.
3. After collecting all rows from Sales, make a new list of all rows where amount
    is a positive, non-prime number.
Don't forget to write your code so that the connection always closes, even if
    there's an error!'''
    # YOUR CODE HERE

def main():
    '''Get answers to problems 1-6.
    Do this AFTER using to create the database.
    Your answers should be the same as in parts A and B.'''
    # YOUR CODE HERE
             
if __name__ == '__main__':
    t0 = time.perf_counter()
    # create the database
    print("time for asynchronous creation of clean_sales:", time.perf_counter() - t0)
    # now get the answers
    main()
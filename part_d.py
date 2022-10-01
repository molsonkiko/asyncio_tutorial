#!/usr/bin/python3.6
import asyncio
from aiofile import async_open
import os
import json
import re
import sqlite3

async def load_sales_json(fname):
    # YOUR CODE HERE

def parse_sales_json(j, multipliers):
    '''Process a JSON file as described in part D of questions.txt and return
    a 2-tuple:
    (the name of the agent, [list of integers, the total amount for each day])
    '''
    # YOUR CODE HERE

def write_sales(con, agent_id, name, amounts):
    '''Using a SQLite database connection, write the amounts sold to the
    Sales table.
con: as sqlite3 Connection object returned by sqlite3.connect(db fname)
agent_id: the agent_id of an agent, found in the name of the file.
name: the agent's name
amounts: the amount sold on each day
    '''
    # YOUR CODE HERE

def main():
    '''Parse the JSON data, write it to the database,
    and then query the database 
    to answer the questions in part D of questions.txt'''
    # YOUR CODE HERE
        
if __name__ == '__main__':
    main()
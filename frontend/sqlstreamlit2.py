#sqlstreamlit2.py
import streamlit as st
import pandas as pd
import sys

from db.sqlpractice2 import CustomersTableQuery
import logging
logger = logging.getLogger(__name__)
'''
This is another implementation of database manipulation using the CustomersTableQuery class and displaying it on Streamlit. This code first converts the SQL table into a Pandas dataframe before displaying.
'''

table2 = CustomersTableQuery()

value = table2.getCustomers(5)

df = pd.DataFrame(value)

def main():
	st.header("This takes the rows from getCustomers method and prints them after convering into Pandas dataframe")
	st.write(df)


if __name__ == '__main__':
	main()


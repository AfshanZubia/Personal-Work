#sqlstreamlit.py
import streamlit as st 
import sys
from db.sqlpractice2 import CustomersTableQuery
import logging
logger = logging.getLogger(__name__)
'''
This class is an implementation of dabatase manipulation and displaying it on Streamlit, a popular frontend UI.
'''


def main():
	st.header("This is the sql assignment")

	row1 = {
		'FirstName': 'Afshan',
		'Lastname': 'Akmal',
		'Company': 'NJIT',
		'Address': '35 Clark Avenue',
		'City': 'Edison',
		'State': 'NJ',
		'Country': 'USA',
		'PostalCode': '08817',
		'Phone': '848-668-3611',
		'Fax': 'idk',
		'Email': 'afshanzubia.akmal05@gmail.com',
		'SupportRepId': 'idkeither'
	}

	row2 = {

                'FirstName': 'Haneef',
                'Lastname': 'Jijaji',
                'Company': 'NVIDIA',
                'Address': 'somewhere in cali',
                'City': 'Milpitas',
                'State': 'CA',
                'Country': 'USA',
                'PostalCode': 'idklol',
                'Phone': 'hisphone#',
                'Fax': 'idkk',
                'Email': 'jijaji@gmail.com',
                'SupportRepId': 'idkidk'
        }

	newtable = CustomersTableQuery()
	newtable.insertCustomers(row1)
	st.write(newtable.getCustomers(10))

if __name__ == '__main__':
        main()

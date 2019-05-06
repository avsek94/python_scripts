#!/usr/src/Python-3.7.2/python
user = { 'admin': True, 'active': True, 'name': 'Abhishek'}
prefix = ""

if user['active'] and user['admin']:
    prefix = "ACTIVE - (ADMIN)"
elif user['admin']:
    prefix = "(ADMIN)"
elif user['active']:
    prefix = "ACTIVE - "

print(prefix + user['name'])

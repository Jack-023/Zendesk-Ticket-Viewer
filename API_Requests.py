#! python3

# This module handles Zendesk API requests

import requests

def get_user_dictionary(domain, usr, pwd):
    # Takes sub-domain, user email and password. Returns a dictionary that maps user id's to their name

    # here set up user list
    url = 'https://{sub_domain}.zendesk.com/api/v2/users.json'.format(sub_domain=domain)
    # Do the HTTP get request
    users = requests.get(url, auth=(usr, pwd))

    # Check for HTTP codes other than 200
    if users.status_code != 200:
        print('Status:', users.status_code, 'Problem with the request. Exiting.')
        exit()


    user_dic = {}

    user_data = users.json()

    for entry in user_data['users']:
        user_dic[entry['id']] = entry['name']

    return user_dic

def get_tickets(domain, usr, pwd):
    # Takes sub-domain, user email address and password and returns a dictionary containing the returned JSON from the
    # API call

    url = 'https://{sub_domain}.zendesk.com/api/v2/tickets.json'.format(sub_domain=domain)

    # Do the HTTP get request
    res = requests.get(url, auth=(usr, pwd))

    # Check for HTTP codes other than 200
    if res.status_code != 200:
        print('Status:', res.status_code, 'Problem with the request. Exiting.')
        exit()

    j = res.json()


    while j['next_page'] != None: # this loop is needed to grab all tickets since each call only returns 100.
        url = j['next_page']
        res = requests.get(url, auth=(usr, pwd))
        data = res.json()
        print(j['tickets'])
        j['tickets'] += data['tickets']
        print(j['tickets'])
        j['next_page'] = data['next_page']
        print(url, j['next_page'])

    print(len(j['tickets']))
    return j
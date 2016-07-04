#! python3

import requests

def get_user_dictionary(domain, usr, pwd):

    # here set up user list
    url = 'https://{sub_domain}.zendesk.com/api/v2/users.json'.format(sub_domain=domain)
    # Do the HTTP get request
    users = requests.get(url, auth=(usr, pwd))

    # Check for HTTP codes other than 200
    if users.status_code != 200:
        print('Status:', res.status_code, 'Problem with the request. Exiting.')
        exit()


    user_dic = {}

    user_data = users.json()

    for entry in user_data['users']:
        user_dic[entry['id']] = entry['name']

def get_tickets(domain, usr, pwd):
    url = 'https://{sub_domain}.zendesk.com/api/v2/tickets.json'.format(sub_domain=domain)

    # Do the HTTP get request
    res = requests.get(url, auth=(usr, pwd))

    # Check for HTTP codes other than 200
    if res.status_code != 200:
        print('Status:', res.status_code, 'Problem with the request. Exiting.')
        exit()

    return res.json()
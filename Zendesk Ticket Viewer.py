#! python3

import json, requests
import InputHandler


while (True):

    print("Welcome to Zendesk Ticket Viewer by Jack Jordan.")

    domain = InputHandler.get_domain()

    usr, pwd = InputHandler.get_acc()

    url = 'https://{sub_domain}.zendesk.com/api/v2/tickets.json'.format(sub_domain = domain)

    # Do the HTTP get request
    res = requests.get(url, auth=(usr,pwd))

    # Check for HTTP codes other than 200
    if res.status_code != 200:
        print('Status:', res.status_code, 'Problem with the request. Exiting.')
        exit()


    else:
        tickets = res.json()

        print(tickets)

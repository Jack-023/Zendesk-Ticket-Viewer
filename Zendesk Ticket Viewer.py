#! python3

import json, datetime, calendar
import InputHandler, API_Requests as api


while (True):

    print("Welcome to Zendesk Ticket Viewer by Jack Jordan.")

    domain = InputHandler.get_domain()

    usr, pwd = InputHandler.get_acc()

    tickets = api.get_tickets(domain, usr, pwd)

    print(tickets)

    user_dic = api.get_user_dictionary(domain, usr, pwd)
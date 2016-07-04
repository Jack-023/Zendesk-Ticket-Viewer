#! python3

# This is the main file for Zendesk Ticket Viewer.
# This is a command line program that uses the Zendesk API to display ticket information.

import InputHandler, API_Requests as api


print("Welcome to Zendesk Ticket Viewer by Jack Jordan.")

domain = InputHandler.get_domain()

usr, pwd = InputHandler.get_acc()

# print(domain, usr, pwd)

InputHandler.tickets = api.get_tickets(domain, usr, pwd)

InputHandler.user_dic = api.get_user_dictionary(domain, usr, pwd)

InputHandler.current_page = 1

InputHandler.main_input(None)

while True:

    InputHandler.main_input(input("Enter a ticket number to view that ticket or enter one of the letters in brackets" +
                                  " below:\n" +
                                  "(N)ext page.\n" +
                                  "(P)revious page.\n" +
                                  "(Q)uit\n\n> "))

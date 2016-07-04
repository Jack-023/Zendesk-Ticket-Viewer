#! python3

# This module handles user input for Zendesk Ticket Viewer

import getpass, re
import OutputHandler

# Variables related to handling tickets, we store them here so this module can easily make changes to them.
current_page = 0
user_dic = {}
tickets = {}

def get_user_name():
    # Ask the user for their Zendesk email address. Uses very basic sanity check, if the email is invalid
    # the request will fail anyway.
    valid_input = False
    regex = re.compile(r'[^@]+@[^@]+\.[^@]+')


    while (not valid_input):
        # usr = input("Please enter your email address: ")
        f = open('acc.txt', 'r')
        usr = f.readline().strip()
        usr = f.readline().strip()
        f.close()

        valid_input = re.fullmatch(regex, usr)
        if not valid_input:
            print("Incorrect email address.", usr)

    return usr


def get_pwd():
    f = open('acc.txt', 'r')
    usr = f.readline().strip()
    usr = f.readline().strip()
    usr = f.readline().strip()
    f.close()
    return usr

    return getpass.getpass("Please enter your password: ")


def get_domain():
    # return input("Please enter your Zendesk sub-domain (eg. sub_domain in  {sub_domain}.zendesk.com): ")
    f = open('acc.txt', 'r')
    usr = f.readline().strip()
    f.close()
    return usr

def get_acc():
    usr = get_user_name()

    pwd = get_pwd()

    return (usr, pwd)


def main_input(inp):
    # Handle the input in the main event loop.

    global current_page, user_dic, tickets

    if inp == None:
        # This happens the first time the function is called.
        OutputHandler.print_page(current_page, user_dic, tickets)

    elif inp.lower() == 'n':
        if current_page < len(tickets['tickets']) // 25 + 1:
            current_page += 1
            OutputHandler.print_page(current_page, user_dic, tickets)

        else:
            print("You are on the last page, you can't go forward any further.")

    elif inp.lower() == 'p':
        if current_page > 1:
            current_page -= 1
            OutputHandler.print_page(current_page, user_dic, tickets)

        else:
            print("You are on the first page, you can't go back any further.\n")

    elif inp.isdigit():
        id = int(inp)
        OutputHandler.print_ticket(current_page, user_dic, tickets, id)

    elif inp.lower() == 'q' or inp.lower() == 'quit':
        quit()
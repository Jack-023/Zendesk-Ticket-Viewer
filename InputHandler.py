#! python3

import getpass, re

def get_user_name():
    valid_input = False
    regex = re.compile(r'[^@]+@[^@]+\.[^@]+')


    while (not valid_input):
        usr = input("Please enter your email address: ")

        valid_input = re.fullmatch(regex, usr)
        if not valid_input:
            print("Incorrect email address.", usr)

    return usr

def get_pwd():
    return getpass.getpass("Please enter your password: ")

def get_domain():
    return input("Please enter your Zendesk subdomain (eg. sub_domain in  {sub_domain}.zendesk.com): ")

def get_acc():
    usr = get_user_name()

    pwd = get_pwd()

    return (usr, pwd)
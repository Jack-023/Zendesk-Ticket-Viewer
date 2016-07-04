#! python3

# This module handles the formatting of detailed output. It does not include single line outputs, they are
# handled where appropriate.

import datetime, calendar


def print_page(curr_page, user_dic, tickets):

    # Print the current page of tickets to the console.

    print('Displaying tickets. Page', str(curr_page), 'of', str(len(tickets['tickets']) // 25 + 1) + '.\n')

    for t in tickets['tickets'][(curr_page-1) * 25:curr_page * 25]:
        created = datetime.date(int(t['created_at'][:4]), int(t['created_at'][5:7]), int(t['created_at'][8:10]))

        # this is pretty a pretty nasty looking print call but it formats the output nicely.
        print('Ticket', str(t['id']) + ':', t['subject'][:20].rstrip() + ('...' if len(t['subject']) > 20 else ''),
              'requested by', (user_dic[t['requester_id']] if t['requester_id'] in user_dic else t['requester_id']),
              'on', calendar.day_abbr[created.weekday()], calendar.month_abbr[created.month], str(created.day),
              str(created.year))

    print() # Newline for nicer formatting

def print_ticket(curr_page, user_dic, tickets, id):
    # Prints the info for a specific ticket on the current page.
    done = False
    for t in tickets['tickets'][(curr_page-1) * 25:curr_page * 25]: #search through tickets on the current page.
        if int(t['id']) == id:
            created = datetime.date(int(t['created_at'][:4]), int(t['created_at'][5:7]), int(t['created_at'][8:10]))
            print("Ticket", str(id) + ':', t['subject'])
            print('requested by',
                  (user_dic[t['requester_id']] if t['requester_id'] in user_dic else t['requester_id']),
                  'on', calendar.day_abbr[created.weekday()], calendar.month_abbr[created.month], str(created.day),
                  str(created.year))
            print() #for nicer formatting
            print(t['description'])

            done = True
            break
    if not done:
        print("Ticket with id {id} not found on the current page.".format(id=id))

    print()  # for nicer formatting
    input("Press enter to continue.")

    print_page(curr_page, user_dic, tickets)
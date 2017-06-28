'Goal:  Learn common practices for REST APIs'

# The Github REST API is documented at:
# https://developer.github.com/v3/

import json
import urllib

def show_user_info(user):
    "Display a Github User's name, company, and contact info"
    # C API:   struct UserInfo * = get_user_info(char *user)
    #          info = get_user_info("raymondh");
    # REST API:        https://api.github.com/users/<username>
    #          json <- https://api.github.com/users/raymondh
    url = 'https://api.github.com/users/' + user
    u = urllib.urlopen(url)
    info = json.load(u)
    print '%(name)s works at %(company)s.  Contact at %(email)s' % info

if __name__ == '__main__':

    show_user_info('raymondh')
    show_user_info('hugs')

'''
Q. What the heck is a REST API?

A. A company typically has two APIs for accessing data
   1. A human facing API, so typically a url request returns HTML
   2. A computer facing API, so typically a url request returns JSON, XML, CSV

Q. Who are the Parties?
    Github has a human facing API at:  www.github.com
    and a computer facing API at:      api.github.com/


'''

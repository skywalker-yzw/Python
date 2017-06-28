''' An old, true, and sordid tale of Python
    featuring raisins, checkerboards, business cards,
    pushy relatives, and getting much needed rest.
'''

import csv
import urllib

# Acquire a QR code in PNG from the Google Chart REST API documented at:
# https://developers.google.com/chart/infographics/docs/qr_codes
root_url = 'https://chart.googleapis.com/chart?'

vcard_template = '''\
BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s %s
ORG:Raisins R Us, Inc.
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK;PREF:;;100 Flat Grape Dr;Fresno;CA;95555;United States of America
EMAIL:%s
REV:20160914T195243Z
END:VCARD
'''

def make_qr_code(text):
    'Generate a QR code in a PNG file format using the Google Chart REST API'
    query = dict(cht='qr', chs='300x300', chl=text)
    url = root_url + urllib.urlencode(query)
    u = urllib.urlopen(url)
    return u.read()

def make_vcard(fname, lname, title, phone, email):
    'Create an electronic business card in the VCard 2.1 format'
    return vcard_template % (lname, fname, fname, lname, title, phone, email)

if __name__ == '__main__':
    with open('notes/raisin_team_update.csv') as f:
        for lname, fname, title, email, phone in csv.reader(f):
            vcard = make_vcard(fname, lname, title, phone, email)

            filename = '%s_%s_%s.vcf' % (lname, fname, email)
            with open(filename, 'w') as vcard_file:
                vcard_file.write(vcard)

            image = make_qr_code(vcard)
            filename = '%s_%s.png' % (fname, lname)
            with open(filename, 'wb') as image_file:
                image_file.write(image)

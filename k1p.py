#!/usr/bin/env python

import logging

import ConfigParser
import argparse
from jinja2 import Environment, PackageLoader
from bs4 import BeautifulSoup

# Setup logging
script_name = os.path.splitext(os.path.basename(__file__))[0]
logging.basicConfig()
logger = logging.getLogger(script_name)
logger.setLevel(logging.DEBUG)

# Parse command line options
parser = argparse.ArgumentParser(
    description='Converts KeePass XML file to 1Password CSV')
parser.add_argument('--version', action='version', version='%(prog)s 0.1.0')
args = parser.parse_args()

# Read config file
config = ConfigParser.SafeConfigParser()
config.read(os.path.join('etc', script_name + '.conf'))

passwords_xml = BeautifulSoup(open(config.get('General', 'input')))
logger.info('KeePass XML file is opened')

passwords = []

for entry in passwords_xml.find_all('entry'):
  password['title'] = entry.title.string
  password['username'] = entry.username.string
  password['password'] = entry.password.string
  password['url'] = entry.url.string
  password['notes'] = entry.comment.string

  passwords.append(password)

# Prepare output file
env = Environment(loader=PackageLoader('__main__', 'templates'))
template = env.get_template('passwords.tmpl')
output = open(config.get('General', 'output'), 'w')
output.write(template.render(passwords = passwords).encode('utf-8'))
output.close()

logger.info('1Password CSV file is written')

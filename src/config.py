from __future__ import print_function
import argparse

parser = argparse.ArgumentParser(description='cmdArgs')
parser.add_argument('--output', type=str, default='slack_data.csv')
help=('filename to write analysis output in CSV format')  
parser.add_argument('--path', required=True, type=str, help='sys.path')
parser.add_argument('--channel', type=str, default='path_channel', help='channels.json')
parser.add_argument('--userfile', type=str, default='user_profile', help='users.json')

cfg = parser.parse_args()
#print(cfg)
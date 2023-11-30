import os, sys
import json
import argparse
import os
import io
import shutil
import copy
from datetime import datetime
from pick import pick
from time import sleep
import utils as utils
from loader import SlackDataLoader
# Initialize DataLoader
data_loader = SlackDataLoader(sys.path)
# Load data from a Slack channel
#data_loader.get_channels
#get_channel_message
#get_users(self)
#get_channels(self)
#get_user_map(self)
slack_data = data_loader.load_slack_data("path/to/slack_channel_data")
# from colorama import Fore
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def empty_name():
  print(bcolors.FAIL + 'Creation of directory failed! ' + bcolors.ENDC)
  sys.exit(1)

def failure_msg(app_name):
  print(bcolors.FAIL + 'Creation of directory failed! ' + bcolors.ENDC)
  sys.exit(1)

def success_msg(app_name):
  print(bcolors.OKGREEN + 'Creation of directory success: ' + app_name + bcolors.ENDC)

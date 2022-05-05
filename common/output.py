class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    print(bcolors.HEADER + text + bcolors.ENDC)

def print_warning(text):
    print(bcolors.WARNING + text + bcolors.ENDC)

def print_errror(text):
    print(bcolors.FAIL + text + bcolors.ENDC)
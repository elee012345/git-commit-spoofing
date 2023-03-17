import subprocess
import argparse
import os
import datetime
import re
import random


def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '


    ending = '\n' if current >= total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)


parser = argparse.ArgumentParser(description="A program to spoof commits to GitHub so that potential employers won't see that you're lazy and don't actually code lol\nOnly tested on Windows idk if it works on Linux or anything else")
parser.add_argument("-rp", "--repo_path", default=None, nargs=1, metavar="path", type=str, help="The path of the repo you want to spoof commit dates to")
parser.add_argument("-sd", "--start_date", default=None, nargs=1, metavar="short git date", type=str, help="The date to start spoofing commits to in Git's 'short' date format (YYYY-MM-DD)")
parser.add_argument("-ed", "--end_date", default=None, nargs=1, metavar="short git date", type=str, help="The date to stop spoofing commits to in Git's 'short' date format (YYYY-MM-DD)")
parser.add_argument("--blatant", default=False, nargs=1, metavar="boolean", type=bool, help="Whether you want the commits to look blatant and suspicious or natural and not sus")


args = parser.parse_args()
path = args.repo_path[0]

git_start_date = args.start_date[0]
git_end_date = args.end_date[0]
blatant = args.blatant[0]

try:
    if ( len(git_end_date) != 10 or len(git_start_date) != 10 ):
        raise Exception("Bad Date Format")
    # regex for correctly formatted date string 
    if ( re.search( "[1-2][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", git_start_date ) == None or re.search( "[1-2][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", git_end_date ) == None ):
        raise Exception("Bad Date Format")
    
    start_date = datetime.date(int(git_start_date[0 : 4]), int(git_start_date[5 : 7]), int(git_start_date[9 : 11]))
    end_date = datetime.date(int(git_end_date[0 : 4]), int(git_end_date[5 : 7]), int(git_end_date[9 : 11]))
except:
    print("Invalid date(s)!")
    exit()

num_days = abs(start_date - end_date).days


if not os.path.exists(args.repo_path[0]):
    print("Path does not exist!")
else:
    print("Spoofing commits...")
    spoof_date = start_date
    toggle_write = True
    spoof_to = open(args.repo_path[0] + "\\spoof", "w")
    subprocess.run( "git add spoof", shell=True, cwd=path )
    spoof_to.close()
    should_commit = [True, True, False]
    for i in range(num_days):
        if ( random.choice(should_commit) ):
            num_commits = random.randint(1, 5)
            for j in range(num_commits):
                spoof_to = open(args.repo_path[0] + "\\spoof", "w")
                if ( toggle_write ):
                    spoof_to.write("\n")
                    toggle_write = False
                else:
                    spoof_to.write("")
                    toggle_write = True
                spoof_to.close()
                subprocess.run( "git commit -a -m \"spoof\" --date=format:short:" + str(spoof_date.year) + "-" + str(spoof_date.month) + "-" + str(spoof_date.day), shell=True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT )
        spoof_date += datetime.timedelta(days=1)
        progress_bar(i, num_days)
    progress_bar(num_days, num_days)
    os.remove(args.repo_path[0] + "\\spoof")
    subprocess.run( "git commit -a -m \"spoof\" --date=format:short:" + str(spoof_date.year) + "-" + str(spoof_date.month) + "-" + str(spoof_date.day), shell=True, cwd=path, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT )
    print("Done!")
        

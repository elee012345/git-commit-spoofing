# git-commit-spoofing
Create fake activity on your GitHub profile.

A while ago, I wondered if I could change my commit dates, if, say, I forgot to commit one day and wanted to make the commit appear to be on that day. Well, commits are controlled locally, so it seemed possible. Then did that mean that people could fake their commits and spoof fake activitty to GitHub? Everything is done locally, after all. It turns out git has a built in feature to let you do this.

Example call:
```cmd
python spoof.py -rp "C:\Users\Ethan\Documents\coding-stuff\spoofing-repo-hahaha" -sd 2023-01-01 -ed 2023-03-16
```
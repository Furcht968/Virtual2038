@echo off
git add .
git commit -m %1
git branch -M master
git push -u origin master
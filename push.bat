@echo off
git add .
git commit -m %1
git branch -M main
git remote add origin https://github.com/Furcht968/Virtual2038.git
git push -u origin main
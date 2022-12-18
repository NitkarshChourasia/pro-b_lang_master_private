#!/bin/sh

# Script made by me, Nitkarsh Chourasia.
cd /home/nitkarshc/Desktop/Programmed?/downloadedScrapedEdabitCodes

mv *.cpp ../originalEdabitScraped/C++
mv *.java ../originalEdabitScraped/Java
mv *.py ../originalEdabitScraped/Python
mv *.js ../originalEdabitScraped/JavaScript

cd ../originalEdabitScraped
git add --all
git commit -S -m "Latest files being uploaded at `date +%F %T`"
git push
git fetch
git pull
git push


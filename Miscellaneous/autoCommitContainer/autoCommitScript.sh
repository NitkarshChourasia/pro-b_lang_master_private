#!/bin/sh

# Script made by me, Nitkarsh Chourasia.

cd /home/nitkarshc/Desktop/Programmed?/downloadedScrapedEdabitCodes

mv *.cpp /home/nitkarshc/Desktop/Programmed?/originalEdabitScraped/C++
mv *.java /home/nitkarshc/Desktop/Programmed?/originalEdabitScraped/Java
mv *.py /home/nitkarshc/Desktop/Programmed?/originalEdabitScraped/Python
mv *.js /home/nitkarshc/Desktop/Programmed?/originalEdabitScraped/JavaScript
mv *.cs /home/nitkarshc/Desktop/Programmed?/originalEdabitScraped/C#

cd /home/nitkarshc/Desktop/Programmed?/originalEdabitScraped
git add --all
git commit -S -m "Latest files being uploaded at `date +%F-%T`"
git push
git pull
git push

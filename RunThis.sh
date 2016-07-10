#!/bin/bash

#wget -O instagram.html "https://www.instagram.com/kinfolk/"
wget -O instagram.html "https://www.instagram.com/time/"
echo "" > index.html
echo "./scrape.py >> index.html"
./scrape.py >> index.html
# Facebook Massive Picture Downloader

Python script to automatically download any number of Facebook pictures given a list of their FBIDs.

## About

Facebook has a tool that allows any user to download all the pictures they have uploaded. However, it does not allow to automatically download all the pictures that one's been tagged in. In fact, this can be a hard task. This script tries to make the task easier. Nevertheless, it works for any list of FBIDs of pictures.

This script is in no way efficient; it could be parallelized and made more robust. This is just a one-off task I needed solved, and decided to upload my solution for anybody else that might need it. I'm not responsible for any consequence of the usage of these files.

## Instructions

### Get the FBID of the pictures to download

Facebook assigns a unique identification number ("FBID") to every picture uploaded. We first need to obtain a list of the FBIDs of the pictures we want to download.

In case we want to download all the pictures we've been tagged in, we can follow [these](https://github.com/gnmerritt/gnmerritt.net/issues/1#issuecomment-407623247) steps. We generate a file containing all the FBID numbers, one per line. Save this file as `list.txt` in the same folder as the Python script.

### Get your browser cookies

Facebook, naturally, only allows access to the pictures if you're logged in. Luckily, this can be emulated in `curl` by using a `cookies.txt` file. This file is supposed to contain all the cookies that your browser has saved. To obtain it, one can use a browser extension. I used [this one](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/) for Firefox.

First, make sure you log into Facebook with the keep me logged in option checked. Then, export the file as `cookies.txt` and save it in the same folder as the Python script.

### Execute the script

Run, using Python 3:

    python download.py

The script will create an `output` folder and save the pictures there, keeping their original modification timestamp (whenever they were uploaded to Facebook). The pictures will be named `YYYYMMDD.jpg` according to this date, with numbering (`YYYYMMDD 1.jpg`, etc.) in case there are two or more pictures with the same date.

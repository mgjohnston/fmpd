import subprocess
import re
import os
import time

# This can be any valid agent string
AGENT = '"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"'
OUTPUT_FOLDER = 'output/'
TEMP = 'temp.jpg'
EXT = '.jpg'
COOKIES_FILE = 'cookies.txt'
FBID_FILE = 'list.txt'
PREFIX = 'https://m.facebook.com/photo/view_full_size/?fbid='

os.mkdir(OUTPUT_FOLDER)

with open(FBID_FILE) as fbids:
    for fbid in fbids:
        fbid = fbid.rstrip()

        # The fbid URL doesn't point to the picture but to a page that generates a URL for the file. Get that URL
        redirect = subprocess.check_output(['curl', '--cookie', COOKIES_FILE, '-A', AGENT, PREFIX + fbid]).decode("utf-8")
        print(PREFIX+fbid)
        FinalwNone = re.search(r'(?<=url=).*?(?=")', redirect)
        if FinalwNone is None:
            continue
        final = re.search(r'(?<=url=).*?(?=")', redirect).group(0).replace('&amp;', '&')
        print (type(final))

        # Download the actual pic
        subprocess.Popen([
            'curl',
            '--remote-time', # Keep the timestamp
            '--cookie', COOKIES_FILE, # Use cookies so Facebook lets us in
            '-A', AGENT, # Tell Facebook we are some browser instead of curl
            '--output', TEMP, # File destination
            final, # URL to retrieve
        ]).wait() # Wait for subprocess to finish before accessing the file

        # Get the timestamp
        stamp = time.strftime('%Y%m%d', time.localtime(os.path.getmtime(TEMP)))

        # Rename avoiding duplicates
        name = stamp + EXT
        i=1
        while os.path.isfile(OUTPUT_FOLDER + name):
            # Another file with the same date already exists, add a number
            name = stamp + ' ' + str(i) + EXT
            i+=1
        os.rename(TEMP, OUTPUT_FOLDER + name)

#PiStats
##Description
A simple REST API made with Python\'s Flask Framework.

##Setup
1. Clone this repository with `git clone https://github.com/Naoto-Ida/PiStats-Server.git` in your Pi.
2. `pip install` all the packages in `requirements.txt`
3. Do `python runserver.py`
4. In your browser, access your Pi\'s local IP at port 5000(Default basic auth is "rpi").

##Usage
`GET /disk` will get you information on your disk, in JSON format.

##TODO
1. Make a batch program to schedule a check on the device, then store into a local database.
2. Give the user options to get real-time information or stored information

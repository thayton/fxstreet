# fxstreet
Scraper to get the data from the table titled "Major Central Banks Overview"
from the page at http://www.fxstreet.com/economic-calendar/world-interest-rates/

# Setup

Setup a virtual environment:

    $ virtualenv venv
    $ source venv/bin/activate

Install dependences (BeautifulSoup and Requests):

    $ pip install requirements.txt

Run the scraper:

    $ ./scraper.py 
    Reserve Bank of Australia,2.000,2015-11-03 - 03:30,2015-10-06 - 03:30
    Federal Reserve,0.250,2015-10-28 - 19:00,2015-09-17 - 18:00
    Swiss National Bank,-0.750,2015-12-10 - 07:30,2015-09-17 - 07:30
    European Central Bank,0.050,2015-10-22 - 11:45,2015-09-03 - 11:45
    Bank of Japan,0.100,2015-10-30 - 03:00,2015-10-07 - 03:00
    Reserve Bank of New Zealand,2.750,2015-10-28 - 20:00,2015-09-09 - 21:00
    Bank of Canada,0.500,2015-10-21 - 14:00,2015-09-09 - 14:00
    Bank of England,0.500,2015-11-05 - 11:00,2015-10-08 - 11:00

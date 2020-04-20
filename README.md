# SAE Data Scraper
collects results data from sae.org and returns them in a more usable format


This first script has no dependencies

`python3 getResults.py`
it downloads all of the results for formula sae (non electric vehicle) from sae.org into the current directory
you can also run the exe file if you don't have python installed, the folder 'scraped results' contains the output from this script


The next script has extra dependencies it requires the installation of 2 libraries, and potentially another non python library depending on what system you're running

`pip3 install -r requirements.txt`

`python3 fsae.py "PATH_TO_PDF.pdf"`

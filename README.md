# sample

usage: logparser.py [-h] [--sort-order {Ascending,Descending}] [--verbose]
                    F [F ...]

positional arguments:
  F                     List of files to process

optional arguments:
  -h, --help            show this help message and exit
  --sort-order {Ascending,Descending}
                        Order to sort output
  --verbose             Display process information


This is a simple script to parse a log file. It takes a list of files as input. Output is a sorted list of which url received the most traffic and which url received the most unique traffic. The expected input is <URL-PATH> <IP-ADDRESS>. There are safety checks to ensure there are exactly two columns in the input file, but checks to see if the entries are valid url-paths or ip address.

 

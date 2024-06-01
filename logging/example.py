#This method is used to config the logging system
# basicConfig(**kwargs)
# filename
# filemode
# level
# format
# datefmt
# style


from logging import *

LOG_FORMAT='{lineno} *** {name} *** {asctime} *** {message} '
basicConfig(filename='logfile.log',
            level=DEBUG,
            filemode='w',
            style='{',
            format=LOG_FORMAT)

debug("This is debug")
info("This is info")
warning("This is warning")
error("This is Error")
critical("This is critical")


""" 
Version 0.1 28th April 2020 Framework to create pypi package
  

Pete White
This is a Python module to simplify operations via F5 Declarative Onboarding interface. 
No support or liability is assumed

Install using pip: pip install DO

see README.rst and examples for more detail on usage

"""
###############################################################################
import os
import sys
import json
import requests
# Disable warnings about insecure
if sys.version_info[0] < 3:
  # Python 2:
  from requests.packages.urllib3.exceptions import InsecureRequestWarning
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
else:
  # Python 3:
  import urllib3
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DO:
   
  def __init__(self,hostname,username = "admin",password = "admin",**kwargs):
    # Setup variables
    pass
  pass
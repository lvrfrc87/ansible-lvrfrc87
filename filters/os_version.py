#!/usr/bin/python
import re

class FilterModule(object):
    def filters(self):
        return { 'os_version_filter': self.os_version_filter }


    def os_version_filter(self, stderr_var):
        match = re.search(r'(?<=ersion\s)\w+.\d', stderr_var, re.M)
        os_version = match.group()
        return float(os_version)

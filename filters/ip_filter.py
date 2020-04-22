#!/usr/bin/python
import re

class FilterModule(object):
    def filters(self):
        return { 'ip_filter': self.ip_filter }


    def ip_filter(self, stdout_var):
        match = re.search(r'\d+.\d+.\d+.\d+', stdout_var, re.M)
        ip_filter_match = match.group(0)
        return str(ip_filter_match)

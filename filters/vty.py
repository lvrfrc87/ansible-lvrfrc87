#!/usr/bin/python
import re

class FilterModule(object):
    def filters(self):
        return { 'vty_filter': self.vty_filter }

    def vty_filter(self, stderr_var):
        match = re.search(r'<\d-(\d+)>', stderr_var, re.M)
        vty_max = match.group(1)
        return str(vty_max)


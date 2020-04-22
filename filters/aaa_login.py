#!/usr/bin/python
import re

class FilterModule(object):
    def filters(self):
        return { 'aaa_login': self.aaa_login }


    def aaa_login(self, stdout_var):
        match = re.search(r'login (\S+) group', stdout_var, re.M)
        aaa_login_filter = match.group(1)
        return str(aaa_login_filter)


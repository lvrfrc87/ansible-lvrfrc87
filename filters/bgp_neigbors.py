#!/usr/bin/env python3
# {
#   "bgp": {
#     "sessions": [
#       {
#         "peer": {
#           "neighbors": [
#             "10.76.100.4"
#           ], 
#           "route_map": {
#             "direction": "out", 
#             "name": "TO-SPINE-LAYER"
#           }, 
#           "remote_as": "64520", 
#           "allowas_in": "disabled", 
#           "name": "EBGP_SPINE1_64520"
#         }
#       }
#     ]
#   }
# }

class FilterModule(object):
    def filters(self):
        return { 'bgp_neigbors': self.bgp_neigbors }

    def bgp_neigbors(self, stdout_var):
        ip_list = list()
        final_list = list()


        for session in stdout_var.get('sessions'):
            for ip in session.get('peer').get('neighbors'):
                ip_list.append(ip)

        some_magic = sorted(
            ip_list,
            key=lambda ip: int(''.join(["%02X" % int(i) for i in ip.split('.')]), 16)
            )

        for ip in some_magic:
            for session in stdout_var.get('sessions'):
                if ip in session.get('peer').get('neighbors'):
                    final_list.append('neighbor {neighbor} peer group {name}'.format(
                        neighbor=ip,
                        name=session.get('peer').get('name')
                    ))
        return(final_list)

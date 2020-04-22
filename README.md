### RUN DOCKER
A docker container is provided with `ansible==2.9.5`, `napalm-ansible==1.0.0`, `pyateos-ansible==1.0.2`, `git-acp-ansible==1.0.4` and a bunch of custom filters.

Run the docker and mount the repo folder you cloned into `/git` i.e. `-v ~/git/my_repo/:/git` as well as the Vault file into `/root/` i.e. `-v ~/.my_vault:/root/.my_vault`

Full command example:

`docker run -dit -v ~/git/NaC/:/git -v ~/.v:/root/.v --name ansible-lvrfrc87 ansible-lvrfrc87`

Use `docker exec ansible-lvrfrc87` to run your ansible playbook.

Example:

`docker exec ansible-lvrfrc87 ansible-playbook -i inventory --limit device1.dev0 --diff my_playbook.yml --vault-password-file /root/.v`

If you don't want to run the full docker command, you can create and alias (restart terminal session after editing `.bash_profile`):

* `vi .bash_profile`
* `alias ansible-playbook='docker exec ansible-lvrfrc87 ansible-playbook'`
* `ansible-playbook -i inventory --limit device1.dev0 --diff my_playbook.yml --vault-password-file /root/.v`

### FILTERS

* `aaa_login.py` - find AAA group from `show run` in IOS
* `bgp_neighbors.py` - reorder BGP neighbors config lines in EOS
* `ip_filter.py` - fin IPv4 address in string
* `os_version.py` - find OS version from `show version` in IOS
* `vty.py` - find line vty number from `show run`
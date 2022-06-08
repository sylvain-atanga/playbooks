import subprocess
sylvain = 1
while sylvain <= 8:
    subprocess.call("ansible-playbook playbook%d.yml -b"%sylvain,shell=True)
    sylvain = sylvain + 1

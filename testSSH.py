import paramiko
hostname = '45.76.8.143' 
myuser   = 'root'
mySSHK   = '/root/.ssh/id_demo'
sshcon   = paramiko.SSHClient()  # will create the object
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())# no known_hosts error
sshcon.connect(hostname, username=myuser, key_filename=mySSHK) # no passwd needed


stdin, stdout, stderr = sshcon.exec_command('ps fax | grep ssh')

for line in stdout:
    print line.strip('\n')

sshcon.close()

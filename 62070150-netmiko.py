from netmiko import ConnectHandler

device_ip = '10.0.15.109'
username = 'admin'
password = 'cisco' 
loopback1 = 'loopback62070150'

device_params ={'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': username,
                'password': password
                }

def create():
    with ConnectHandler(**device_params) as ssh:
        ssh.send_command_timing("conf ter")
        interfaceb = ssh.send_command('do show ip interface brief')
        list_inf = interfaceb.strip().split('\n')
        
        for line in list_inf:
            y = line.split()
            if y[0] == 'Loopback62070150' and y[1]== "192.168.1.1":
                interfaceloop62070150 = y[0]
                iploop62070150 = y[1]
                print(interfaceloop62070150)
                print(iploop62070150)
            else:
                interfaceloop62070150 = ""
                iploop62070150 = ""
  
        if interfaceloop62070150 != "Loopback62070150" and iploop62070150 != "192.168.1.1":
            ssh.send_command_timing('interface '+loopback1)
            result = ssh.send_command('ip address 192.168.1.1 255.255.255.0')
            print(result)
            result = ssh.send_command('do show ip interface brief')
            print(result)
        else:
            result = ssh.send_command('do show ip interface brief')
            print(result)
            print("Create ERROR")
       
        

def delete():
    with ConnectHandler(**device_params) as ssh:
        ssh.send_command_timing("conf ter")
        interfaceb = ssh.send_command('do show ip interface brief')
        list_inf = interfaceb.strip().split('\n')
        for line in list_inf:
            y = line.split()
            if y[0] == 'Loopback62070150' and y[1]== "192.168.1.1":
                interfaceloop62070150 = y[0]
                iploop62070150 = y[1]
                
            else: 
                 
                interfaceloop62070150 = ""
                iploop62070150 = ""
  
        if interfaceloop62070150 == "Loopback62070150" and iploop62070150 == "192.168.1.1":
            ssh.send_command_timing('no interface '+loopback1)
            result = ssh.send_command('do show ip interface brief')
            print(result)
        else:
            result = ssh.send_command('do show ip interface brief')
            print(result)
            print("Delete ERROR")
            

def main():
    print("Create loop back type 1")
    print("Delete loop back type 2")
    
    input1 = str(input("Press your number:"))
    if input1 == "1":
        create()
    elif input1 == "2":
        delete()
    else:
        print("ERROR")
main()
        

    
    


   
IP_list = ['10.10.10.15', '10.10.10.1', '10.10.10.5', '10.10.10.255']

for IP in IP_list:
    if IP == '10.10.10.1':
        print(IP + ' is the gateway address')
    elif IP == '10.10.10.255':
        print(IP + ' is the broadcast address')
    else:
        print(IP + ' is a host address')


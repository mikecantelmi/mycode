def main():
    switch = {'hostname': 'sw-01', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}
    print( switch['hostname'] )
    print( switch['ip'] )

#    print( switch['lynx'] )
    print ("First test - .get()")
    print (switch.get('lynx'))

    print ("Second test - .get()")
    print (switch.get('linx', "The KEY IN IN ANOTHER CASTLE!"))

    print ("Third test - .get()")
    print (switch.get('version'))

    
main()


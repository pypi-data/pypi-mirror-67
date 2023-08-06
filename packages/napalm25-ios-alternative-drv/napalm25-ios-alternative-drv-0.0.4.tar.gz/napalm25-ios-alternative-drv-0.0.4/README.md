## alternative unofficial napalm ios driver

Due the purpose of NAPALM the included IOS Drivers are designed to require Privilege Exec Mode(aka Privilege Level 15) 
to ensure the full feature-set is always available.<br>
If this privilege level is not available the driver will not work.<br>
This limits its use for certain purposes where priv exec is not required. (like using the getters() or sending show commands)

This driver is a fork of the original driver, it changes the behavior of the driver and implements privilege level checking.
It will allow to connect without privilege level 15 and instead raise permission-errors whenever a function is called and the required privilege level is not available. <br>
It will neither change function arguments or return values nor implement new functions. 


## install
 
    pip install napalm-ios-alternative-drv
    
## usage 

   without secret: 
    
    #!/usr/bin/env python3
    from napalm import get_network_driver
    driver = get_network_driver('ios_ad')      
    device = driver('1.1.1.1', 'username', 'password')
    device.open()    
    vals = device.get_facts()   
    print(vals)    
    device.close()

   with secret: 
    
    #!/usr/bin/env python3
    from napalm import get_network_driver
    optional_args = { 'secret': '<enable_secret>'}
    driver = get_network_driver('ios_ad')      
    device = driver('1.1.1.1', 'username', 'password', optional_args=optional_args)
    device.open()    
    vals = device.get_facts()   
    print(vals)    
    device.close()
    

## Authors:

The largest part of the codebase is sync'd from and belongs to the [NAPALM Project](https://github.com/napalm-automation/napalm/).<br>
Privilege Patches are done by me.


Original Authors(NAPALM Project)
 * David Barroso ([dbarrosop@dravetech.com](mailto:dbarrosop@dravetech.com))
 * Elisa Jasinska ([elisa@bigwaveit.org](mailto:elisa@bigwaveit.org))
 * Many others, check the [napalm contributors](https://github.com/napalm-automation/napalm/graphs/contributors) page for details.

Privilege Patches
  * remingu <remingu@techturn.de>


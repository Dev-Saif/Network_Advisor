Home :
    [Enterprise]
    - enterprise name
    - enterprise img 
    - public ip
    - join [function]   
    - [requests] [FK]
        - floor num
        - dept. num
        - room type
        - room name 
        - use type
        - users. num
    
Enterprise :
    - enterprise name
    - enterprise img
    - Admin name 
    - public ip
    - users num
    - requests num
    [functions]
    - view 

Workspace :
    - project name
    - [Network]
    - [Hardware]
    - [Software]
    - total cost
    - total time
    - workers num
    [functions]
    - add
    - calculate
    - modify
    - expand
    - design
    - remove

Network : 
    [Building]
    - building name
    - connection type (db1)
    - network topology [FK]
    - [floor] [FK]
        - floor num
        - connection
        - topology
        - [dept] [FK]
            - dept name
            - connection
            - topology
            - [room] [FK]
                - room name
                - room type
                - connection
                - topology
    
Hardware :
    - network devices
    - end devices
    - Transmission media (db2)
    - cost      
    - time

Software :

Equipments :

Account :
    - username
    - email
    - password
    - public ip
    - [profiles] [FK]
        - enduser name
        - enduser Img        
        - floor num
        - dept. num        
        - room name
        - public ip 
        - privte ip
        [functions]
        - edit profile
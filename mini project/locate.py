from ip2geotools.databases.noncommercial import DbIpCity

def locate(ip):
    res = DbIpCity.get(ip,api_key="free")
    print(f"ip : {res.ip_address}")
    print(f"LOCATION : {res.city} , {res.region} , {res.city}")
    print(f"cordinate : Lat:{res.latitude}, Lon:{res.longitude}")

getIp = input("please enter your ip address : ")
locate(getIp)
# function for caching data from DB in redis
import subprocess
import time

def connect_redis():
    s = subprocess.check_output('docker ps', shell=True)
    if str(s).find('redis-py') != -1:
        print ('redis already started!')
    else:
        print ('not found.')
        s = subprocess.check_output('docker ps -a', shell=True)
        if str(s).find('redis-py') != -1:
            res = subprocess.run("docker start redis-py", shell=True)
            print("docker started redis-py")
        else:
            cmd_str = "docker run -p 6379:6379 -d --network=host --name redis-py redis"
            res = subprocess.run(cmd_str, shell=True) #if 0 - run succes
            print("docker ran redis-py")
        # time.sleep(1) #pause for redis container can started entirely
    return 0

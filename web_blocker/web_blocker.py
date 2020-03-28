import time
from datetime import datetime as dt

hosts_path = '/etc/hosts'
redirect = "127.0.0.1"
websites_list = ['www.vk.com', 'vk.com', 'ok.ru', 'www.ok.ru']
start_time = dt(dt.now().year, dt.now().month, dt.now().day, 21, 12)
end_time = dt(dt.now().year, dt.now().month, dt.now().day, 21, 13)

while True:
    if start_time < dt.now() < end_time:

        time.sleep(5)
        with open(hosts_path, 'r+') as file:
            content = file.read()
            print(content)
            for website in websites_list:
                if website in content:
                    pass
                else:

                    file.write(redirect + " " + website + "\n")

    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
    print(dt.now().time())

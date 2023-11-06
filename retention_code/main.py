import my_token
import helper
import push
from push import repo
import time

paths = input("Enter target path: ")
days = input(str("Enter retention period in days: "))
r_dirs = input(str("Enter retention dir count: "))
regex = input("Enter Capture Expression: ")
date_format = input("Enter date format: ")
_cron = input("Please choose cron in * * * * * ? format: \n")
              
dryRun = False
recursiveSearch = False

kinit= paths.split("/")

file_name = paths.replace("_", "-").replace("/", "-")
filename = file_name.replace("-group-", "") + f"-{days}d"



filed1 = "filed1"
value1 = (kinit[2])
filed2 = "/filed2"
value2 = filename
job_file = str("delete-" + value2 + ".job")

helper.meta_yml(filename, paths, days, r_dirs, regex, date_format, dryRun, recursiveSearch)
helper.delete_job(filed1, value1, filed2, value2, job_file)
time.sleep(1)
push.push_yml(filename)
push.push_job(job_file)
push.update_azk(_cron, value2)


#create pull request
time.sleep(2)
pr = repo.create_pull(base="release", head="moreyogesh748:main", title="Bot added new retention job")

time.sleep(2)
pulls = repo.get_pulls(state='open', sort='created', base='release')
for pr in pulls:
    a = pr.number
    print(f"\nPull request created & PR no. is : {a}")
#time. sleep(3)
#pull_request = repo.get_pull(a)
#pull_request.merge()
#print(f"\n PR {a} is merged")

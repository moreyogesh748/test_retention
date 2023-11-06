from github import Github
from my_token import token
from helper import *


my_git = Github(token)
for repo in my_git.get_user().get_repos():
    print(f"You are in: {repo.name}")


def push_yml(filename):
    yml_path = '/Users/mac/Downloads/code/retention_request_project/temp/' + filename +".yml"
    
    with open(yml_path, 'r') as file:
        content = file.read()
    git_prefix = 'deployment/configs/'
    git_file = git_prefix + filename + ".yml"

    repo.create_file(git_file, "committing files", content, branch="main")
    print("\n" + git_file + ' CREATED')

def push_job(job_file):
    job_path = "/Users/mac/Downloads/code/retention_request_project/temp/" + job_file
    delete_job = job_file
    with open(job_path, 'r') as file:
        content = file.read()
    git_prefix = 'deployment/azkaban/'
    git_file = git_prefix + delete_job
    repo.create_file(git_file, "committing files", content, branch="main")
    print("\n" + git_file + ' CREATED')



def update_azk(_cron, value2):
    # get the repository where the azkban.yml file exists

    sch = _cron
    repo = my_git.get_repo('moreyogesh748/test_retention')
    file = repo.get_contents('/deployment/configs/azkaban.yml')

    # get the current content of the azk file
    current_content = file.decoded_content.decode("utf-8")

    # appending new lines to the azk file
    new_lines = ["  - name: " + value2, "    schedule: " + sch, "    concurrency: skip"]
    updated_content = current_content + "\n" + "\n".join(new_lines)
    msg = "Bot added new schedule"

    # pushing updated the content of azk file to repo
    repo.update_file(file.path, msg , updated_content, file.sha)


















'''
def raise_pr():
    time. sleep(3)
    pr = repo.create_pull(base="release", head="moreyogesh748:main", title="Bot added new retention job")


def merge():
    time. sleep(3)
    pulls = repo.get_pulls(state='open', sort='created', base='release')

    for pr in pulls:
        a = pr.number
        print(a)

    time. sleep(3)
    pull_request = repo.get_pull(a)
    pull_request.merge()'''

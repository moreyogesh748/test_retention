import yaml

def meta_yml(filename, paths, days, r_dirs, regex, date_format, dryRun, recursiveSearch):
    data = {
    "name": filename,
    "parentDirs": [paths],
    "retentionDays": str(days),
    "retentionDirs": str(r_dirs),
    "captureDateRegexp": regex,
    "dateFormat": date_format,
    "dryRun": dryRun,
    "recursiveSearch": recursiveSearch

    }
    yml_file = str("/Users/mac/Downloads/code/retention_request_project/temp/" + filename + ".yml")

    with open(yml_file, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)

    print("\nyml file successfully wrote to ", yml_file)


def delete_job(filed1, value1, filed2, value2, job_file):
    yml_file = str("/" + value2 + ".yml")
    job_file = str("delete-" + value2 + ".job")
    job = ("/Users/mac/Downloads/code/retention_request_project/temp/" + job_file)
    with open('/Users/mac/Downloads/code/retention_request_project/job.txt', 'r') as file :
        filedata = file.read()

    filedata = filedata.replace(filed1, value1).replace(filed2, yml_file)
    with open(job, 'w') as file:
        file.write(filedata)
    print("\n job Successfully wrote to", job_file)

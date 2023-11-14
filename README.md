# Retention Automation

This project is designed to automate the retention setup process which is presently being accomplished manually.

How to use it !!

Just provide,
1. Target path
2. Retention days
3. Column name on which partitioning is done & written on HDFS

Provide the above information and it will generate yaml file, delete job file for azkaban and update azkaban.yml with schdule into repository.
also, the program will raise PR for you and can be merged as well. (for now, merge option is disabled in order to review by SRE)

# log4s3-



# Saving Log files to AWS S3 
####(hyphen in name is an intended pun :) )

## Motivation
Python logging saves files to file system. There is no S3 Driver (log handler) owing to fact that you can't append file on AWS S3. 

## Design
Rewrite `doRollOver`  method to copy all files AWS S3. Currently we overwrite files. But we can surely move (rename) files to 
save data transfer costs. is provided to explain usage. 


An example.py script is included in github. You want change certaing parameters like S3 URL, AWS Secret and Key and locartion of log file on disk.

## Prereq.
* AWS Accoount
* AWS S3 bucket 
* AWS IAM account with permission like CreateObject and LitBucket.


#Future Plans
* Driver to save Log entries to AWS DynamoDB


### Support

mvaidya@awanitech.com

forvaidya@awanitech.com

http://www.awanitech.com

+91-9740500144


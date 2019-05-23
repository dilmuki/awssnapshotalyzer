# awssnapshotalyzer
Project to manage AWS EC2 instance snapshots

## About

This project uses boto3 to manage AWS EC2 instance shapshots.

## Configuring

shotty uses the configuration file created by the AWS CLI. 
For example:

`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECTNAME>`
`pipenv run python shotty/shotty.py --help` for more help

*command* is instances, volumes, or snapshots
*subcommand* is depends on command
*project* is optional

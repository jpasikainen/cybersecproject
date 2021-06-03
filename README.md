# Cyber Security Base 2021 Project

## Running
Make sure you have django and python3 installed. Start server by running
```
python3 migrate.py runserver
```
in the project root.

## Analysis
Link https://github.com/jpasikainen/cybersecproject

Installation instructions: https://github.com/jpasikainen/cybersecproject/blob/master/README.md

FLAW 1:
https://github.com/jpasikainen/cybersecproject/blob/3d3f5e6890592ebc493f6ae9dbe1cdd86e668142/cybersecproject/settings.py#L23

A6:2017-Security Misconfiguration. The project was created using the django starter template which preconfigures the project for general use. This includes the creation of project_name/settings.py file which includes the configuration settings. This file is present at the project git repository. The most sensitive exposed information is the SECRET_KEY variable that is used for cryptographic signing. Exposing it "can lead to privilege escalation and remote code execution vulnerabilities". https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY

Fortunately, this is a very simple vulnerability to fix. For example, the file can be excluded from the repository on the .gitignore file or be regenerated on the production machine. However, if the key got exposed at any point, it must be replaced.
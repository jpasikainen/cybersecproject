# Cyber Security Base 2021 Project
The web project is a site where the users can write micro blogs.

## Running
Make sure you have django and python3 installed. Start server by running
```
python3 migrate.py runserver
```
in the project root.

## Analysis
# Cyber Security Base 2021 Project
The web project is a site where the users can write micro blogs.

## Running
Make sure you have Django and python3 installed. Start server by running
```
python3 migrate.py runserver
```
in the project root.

## Analysis
Link https://github.com/jpasikainen/cybersecproject

Installation instructions: clone the project, https://github.com/jpasikainen/cybersecproject/ , using git or by downloading it directly from the GitHub repository. Execute command "python migrate.py runserver" at the project root to start the server locally and test the project. The project should run on machines that have the previously installed dependencies used on the course.

By default the application does not include any posts or accounts. There is no special privileges on admin accounts. By default the site is accessible at http://localhost:8000/

FLAW 1:

https://github.com/jpasikainen/cybersecproject/blob/3d3f5e6890592ebc493f6ae9dbe1cdd86e668142/cybersecproject/settings.py#L23

A6:2017-Security Misconfiguration. The project was created using the Django starter template which preconfigures the project for general use. This includes the creation of project_name/settings.py file which includes the configuration settings. This file is present at the project git repository. The most sensitive exposed information is the SECRET_KEY variable that is used for cryptographic signing. Exposing it "can lead to privilege escalation and remote code execution vulnerabilities". (https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY)

Fortunately, this is a very simple vulnerability to fix. For example, the file can be excluded from the repository on the .gitignore file or be regenerated on the production machine. However, if the key got exposed at any point, it must be replaced.

FLAW 2:

https://github.com/jpasikainen/cybersecproject/blob/dedd481aa5d7c6e949b07bae7e308d39c86e7e85/cybersecproject/views.py#L23

A1:2017-Injection. An user can sign in to any account as long as they know the username. When the username is correct, using ' OR '1=1 as the password input fools the system. What happens is that the SQL query checks if the password is true or if one is equal to one. One is always equal to one so the login is successful.

The vulnerability can be fixed by taking out single quotes around the %s that get replaced with the entered credentials. Now when using the previous input, it is treated as the password and gets rejected. Alternative way is to use the Django ORM system as it prevents this misconfiguration by default. Django's ORM is used in the register process and does not contain the same vulnerability.

FLAW 3:

https://github.com/jpasikainen/cybersecproject/blob/dedd481aa5d7c6e949b07bae7e308d39c86e7e85/cybersecproject/views.py#L66

A5:2017-Broken Access Control. Creating an account with a space at the end or the beginning of the username allows impersonation. Now the user with this type of name has the access on the profiles of user with the same name not containing the space. The profile page for each user displays their credentials which is used to make the point why this matters. In some other web application, it could be the personal API key for example.

The issue is caused by strip function when matching profile name. Strip function removes the white-space around a string. The fix is easy as taking it out. Alternatively, it can be left there and prevent creating accounts that abuse this vulnerability.

FLAW 4:

https://github.com/jpasikainen/cybersecproject/blob/dedd481aa5d7c6e949b07bae7e308d39c86e7e85/cybersecproject/templates/pages/index.html#L35

A8:2017-Insecure Deserialization. This is perhaps the worst vulnerability on the project. When creating a post, an user can write anything that a normal HTML site can parse. This includes executing JavaScript code when it is added inside script-tags. Just by entering the site a normal user gets exposed to the vulnerability when the malicious post is loaded. The text area input is limited to 300 characters on the server-side, but an attacker can use that short space to execute code from their server. A very plain way to exploit this is to redirect the user to a malicious site.

This can be fixed by sanitizing the user input or by rendering everything as text. In that case, HTML tags would be visible and no JavaScript gets executed. In this particular project, the issue is caused by overriding the default setting of escaping HTML with the filter "safe". Removing it fixes the issue, but now the users cannot use formatting on their posts. Safe filter should never be used on data from the users.

FLAW 5:

https://github.com/jpasikainen/cybersecproject/blob/dedd481aa5d7c6e949b07bae7e308d39c86e7e85/cybersecproject/views.py#L29

A10:2017 Insufficient Logging & Monitoring. The project does not do any logging and thus cannot detect abuse or attacks against it. Bruteforcing a password does not get detected and eventually the attacker can get in. There is also no rate limiting on the speed of how fast an user can create posts.

Django framework includes a logging library that can be used to fix this issue. Example of the implementation is on the linked line which is currently commented out. However, making it work properly some tinkering with settings.py is required. The logging system can be configured to mail errors to the site admins, which may be caused by an attacker trying to find weak spots. To utilize the logs further, an IP that fails singing in too many times should be blocked or at least be displayed a detection captcha. This is not the greatest solution since it is rather simple to bypass using a VPN or a proxy.

FLAW 6:

https://github.com/jpasikainen/cybersecproject/blob/master/db.sqlite3

A2:2017-Broken Authentication. To do administrative duties, an admin account is present at the database. Unfortunately it uses a very common username/password combo, admin/admin. This allows a possible attacker to access the admin tools and cause damage.

This problem can be fixed by removing the database or by changing the admin password. In addition, it would be more secure to add multi-factor authentication. Now even with leaked credentials it is very difficult for an attacker to get in.
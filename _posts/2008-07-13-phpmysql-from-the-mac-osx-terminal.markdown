---
date: '2008-07-13 06:24:00'
layout: post
slug: phpmysql-from-the-mac-osx-terminal
status: publish
title: PHP+MySQL from the Mac OSX Terminal
wordpress_id: '42082031'
categories:
- Articles
tags:
- apache
- Articles
- BSD
- Development
- mac
- mysql
- OSX
- php
- Sockets
- xampp
---

I had to write a CLI PHP script today as part of the job-parser for the SMS module in ChirpSchool. The parser executes every 5 minutes as a cron-job and dispatches waiting messages in the Message Queue.




I ran into a small problem in that the Command-Line-Interface PHP binary was different to the one running on my Apache+Mysql+PHP stack so the CLI PHP didn't know which MySQL socket to attach to:




> 

> 
> Warning: mysqli_connect(): (HY000/2002): Can't connect to local MySQL server through socket '/var/mysql/mysql.sock'
> 
> 





The solution is simple. I am using Mac OSX 10.5.4 Leopard and XAMPP.






  1. Find out which PHP you are using from the terminal by typing 'whereis php'. It is no doubt /usr/bin/php.   




  2. Create a php.ini in /etc. Type 'sudo cp /etc/php.ini.default /etc/php.ini


  3. Then open this new file in something… I did a 'sudo nano /etc/php.ini'.


  4. Edit the mysqli.default_socket parameter (or mysql if you aren't using the new improved driver) to point to the MySQL socket Apache is using. Mine was at /Applications/xampp/xamppfiles/var/mysql/mysql.sock (your's may be at  /tmp/mysql.sock)


  5. Be sure to save this new php.ini. Remember, /etc is protected so you won't be able to save the file unless you have sudo'd yourself admin rights.  




  6. Commenter** ferzkopp** kindly reminds us that an Apache restart may be neccesary to get this activated. Thanks for the Tip! 




Hope this helps!

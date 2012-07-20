---
date: '2008-08-28 15:56:00'
layout: post
slug: setting-up-lamp-within-a-small-network
status: publish
title: Setting up LAMP within a small network
wordpress_id: '47789789'
tags:
- '3306'
- apache
- c#
- dotnet
- dyndns
- lamp
- linux
- mac
- mysql
- php
- port forwarding
- Technology
- wamp
- xampp
---

My friend [Alain K](http://twitter.com/alainkermis) is deploying the first version of his soon-to-be-released desktop application, _WealthWorks_. It is designed for Personal Financial Advisors and Investors that need to track client information, risk profiles, investments and returns. He has a MySQL backend with which the C# client application connects.

Due to the latency on South African DSL connections and the fact that the application is quite chatty, he is installing database servers within company intranets. This tutorial goes through the basics of making this work on a network where there are no static public IP Addresses available.

**Decisions**

Start with a piece of paper. Draw the network including any cables, routers, computers or switches that you think are important. This will give you a broad understanding of where your server fits into the picture.

The computers on the network will access the server you are setting up via its  [IP Address](http://en.wikipedia.org/wiki/IP_address). Ask the network administrator for an open address which you can use.

Configure the computer to use this address as a Static IP.

Tutorial: Setting up a Static IP on Windows ([Read](http://portforward.com/networking/static-xp.htm))
Tutorial: Setting a Static IP on OSX ([Read](http://www.answers.vt.edu/ask4help/connection/vtkb1867.htm))

**MySQL Installation**

Start by installing MySQL. If all you want is the database server then head over to the [download page](http://dev.mysql.com/downloads/mysql/5.0.html#downloads) on MySQL.com and grab it. If you need a full Apache+MySQL+PHP stack then take a look at [WampServer](http://www.wampserver.com/en/) (Windows only) or [XAMPP](http://www.apachefriends.org/en/xampp.html) (MacOSX, Windows, Linux, or Solaris). Both packages include very cool GUIs for installing and controlling the server.

**MySQL Management**

You’ll no doubt want to change the root user password and upload your database scheme to your newly installed server. I personally use Navicat - a great GUI for MySQL which comes in both a [paid and free version](http://mysql.navicat.com/download.html). Give it the IP address you chose earlier, and the username and password of ‘root’ and blank (nothing, empty string, etc) respectively. In no time at all you’ll be browsing your database.

At this stage, all the other computers on the local network should be able to reach MySQL on the IP address you specified (remember, it serves connections on Port 3306).

**Accessing it from the outside
**

The next step is to make your database accessible from outside of the local network. If you’re a consultant working from home or a different office, you’ll undoubtedly want this sort of access. Similarly, you may want clients to be able to connect in via the internet.

You need to tell your router to accept all incoming mysql traffic and push it to that server. We call this Port Forwarding. We are going to forward all traffic (on mysql port 3306) to our mysql server on our local network (also port 3306).

Follow the instructions on [PortForward.com](http://www.portforward.com/english/applications/port_forwarding/SSH/SSHindex.htm) to configure your router.You want to forward all incoming traffic on port 3306 to 10.x.x.x (or 192.x.x.x) on port 3306.

Likewise, if you’ve got an Apache, MySQL, PHP setup on the server, you’ll want to access the website/webapplication by going to a URL from a web browser. The trick is to sign-up for a free DynamicDNS account at [](http://www.dyndns.com)[www.dyndns.com](http://www.dyndns.com) and add that to your router’s configuration.

I trust this helps! Suggestions and thoughts, please :)

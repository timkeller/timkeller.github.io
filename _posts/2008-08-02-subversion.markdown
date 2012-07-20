---
date: '2008-08-02 07:51:00'
layout: post
slug: subversion
status: publish
title: Subversion
wordpress_id: '44445133'
categories:
- Articles
tags:
- Articles
---

A geeky post coming up I'm afraid.




As you may know - I'm a huge fan of the Subversion (SVN) version control system. For the uninitiated: It lets us synchronise our local "working copies" with a central server. If someone messes something up, we can roll back to a previous version of a particular file. It also lets us experiment with the code in a differen branch before merging the result into the trunk.




Anyone doing web development *should* be using version control if they are serious about their product.




The server runs on almost any platforms, and as do the plethora of third-party GUI clients. On the Windows side I would highly suggest [TortoiseSVN](http://tortoisesvn.tigris.org/), one the Linux side you'll either be using the Command Line or one of the generic, [cross-platform](http://www.cuil.com/search?q=linux+svn+client), clients. And now, let me introduce the reason I love Subversion so much. On the Mac - [Versions.app](http://www.versionsapp.com/)! It has to be [the](http://www.versionsapp.com/media/img/ui_browse.jpg) [most](http://www.versionsapp.com/media/img/ui_welcome.jpg) [amazing](http://www.versionsapp.com/media/img/ui_timeline.jpg) svn client ever!




![](http://www.versionsapp.com/media/img/ui_browse.jpg)




One problem that can occur is Server-Local inconsistencies. Sometimes, someone does something stupid and renames a folder without following the proper proceedure and things break horribly. When all else fails I suggest you look to the following one-liner to solve all your problems on linux/bsd/macosx.`   
`




Change to the directory in question. Then simply execute:




> ` rm -rf `find . -type d -name .svn``




'til next time!




Tim

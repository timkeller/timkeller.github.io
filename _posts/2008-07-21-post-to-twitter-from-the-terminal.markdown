---
date: '2008-07-21 17:32:19'
layout: post
slug: post-to-twitter-from-the-terminal
status: publish
title: Post to Twitter from the Terminal
wordpress_id: '43050243'
categories:
- Articles
tags:
- Articles
---

If you're using a [good](http://www.ubuntu.com) or [awesome](http://www.apple.com/macosx/) operating system (and actually anything other than [windows](http://www.microsoft.com/windows)), you can post to Twitter using their API. Just use the great and powerful [curl](http://curl.haxx.se/).




Open up your Terminal or Command Line (whatever you want to call it) and type:




> 

> 
> curl -u _email_:_password_ -d status="_your message here_" [http://twitter.com/statuses/update.xml](http://twitter.com/statuses/update.xml)
> 
> 





You must insert your Email and Password in the instruction, obviously.




Read more about this: [here](http://groups.google.com/group/twitter-development-talk/web/api-documentation#StatusMethods)!

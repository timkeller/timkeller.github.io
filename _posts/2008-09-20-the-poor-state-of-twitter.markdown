---
date: '2008-09-20 10:03:00'
layout: post
slug: the-poor-state-of-twitter
status: publish
title: The (poor) state of Twitter
wordpress_id: '50985386'
categories:
- Articles
tags:
- Articles
---

![](http://alt1040.com/wp-content/uploads/2008/07/twitter-whale.png)




This morning (or evening, depending on where you are) Twitter launched its brand new UI. I was one of the few people who got to have a look at this [new UI](http://twitter.com/timkeller/statuses/861328601) back in July few literally a few minutes and its rather nice.




The UI improvements are notable, but altogether uninspirational when you consider how much else went wrong with Twitter's backend infrastructure. So, I present a letter to Twitter.




Dear Twitter.




Thanks for the new UI. Why didn't you bother including your recently purchased Summize Search Engine? I'm getting tired of going to a different URl when I search you. And why did your new UI bring such massive backend problems?




Let's have a quick look at your status page at Status.Twitter.com:




> 

> 
> During tonight’s update users may have encountered a strange bug where their background image dissapeared.
> 
> 





Right, this was not just a '_strange bug_'. Let's be honest, when we webapp designers do something stupid we call it a 'strange bug'. You simply didn't test what would happen if you installed the new UI over people's profiles that had existing custom backgrounds on a particular asset (Amazon s3) sever. Fail for not thinking.




> 

> 
> This has been fixed. If you are still experiencing the problem send an update to @twitter with the words “no background image” in the tweet and we’ll fix it for you.
> 
> 





This report further goes to prove that you were to blame. Okay, shame, we can survive messed up backgrounds.




Then later you said.




> 

> 
> The site has been slow and many users have been getting errors. We are working through the issues now and will be deploying fixes as quickly as we can.
> 
> 





Well, we're so glad to know you're "working through the issues" guys, but may I venture a guess that you actually don't have a cooking clue what is wrong?




> 

> 
> **Update** (4p): We’re still working through these issues. As we deploy _**potential fixes**_ (_emphasis mine - TK_) for the underlying problems, some additional instability may be introduced. A number of whale pages are being thrown right now. We are working on it.
> 
> 





Thanks for the news that after a full day you're still "working through these issues". Good job. So, you actually don't know what you're doing and instead are just trying random things.




You clearly don't have a staging server where you test builds before taking them live else these wouldn't be "potential fixes" but rather "actual tested fixes". And while we're on it - stop with the Whale Pages, they're lame and uninformative. Again, stop telling us you're "working on it" - tell us when you've fixed it.




> 

> 
> We are currently in the process of re-balancing our timeline cache. You may see missing Tweets in your timeline. This should be entirely cleared up by tomorrow afternoon.
> 
> 





You're re-balancing your timeline cache? What the hell does that mean? Using big words impresses no one dudes. Just say, we're having to reindex our whole database because our architecture and infrastructure sucks.




Enough is enough. You've had plenty of time over the last 4 months to rewrite the whole app. While you've been piddling around with your little _Ruby on <strike>Rails</strike> Fails_ app, [Laconica](http://laconi.ca/trac/) has implemented an opensource, distributed, PHP5 version of your product which is stable works extremely well.




Get it right, or go home, because we're getting tired of the flakeyness.

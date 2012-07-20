---
date: '2009-06-21 17:54:47'
layout: post
slug: rss-exporting-from-mail-app-to-google-reader
status: publish
title: 'RSS: Exporting from Mail.app to Google Reader'
wordpress_id: '62038122'
categories:
- Articles
tags:
- apple
- google
- google reader
- mail
- rss
- Technology
---

Despite the fact that some believe that [RSS is dead](http://www.techcrunchit.com/2009/05/05/rest-in-peace-rss/) (well, [some](http://www.scripting.com/stories/2009/05/06/rssIsDeadMyAss.html) don't), I still use it frequently to catch up on the day's news at a glance.

Historically, I've kept my feeds in Apple's Mail.app. However, I've recently found myself wanting to catch up on RSS when I'm in the car or at the gym. I needed a way to move from Mail to Google Reader.

The trouble is, Apple doesn't have a way for you to export your RSS links our of Mail (as text or [OPML](http://en.wikipedia.org/wiki/OPML)). Thus, I turned to the Google, and found a fairly simple solution:



	
  1. Export the RSS feeds as URL links in plain text (Mac OSX Leopard-only). This bash link places the export on your desktop.
`
IFS=$'\n';
for i in $(find ~/Library/Mail/RSS/ -name "Info.plist");
    do grep "http://" $i | sed "s/.*\(http[^<]*\).*/\1/" >> ~/Desktop/Mail\ Feeds.txt;done
`


	
  2. Convert to from Plain Text to OPML. I used the excellent converter at [http://unold.dk/code/opmlgen/](http://unold.dk/code/opmlgen/) (Dead-link, update thanks to commenter Tom: [http://reader.feedshow.com/goodies/opml/OPMLBuilder-create-opml-from-rss-list.php](http://reader.feedshow.com/goodies/opml/OPMLBuilder-create-opml-from-rss-list.php))

	
  3. Import into GoogleReader!


Simple. I know have all my feeds in GoogleReader, and can access them whereever I am.

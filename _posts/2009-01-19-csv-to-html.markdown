---
date: '2009-01-19 20:06:19'
layout: post
slug: csv-to-html
status: publish
title: CSV to HTML
wordpress_id: '62038105'
categories:
- Articles
tags:
- cli
- csv
- html
- php
- Programming
- script
---

I produce websites for a lot of school's in and around Cape Town. It's something I started doing when I was in High School, and it's kinda stuck.

Last night I received a Word document with pages of teacher's names and email addresses for a website. As I looked at it I imagined the huge amount of time I was about to waste either in a WYSIWYG editor or copying and pasting HTML tags.

Then I remembered that I had a B.Sc and more than 2 brain cells. I moved the Word Table to iWork Numbers (Excel would have worked just as well), exported the file as a CSV document, pulled open Textedit and wrote a quick PHP-CLI script to suck in the CSV and output the relevant HTML.

Hope it's useful to someone else out there!
    
    #!/usr/bin/php
    $job</b>: <a href="mailto:$email">".htmlspecialchars($name)."</a><br></br>n";
    }
    ?>

  


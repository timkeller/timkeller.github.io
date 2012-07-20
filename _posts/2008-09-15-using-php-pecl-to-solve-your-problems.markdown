---
date: '2008-09-15 18:12:00'
layout: post
slug: using-php-pecl-to-solve-your-problems
status: publish
title: Using PHP PECL to solve your problems
wordpress_id: '50304142'
categories:
- Articles
tags:
- Articles
---

So, okay, perhaps that's too general a post title - let me explain.




Over the weekend we got ready to push out a major update to [ChirpSchool](http://chirpschool.com) and ChirpBusiness. Amongst the new features (like our new DB layer, Social Chirp, Infobase upgrades, and a pretty major application server restructuring) was the new module called Intouch which delivers SMS's to staff and parents.




Chirp uses [JSON](http://json.org) to transport information between the backend and UI of the SMS system. Problem is [PHP-JSON](http://php.net/json) ships with PHP 5.2.0+, and we still have [Ubuntu](http://ubuntu.com) Server 6.06LTS on a few servers which only has PHP 5.1.x available.




We could have upgraded 6.06 to 8.04 (also an LTS release) but that brings its own set of challenges, risks, and annoyances. Equally, we could have compiled PHP 5.2.x from source and replaced the running 5.1.x with it. This was tempting but since 5.1 was an Apt-Get install we were hesitant to remove it when this server was very much a live production box.




Our final idea and eventual solution was to add the JSON library as a PECL Extention to our existing PHP 5.1. Here's (simply) how we did it:






  1. 
**Make sure your Ubuntu Server has the neccesary packages:**  
  
`apt-get install php-pear php5-devel  
  
`



  2. 
**You may need to update PEAR so that it grabs PECL:**  
  
`pear update  
  
`



  3. 
**Use the PECL installer:**  
  
`pecl install json  
  
`



  4. 
**Add the extension to php.ini**  
  
add extension=json.so to /etc/php/apache2.ini and /etc/php/cli.ini or wherever you have your PHP configuration files stored.  




  5. **Restart or Reload Apache HTTPd to see changes take effect**




Finding this solution saved us potential headaches, data loss and related undesirable things. I'd highly recommend you take a look at [[http://pecl.php.net](http://pecl.php.net)](http://pecl.php.net) and see if the extesion you require is available before upgrading your PHP version or even distro!

---
date: '2010-02-01 17:05:52'
layout: post
slug: comparing-two-mysql-tables
status: publish
title: Comparing two MySQL tables
wordpress_id: '62038231'
tags:
- Geek
- mysql
- Opensource
- sql
- Technology
---

![](http://timk.co.za/wp-content/uploads/2010/02/mysql_logo.gif)From time to time, I need to compare MySQL database tables and see what data has been added to the one in the time since I mysqldump'd the first one.

For example: Let's say I have table_a as my snapshot'd table, and table_b as my newer table which has one or more new rows in it.The query below will return all records that are in table_b, and not in table_a.


    
    <code>SELECT table_b.* FROM table_b
    LEFT JOIN table_a ON table_b.id = table_a.id
    WHERE table_a.item_id IS NULL</code>



This idea can be extrapolated to comparing the tables of two different databases:


    
    <code>SELECT database_b.sometable.* FROM database_b.sometable
    LEFT JOIN database_a.sometable ON database_b.sometable.id = database_a.sometable.id
    WHERE database_a.sometable.item_id IS NULL</code>



The you can take those results and use them to INSERT the missing records, should you want to do this.

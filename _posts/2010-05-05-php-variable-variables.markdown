---
date: '2010-05-05 18:57:27'
layout: post
slug: php-variable-variables
status: publish
title: PHP Variable variables
wordpress_id: '62038311'
categories:
- Articles
tags:
- Articles
---

A seldom used, but incredibly useful, aspect of PHP is the ability to reference variables by name, based on the contents of a variable. Don't worry if that sentence didn't make sense to you. Let's see an example:

    
    <code>$a = "hello";       // $a is "hello"
    $$a = "world";    // Now $hello = "world"
    echo "$a ${$a}"   // outputs "hello world"
    echo "$a $hello" // also ouptuts "hello world"
    </code>


This is useful in the situation that you need to access an object class variable at runtime. Let's say we have three class variables:

    
    <code>$this->cycle_1_mark
    $this->cycle_2_mark
    $this->cycle_3_mark
    </code>


At runtime, we have a variable $semester which holds the current semester. To it access it, we do something like:

    
    <code>$myObject = new Object();
    echo $myObject->{"cycle_$semester_mark"};  // outputs the value for the substituted class variable
    </code>


More on [PHP.net:Variable Variables](http://php.net/manual/en/language.variables.variable.php).

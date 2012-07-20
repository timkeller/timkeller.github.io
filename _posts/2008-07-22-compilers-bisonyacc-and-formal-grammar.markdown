---
date: '2008-07-22 10:06:31'
layout: post
slug: compilers-bisonyacc-and-formal-grammar
status: publish
title: 'Compilers: Bison/Yacc and Formal Grammar'
wordpress_id: '43128718'
categories:
- Articles
tags:
- Articles
---

We had our first lecture on Compiler Techniques and Theory today in [Computer Science](http://www.cs.uct.ac.za). I think it left some of the class a bit lost, or at least dazed. Here is a bit more information I uncovered this afternoon. Bare in mind this post will probably seem completely stupid in a few days time once we've learnt more about Compilers…




In formal semantics, computer science and linguistics, a **formal grammar** is a precise description of a formal language – that is, of a set of strings over some alphabet.




In other words, a grammar describes which of the possible sequences of symbols (strings) in a language constitute **valid** words or statements in that language, but it does not describe their semantics (i.e. what they mean).




So… say we've devised out own new language which programs are to be written in. We want to compile this, or at least lexically analyze it for correctness. We can use a tool such as [GNU Bison](http://en.wikipedia.org/wiki/GNU_bison) to convert the formal grammar definiton to a C or C++ program. The definition is provided in [BNF](http://en.wikipedia.org/wiki/Backus-Naur_form) format. Consider the cool BNF examples for a US Postal Address on wikipedia.




Along with Bison, you might want to use [Flex](http://en.wikipedia.org/wiki/Flex_lexical_analyser), a lexical analyser which helps identify patterns and elements of a grammar in text.




My Mac had Bison pre-installed, obviously, and if you're using a [good](http://www.ubuntu.com) [Linux](http://www.debian.org) [distro](http://www.fedoraproject.org) you should find this holds true. If you're using Windows, you will need to get [this](http://gnuwin32.sourceforge.net/packages/bison.htm).

---
date: '2006-06-27 11:22:34'
layout: post
slug: umoya-management-console
status: publish
title: Umoya Management Console
wordpress_id: '34'
tags:
- Randomness
---

Phew, I've been working on this management application for the past few days and its finally coming together. Umoya provides a WAN infrastructure across the Western Cape (extending to the whole country in time I'm sure) for various customers including the Disaster Management Services, the Department of Roads and soon another major client which I can't yet discuss publically.

We have equipment spread out at about 50 sites around the province and we need to monitor exactly what's going on at each node on the WAN and know what equipment should be at that node. We have software such as OpManager, Service Desk, and Periscope... but none of them are customised to our needs.

So i'm been tasked to code this application to provide the company with a customised tool. Its coded in PHP5 with a MySQL5 backend and is run on a server on our WAN. The idea is that when out engineers are on site, they can connect to the server and enter all the information about the node (serial numbers, etc) into the database through a web interface. From our HQ we can then run diagnostics on that node and ensure that it is fully functioning.

Its been a great learning experience and I look forward to presenting the final version to the company.

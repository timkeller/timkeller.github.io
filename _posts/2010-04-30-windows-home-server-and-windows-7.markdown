---
date: '2010-04-30 13:49:02'
layout: post
slug: windows-home-server-and-windows-7
status: publish
title: Windows Home Server and Windows 7
wordpress_id: '62038307'
tags:
- microsoft
- Technology
- whs
- windows
- windows home server
---

![](http://timk.co.za/wp-content/uploads/2010/04/windows-home-server-logo.jpg)I like Windows Home Server a lot. It offers most of the features we need at home: central file hosting, backup to the cloud (using an addon), media streaming, and backup.

However, this morning I experienced an issue while trying to join a Windows 7 Professional computer to the Home Server.

During the installation of the Connector software (found at http://yourserver:55000) you are asked to enter the server administrator's password. Strangely I was repeatedly told: “The password is incorrect.  Please retype your password.  Letters in passwords must be typed using the correct case.”

The solution took a while to find, but I eventually I came across a [post](http://social.microsoft.com/Forums/en-US/whssoftware/thread/df3182a5-e134-4b38-a5a4-e94f1cf71314/) by [AMLane](http://social.microsoft.com/Profile/en-US/?user=AMlane&referrer=http%3a%2f%2fsocial.microsoft.com%2fForums%2fen-US%2fwhssoftware%2fthread%2fdf3182a5-e134-4b38-a5a4-e94f1cf71314%2f&rh=gi7InVGPn%2flltG4xjdVb125TDS5YtDgtwIh0%2bNMG7R8%3d&sp=forums) on the Microsoft forums that solved my problem.



	
  1. Run _secpol.msc_ (You'll need Windows 7 Professional, Enterprise or Ultimate)

	
  2. Drill down through _Local Policies_ | _Security Options_

	
  3. Find _Network Security: LAN Manager authentication level_

	
  4. Set this to _Send NTLM response only_

	
  5. __Reboot the machine


I imagine that similar strange bugs in WHS will be dealt with in the [upcoming](http://www.engadget.com/2010/04/26/windows-home-server-vail-beta-now-available-for-download-brin/) Home Server 2.0 codenamed - "Vail", now [available](http://windowsteamblog.com/blogs/windowshomeserver/archive/2010/04/26/wanna-peek-at-the-next-version-of-windows-home-server-check-out-the-new-public-beta-for-windows-home-server-code-name-vail.aspx) for beta testing.

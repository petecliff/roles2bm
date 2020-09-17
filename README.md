# AWS Roles to Netscape Bookmark format
A simple script to convert AWS roles in the format used by the very useful AWS Extend Switch Roles browser extension to Netscape bookmark format for import into Firefox.

This came about as changes to the AWS UI mean the extension stops working. While this is resolved it may be useful to use bookmarks instead.

Requires python 3 and not a lot else.

WARNING - the output file is overwritten without any checking!

## Usage
> python3 ./roles2bm.py -i INPUT -o OUTPUT

Then open Firefox, go to Bookmarks -> Show All Bookmarks
Click the up/down arrow dropdown -> Import bookmarks from HTML...

The bookmarks go into a folder called `AWS Role Switcher import` on the bookmark menu and from there can be moved about as required.
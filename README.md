=======
vid2mp3
=======

Commandline tool to download youtube flash videos as mp3.

It communicates with listentoyoutube.com for this purpose.

Vimeo.com, dailymotion.com, metacafe.com are also supported by this tool.

Installation
------------

Now it is an early release so if you want to install it in your system it requires su/superuser access.

To install the script do this

Option 1 : Install via pip ::

    $ sudo pip install vid2mp3

Option 2 : If you have downloaded the source ::

    $ sudo python setup.py install


How-to Use
----------

Use it as ::

    $ vid2mp3 [video-link]

Releases
========

v0.1
----
* First stable release.
* Supports youtube.com.
* Supports vimeo.com.
* Supports dailymotion.com.
* Downloads the audio file(.mp3) into present working directory.

v0.1.1
------
* More user friendly and verbose.
* Fixed wrong url exception.

v0.1.2
------
* Added dependency link for dependency lxml

v0.1.3
------
* Fixed bug: UnicodeError handled when there's a unicode problem.


Reporting Bugs
--------------

Please report bugs at github issue tracker: https://github.com/iamsudip/vid2mp3/issues

Author
------
iamsudip <iamsudip@programmer.net>

* http://github.com/iamsudip


# Table of Contents

1.  [Description](#org0a55360)
2.  [How it works](#orge021f17)
3.  [How to use](#org5a7106c)
    1.  [Some examples](#orgbb080c4)
4.  [Notes](#org14d21a2)
5.  [License](#orge37ffe5)



<a id="org0a55360"></a>

# Description

**xdcc** is a simple, one file, **[XDCC](https://en.wikipedia.org/wiki/XDCC)** downloader written in python, so it should works out of the box on every system that
has python3 installed.


<a id="orge021f17"></a>

# How it works

This program uses a small IRC client library, <https://github.com/jaraco/irc>, to connect to the specified server, join the
chosen channel(if some channel are specified on command-line) and sends a **ctcp** message to the XDCC bot soliciting 
the desired file. If the last part goes well then we start to receive the file via **DCC**.


<a id="org5a7106c"></a>

# How to use

    xdcc -s <server-name> -p <port-number> -c <channel>  botname [action] [packs]

If **server** and **port number** options are not specified, the default server and port are irc.rizon.net
and 6670, respectively. If no channel is specified then the program don't join any channel at all.


<a id="orgbb080c4"></a>

## Some examples

Print the bot's file list to stdout:

    xdcc --stdout 'YOUR-BOT-NAME-HERE' list

Download the files given by the pack numbers 500,501,502,503 and 510:

    xdcc 'YOUR-BOT-NAME-HERE' send '500-503,510'

Same as above, but supposing that the bot requires you to be logged in a specific channel:

    xdcc -c '#ChannelNameHere' 'YOUR-BOT-NAME-HERE' send '500-503,510'

For more options just type `xdcc --help` in your shell:

    usage: xdcc [-h] [--server SERVER] [--channel CHANNEL] [--port PORT] [--stdout] [--nickname NICKNAME] [--verbose]
    	    bot {list,send} [packs]
    
    positional arguments:
      bot                   The XDCC Bot name.
      {list,send}           Action to take. Use 'list' for get the file list from the bot. Use 'send' to get a file from the bot.
      packs                 Packs numbers of the desired files. Ex: '50-62,64,66,70-80'.
    
    optional arguments:
      -h, --help            show this help message and exit
      --server SERVER, -s SERVER
    			The server to connect. The default is irc.rizon.net.
      --channel CHANNEL, -c CHANNEL
    			The channel to join. The default is to not join in any server.
      --port PORT, -p PORT  The port number of the server. The default is 6670.
      --stdout, -t          When used with the 'list' action, print the contents of the list file to the stdout.
      --nickname NICKNAME, -n NICKNAME
    			Nickname to be used in the server. If this option is not provided, a random permutation of 'anonymous' will
    			be used.
      --verbose, -v         Enable verbose mode.


<a id="org14d21a2"></a>

# Notes

-   Currently connections using **SSL/TLS** are not supported, so the secure ports will not work.
-   This software assume that the bot is using turbo DCC by default. This was the case with the bots that

i have used for testing. If you come across some bot that handles DCC differently, let me know by open a issue
or a pull request. 


<a id="orge37ffe5"></a>

# License

    MIT License
    
    Copyright (c) 2020 Thiago Teodoro Pereira Silva
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.


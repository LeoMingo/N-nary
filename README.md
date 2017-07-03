# N-nary
A toy script to convert a type of number to another type of number, for instance: binary to hexidecimal


But you can do a lot more than that with this small script, here is a simple demonstration:

<img src = "https://github.com/LeoMingo/N-nary/blob/master/demo.png">

Notice, the last line is not an error, it was simply due to the fact that I contained multiple same characters in the map for 17-nary base map, and this case should be avoided, as you can see from hex_map, each character is unique in the list.

Maybe I will start extending the script into a further developed miniproject(like adding float system, defining numeric calculations etc.), though for now, this script can still be used as a simple and fun utility as it can not only produce standard types like binary and hexidecimal etc., you can define your own number types with or without base_map to decorate your number as well, as long as it's integer though.

It can also be extended as a simple back engine for generating passwords with base_map, but remember as shown in the last line of picture and as being explained above, you should avoid using the same characters in one base_map to avoid index conflicts.

# review of regex Symbols

This chapter covered a lot of notation, so here’s a quick review of what 
you learned:
 •	The ? matches zero or one of the preceding group.
 •	The * matches zero or more of the preceding group.
 •	The + matches one or more of the preceding group.
 •	The {n} matches exactly n of the preceding group.
 •	The {n,} matches n or more of the preceding group.
 •	The {,m} matches 0 to m of the preceding group.
 •	The {n,m} matches at least n and at most m of the preceding group.
 •	{n,m}? or *? or +? performs a nongreedy match of the preceding group.
 •	^spam means the string must begin with spam.
 •	spam$ means the string must end with spam.
 •	The . matches any character, except newline characters.
 •	\d, \w, and \s match a digit, word, or space character, respectively.
 •	\D, \W, and \S match anything except a digit, word, or space character, 
respectively.
 •	[abc] matches any character between the brackets (such as a, b, or c).
 •	[^abc] matches any character that isn’t between the brackets.
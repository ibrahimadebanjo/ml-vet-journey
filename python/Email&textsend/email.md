## Selecting a Folder
 pprint.pprint(imapObj.list_folders())
 [(('\\HasNoChildren',), '/', 'Drafts'),
 (('\\HasNoChildren',), '/', 'Filler'),
 (('\\HasNoChildren',), '/', 'INBOX'),
 (('\\HasNoChildren',), '/', 'Sent'),--snip-
 (('\\HasNoChildren', '\\Flagged'), '/', '[Gmail]/Starred'),
 (('\\HasNoChildren', '\\Trash'), '/', '[Gmail]/Trash')]

## Performing serach
ALL'
 'BEFORE date',  
'ON date',  
'SINCE date'
 'SUBJECT string',  
'BODY string',  
'TEXT string'
 'FROM string',  
'TO string',  
'CC string',  
'BCC string'
 'SEEN',  
'UNSEEN'
 'ANSWERED',  
'UNANSWERED'
 'DELETED',  
'UNDELETED'
 'DRAFT',  
'UNDRAFT'
 'FLAGGED',  
'UNFLAGGED'
 'LARGER N',  
'SMALLER N'
 'NOT search-key'
 'OR search-key1 
search-key2'

## Changing the default storage from 10000(default) to 10,000,000 bytes
imaplib._MAXLINE = 10000000
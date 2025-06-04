# This method is used in removing whitespaces
spam = "              Hello World              "
print(spam.strip())
print(spam.rstrip())
print(spam.lstrip())
spam = "SpamSpamBaconSpamEggsSpamSpam"
print(spam.strip("ampS"))
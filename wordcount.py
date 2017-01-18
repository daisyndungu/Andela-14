def words(string):

 mylist = string.split()

 mydict = {}

  for word in mylist:
    
    if word.isdigit():
      word = int(word)
    #count each word occurence in the string
    if word in mydict:
      mydict[word] +=  1
    else:
      mydict[word] = 1
  return mydict

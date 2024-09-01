class MyCounter:
    import os.path
    import sys
    counts = dict()
    bigcount = None
    bigword = None
    wordtotal = 0

    @classmethod
    def most_common_word_count(cls):
        name = input("Input a file name: ")
        name = cls.os.path.normpath(name)
        handle = open(name)
        for line in handle:
            words = line.split()
            for word in words:
                cls.counts[word] = cls.counts.get(word, 0) + 1

        for word,count in cls.counts.items():
            if cls.bigcount is None or count > cls.bigcount:
                cls.bigword = word 
                cls.bigcount = count
        handle.close()
               
        print("Most common word is: {}".format(cls.bigword))
        print("It appears: {} times".format(cls.bigcount))

    @classmethod
    def word_count(cls):
       name = input("Total Word Count\n Input file name:")
       fhandle = open(name)
       for word in fhandle:
            cls.wordtotal += 1
        
       print(f"Total word count in {name}: {cls.wordtotal}") 


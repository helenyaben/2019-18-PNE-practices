class Seq:
    #A class for representing sequences
    def __init__(self, strbases):
        print('New sequence created!')

        self.strbases = strbases

    def len(self):
        return len(self.strbases)


s1 = Seq("ACCTTG")
s2 = Seq("AAAACCTT")

l1 = s1.len()
l2 = s2.len()

str1 = s1.strbases
str2 = s2.strbases

print("Sequence 1: {}".format(str1))
print("Sequence 2: {}".format(str2))
print("Length 1: {}".format(l1))
print("Length 2: {}".format(l2))
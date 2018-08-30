# s = "{0}{1} hi"
# print(s)
# s.format('a', 'b')
# print(s)
#
# s = s.format('a', 'b')
# print(s)
#
# s2 = "%s %s hi"
# print(s2)
# s2 % ('asdf', "sdfgdfghdfguh")
# print(s2)
#
# s2 = s2 % ('asdf', "sdfgdfghdfguh")
# print(s2)

class S1:
    def ss(self, items):
        for item in items:
            str_tup = item.__str__()
            str_result = r"hi hello hi %s" % str_tup
            print(str_result, type(str_result))
    def __init__(self):
        pass

s11 = S1()
items = [("hi", "hello", "aa"), ("hi", "hello", "bb"), ("hi", "hello", "cc")]
s11.ss(items)


base = "asdfasdf %s"
str = ("hi", "hello", "aa")
result = base % str[1]

print(str[0])

aa = str(("hi", "hello", "aa"))
print(aa, type(aa))

'(\\'
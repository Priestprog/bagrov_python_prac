s = "hello world a"
s1 = "hello sdf sdf sdf sdf yes dsf sdf sdf sdf "
s2 = "world"
s3 = "a dg dfg dfg dfg dfg world"
match s3:
    case string if string.split()[0] == "hello" and "yes" in string.split():
        print(string)
    case string if string.split() == [s.split()[1]]:
        print(string)
    case string if string.split()[0] == s.split()[2] and string.split()[-1] == s.split()[1]:
        print(string)
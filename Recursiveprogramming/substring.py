#Substring
# implement the function is_substring(subrtring, a_str) that answers the
#Is the string substring actually a substring in the list a_str? 
#Examples: 
#is_substring(“a”, “gagnaskipan”) -> True 
#is_substring(“gnask”, “gagnaskipan”) -> True 
#is_substring(“iganpsk”, “gagnaskipan”) -> False 
#is_substring(“gnAsk”, “gagnaskipan”) -> False 
#is_substring(“gnesk”, “gagnaskipan”) -> False 
#Use recursion 
#Hint: Try to first implement the function ​prefix(prefix, a_str) 
#Only checks whether ​prefix​ is an exact duplicate of the beginning  following

def is_substring(substring, a_str):
    if not a_str:
        return False



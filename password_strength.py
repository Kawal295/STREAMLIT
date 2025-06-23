import re

def password_strength(passwd):
    msg=""
    if re.search(" ",passwd):
        msg+="Password must not contain spaces"
        return msg
    elif len(passwd) < 8:
        msg+="Password must be at least 8 characters"
        return msg
    else:    
        return True

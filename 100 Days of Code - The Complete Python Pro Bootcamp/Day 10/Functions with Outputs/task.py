def CamelCase(text):
    """First line is docstring or documentation tstring"""
    outstr=""
    index=0
    for let in text:
        if index==0:
            outstr+=let.upper()
            index+=1
        else:
            outstr+=let.lower()
    return outstr

def format_name(f_name,l_name):
    """This name ffthe srpri"""
    return f"{CamelCase(f_name)} {CamelCase(l_name)}"

def format_name2(f_name,l_name):
    return f"{f_name.title()} {l_name.title()}"

print(format_name("MANAS","nayak"))
print(format_name2("MANAS","nayak"))

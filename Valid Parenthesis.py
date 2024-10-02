def isValid(s: str) -> bool:
    while True:
        if "()" in s:
            s = s.replace("()", "")
        elif "{}" in s:
            s = s.replace("{}", "")
        elif "[]" in s:
            s = s.replace("[]", "")
        else:
            return len(s) == 0
            
            
            
            
            
input_string = "{[()]}"
print(isValid(input_string))

#problem1- User Input Sanitizer and formatter

full_name=input("Enter your full name")
name = full_name.strip().upper()   
print(f"the full name is {name}")



#problem2- The text redactor

sentence = "the secret password is 'SkyBlue123' "
mod_sentence= sentence.replace("SkyBlue123","123456")
print(mod_sentence)
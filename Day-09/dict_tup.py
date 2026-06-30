#problem-1 : The student dictionary lookup

def final_student_score(directory, name):
   score=directory.get(name)
   if score is not None:
      return score
   else:
      return "student not found"
student_directory= {"rohan":20, "mohan":30, "sohan":50, "priya": 60}
name="rohan"
result=final_student_score(student_directory, name)
print(result)



#problem-02 The element frequency counter 

def count_occurrences(item_list):
   freq={}
   for item in item_list:
      if item in freq :
         freq[item]+=1
      else:
         freq[item]=1
   return freq  
items = ["apple","banana","apple","orange","banana","apple"]   
result=count_occurrences(items)
print(result)   

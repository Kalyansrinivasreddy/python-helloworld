list_samples =[]
f = open("student_details.csv","r")
data = f.read() # str
data = data.split("\n") #list
#print(data)

for l in data[1:]:

 #   if not l.startswith("ID"):
      k = l.split(",")
#     print(k)
      print("Id: "+k[0])
      print("Name: "+k[1])
      print("Marks: "+k[2])
      print("Grade: "+k[3])



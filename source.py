import hashlib
import csv




def hash_password_hack(input_file_name, output_file_name):
    c = {}
    for x in range(1000,10000):
       hashed = hashlib.sha256(str(x).encode())
       c[hashed.hexdigest()] = x
    

    a = []
    b = []
    f = []
    with open(input_file_name) as csv_file:
         csv_reader = csv.DictReader(csv_file)
         for row in csv_reader:
               k = 0
               for column in row:
                   f.append(column)
                   if k == 0:
                      a.append(row[column])
                      k += 1
                   elif k == 1:
                        b.append(row[column])
                        k += 1
                   else:
                        break

            
            
    d = [str(f[0]) + "," + str(c[f[1]])]
    for i in range(0,len(a)):
        d.append(str(a[i]) + "," + str(c[b[i]]))
        
    with open(output_file_name, mode='w') as csv_file2:
          csv_file2.write(f[0])
          csv_file2.write(",")
          csv_file2.write(str(c[f[1]]))
          csv_file2.write("\n")
          for i in range(0,len(a)):
             csv_file2.write(a[i])
             csv_file2.write(",")
             csv_file2.write(str(c[b[i]]))
             csv_file2.write("\n")
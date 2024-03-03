"""
먼저 아래와 같은 형태의 run_sh_bytecode.txt을 만들어야 한다.

48 31 c0                
50                      
48 b8 6f 6f 6f 6f 6f    
...
"""

file = open('run_sh_bytecode.txt', 'r')
lines = file.readlines()
file.close()

result = []

for line in lines:
    line = line.split(' ')

    for i in range(len(line)):
        line_i = line[i]

        if (line_i == ''):
            break

        if (len(line_i) > 2):
            line_i = line_i.replace('\n', '')
        
        result.append(line_i)

bytecode = ""

for i in range(len(result)):
    bytecode = bytecode + r"\x" + result[i]

print(bytecode)
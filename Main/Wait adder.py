with open("Center Script.txt") as f:
    lines=f.read()
    
input()
lines=lines.replace("\n","{wait:0.25}\n")

with open("Center Script.txt","w") as f:
    f.write(lines)
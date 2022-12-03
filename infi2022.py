# https://aoc.infi.nl/2022/?mtm_campaign=aoc2022&mtm_source=aoc
# https://aoc.infi.nl/api/aoc/input/2022/7Q5C6ACHHSFY

voorbeeld = """draai 90
loop 6
spring 2
draai -45
loop 2"""

puzzel = """draai 90
spring 56
draai -90
loop 6
draai 180
loop 3
draai -90
loop 1
draai -45
loop 3
draai 180
loop 3
draai 270
loop 3
draai -135
draai 90
spring -46
draai -90
loop 6
draai 90
loop 3
draai 45
loop 1
draai 45
loop 1
draai 45
loop 2
draai 45
loop 1
draai -180
loop 1
draai 45
loop 2
draai -135
draai 90
spring 54
draai -90
loop 6
draai -90
loop 2
draai 180
loop 4
draai -90
draai 90
spring -39
draai 90
spring 6
draai 180
loop 6
draai 90
loop 3
draai 45
loop 1
draai 45
loop 1
draai 45
loop 1
draai 45
loop 2
draai -270
draai 90
spring 31
draai 90
spring 3
draai 180
draai -90
loop 4
draai 90
loop 3
draai 90
loop 3
draai 180
loop 3
draai 90
loop 3
draai 90
loop 4
draai -90
draai 90
spring -67
draai 90
spring 6
draai 180
loop 6
draai 180
loop 3
draai -90
loop 1
draai -45
loop 3
draai 180
loop 3
draai 270
loop 3
draai -135
draai 90
spring 26
draai -90
loop 6
draai -90
loop 2
draai 180
loop 4
draai -90
draai 90
spring -21
draai 90
spring 6
draai 180
draai -90
loop 4
draai 90
loop 3
draai 90
loop 3
draai 180
loop 3
draai 90
loop 3
draai 90
loop 4
draai -90
draai 90
spring 10
draai 90
spring 6
draai 180
draai 90
loop 3
draai -45
loop 1
draai -45
loop 1
draai -45
loop 1
draai -45
loop 2
draai 45
loop 1
draai 45
loop 1
draai 45
loop 1
draai 45
loop 3
draai -90
draai 90
spring 17
draai 90
spring 6
draai 180
loop 5
draai 45
loop 1
draai 45
loop 2
draai 45
loop 1
draai 45
loop 2
draai 90
loop 3
draai 180
loop 3
draai 90
loop 3
draai 180
draai 90
spring 3
draai -90
loop 6
draai 180
loop 3
draai -90
loop 1
draai -45
loop 3
draai 180
loop 3
draai 270
loop 3
draai -135"""

opdrachten = voorbeeld
opdrachten = puzzel
richtingen = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
richtingentext = ["noorden", "noord-oosten", "oosten", "zuid-oosten", "zuiden", "zuid-westen", "westen", "noord-westen"]
x, y, r = 0, 0, 0
voetsporen = set()
for line in opdrachten.split("\n"):
    k, v = line.split(" ")
    if k == "draai":
        r = (r + int(v)//45)%8
        print(f"De Kerstman draait {v} graden naar het {richtingentext[r]}")
    elif k == "loop":
        print(f"De Kerstman loopt {v} stappen naar positie ({x},{y})")
        for z in range(abs(int(v))):
            if v[0]=="-":
                x, y = x-richtingen[r][0],  y-richtingen[r][1]
            else:
                x, y = x+richtingen[r][0],  y+richtingen[r][1]
            voetsporen.add((x,y))
    elif k == "spring":
        print(f"De Kerstman springt {v} plekken naar ({x},{y})")
        x, y = x+richtingen[r][0]*int(v),  y+richtingen[r][1]*int(v)
        voetsporen.add((x,y))

print(f"Eindpunt ({x}, {y}) betekend een afstand van {abs(x)+abs(y)}")

for y in reversed(range(7)):
    s = ""
    for x in range(75):
        s += "##" if (x,y) in voetsporen else ",'"
    print(s)
    s = ""

#CrazyA

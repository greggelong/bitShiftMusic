import random
"""
for i in range(500):
    print("@PPPPP000000@@PPP0@@@PPP````000PPPPP")

for i in range(500):
    print("PPPPPPPPPPPPPPPPPPPPPPP")

for i in range(500):
    print("AAAAAAAAAAAAAAAAAAAAAAA")

for i in range(500):
    print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
"""
#short bursts range 20 decreacing tone longer string
for i in range(5):
    for j in range(1,40):
        for k in range(20):
            print("P"*j)
#longer tones rage 100 decreacing tone longer string
for i in range(5):
    for j in range(1,40):
        for k in range(100):
            print("@"*j)   # plays a decening voice
            print("P"*30)  # plays that tone 
          #  print("0"*8)

# random tone for range 100 random tones rand string length
for i in range(20):
    t= random.randint(20,60)
    for j in range(100):
        print("P"*t)
        print("@"*30)

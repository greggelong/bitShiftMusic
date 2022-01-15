
## trying to understand how rob Miles bit shift variations works



>echo "g(i,x,t,o){return((3&x&(i*((3&i>>16?\"BY}6YB6%\":\"Qj}6jQ6%\")[t%8]+51)>>o))<<4);};main(i,n,s){for(i=0;;i++)putchar(g(i,1,n=i>>14,12)+g(i,s=i>>17,n^i>>13,10)+g(i,s/3,n+((i>>11)%3),10)+g(i,s/5,8+n-((i>>10)%3),9));}"|gcc -xc -&&./a.out|aplay


### notes to  myself

I have already run this code in in this directory. 

so the compiled code is a.out

you can play the music by typing ./a.out|aplay


there is a git hub repo where they are trying to unpack the code

https://github.com/JamesNewton/BitShift-Variations-unrolled

## making tones with strings in python

I have written some loops in python that create some text then pipe that to 

aplay

what i have found is that it is the length of the string that creates the varying sound
and the number of times that string appears in a row that changes how long the it sounds for

hey I have had some success
with the python code making some sounds

I run it in the terminal and pipe it to acode

like

$python3 tsound2.py | aplay

I have some loops that write out blocks of increasing strings that produce decreasing tones

```python
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

```

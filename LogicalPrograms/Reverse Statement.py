inp="my name is Pranav"
#out="Pranav is name my"

l1=inp.split()
l1=l1[::-1]
#l1.reverse()

out=' '.join(l1)
print(out)
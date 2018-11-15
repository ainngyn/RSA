import random 
import PrimeTest

def Random (bit):
	a = random.getrandbits(bit)
	a = a | 1 << (bit-1)
	a = a | 1 
	#print(bin(a)) 
	return a;

def getPrime(bit):
	p = Random(bit)
	d1 = d2 = d3 = 0
	while True:
		d1+= 1
		if PrimeTest.Preprocessor(p) == False:
			p+= 2
			continue
		d2+=1
		if PrimeTest.Fermat(p,20) == False:
			p+= 2
			continue
		d3+=1
		if PrimeTest.Miller_Rabin(p,20) == False:
			p+= 2
			continue
		break
	# print(d1)
	# print(d2)
	# print(d3)
	return p

def main(bits):
	p = getPrime(bits)
	q = getPrime(bits)
	fo = open("BigPrime.txt","w")
	fo.write(str(p)+'\n')
	fo.write(str(q))
	fo.close()

main(1024)



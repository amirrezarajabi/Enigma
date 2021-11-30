import random
import  pickle


alphabet = "abcdefghijklmnopqrstuvwxyz"

r1 = list(alphabet)
r2 = list(alphabet)
r3 = list(alphabet)

random.shuffle(r1)
random.shuffle(r2)
random.shuffle(r3)

r1 = "".join(r1)
r2 = "".join(r2)
r3 = "".join(r3)

state = 0

f = open("rotors_state.rj", "wb")
pickle.dump((r1, r2, r3, state), f)
f.close()

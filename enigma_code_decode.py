import pickle

alphabet = "abcdefghijklmnopqrstuvwxyz"

def reflector(c):
    return alphabet[len(alphabet)-alphabet.find(c) - 1]

def load_rotors():
    f = open("rotors_state.rj", 'rb')
    r1, r2, r3, state = pickle.load(f)
    f.close()
    return r1, r2, r3, state

def enigma_code(c, r1, r2, r3):
    s = r1[alphabet.find(c)]
    s = r2[alphabet.find(s)]
    s = r3[alphabet.find(s)]
    s = reflector(s)
    s = alphabet[r3.find(s)]
    s = alphabet[r2.find(s)]
    s = alphabet[r1.find(s)]
    return s

def rotate_rotors(r1, r2, r3, state):
    state += 1
    r1 = r1[1:] + r1[0]
    if state % 26 == 0:
        r2 = r2[1:] + r2[0]
        if state % 676 == 0:
            r3 = r3[1:] + r3[0]
    return r1, r2, r3, state

r1, r2, r3, state = load_rotors()
plain = "hihi"
cipher = ""

for c in plain:
    cipher += enigma_code(c, r1, r2, r3)
    r1, r2, r3, state = rotate_rotors(r1, r2, r3, state)
print(cipher)

f = open("rotors_state.rj", "wb")
pickle.dump((r1, r2, r3, state), f)
f.close
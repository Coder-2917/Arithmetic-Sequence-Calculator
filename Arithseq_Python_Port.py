print("\nArithmetic Sequence Calculator")
a = 
print("b = The First Term of the Sequence")
print("d = The distance between each term of the Sequence")
print("n = The Nth Term of the Sequence\n")
def arithmetic_sequence(b, d, n):
  return (d * (n - 1) + b)

b = int(input("b = "))
d = int(input("d = "))
n = int(input("n = "))

print(f"\nAn Arithmetic Sequence with a first term of {b},")
print(f"and a distance of {d},")
print(f"has the number {arithmetic_sequence(b, d, n)} on term #{n}.")

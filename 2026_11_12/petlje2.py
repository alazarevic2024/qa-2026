import time

# for x in range(5):
#     print("Hello")
#     time.sleep(1)

cilj = 20
trenutna_pozicija = 0

for x in range(cilj):
          # simulacija praznog mesta    # trenutno
    print("\r" + trenutna_pozicija * " "     + "#",         end="")
    trenutna_pozicija += 1
    time.sleep(1)
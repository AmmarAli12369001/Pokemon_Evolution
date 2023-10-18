"""
Pokémon Evolution
You have recently caught N Pokémon and you also have M Pokémon candy bars.
You can evolve any of your Pokémon by paying X candy bars.
Alternatively, you can sell any of your Pokémon for a price of Y candy bars.
You cannot sell an evolved Pokémon.
Compute the maximum number of Pokémon you can evolve.

Standard input
The first line contains 4 integers N M X Y.

Standard output
The output should contain a single integer representing the maximum number of Pokémon you can evolve.
"""

l = [int(i) for i in input().split()]
cost = l[0] * l[2]
evolved = 0
if cost > l[1]:
    evolved += (l[1] - (l[1] % l[2])) // l[2]
    l[0] -= evolved
    l[1] %= l[2]
    print(l)
    evolved = (((l[0] - (l[0] % l[3])) // l[3]) - ((l[0] - (l[0] % l[3])) // l[3]) % l[2]) // l[2]
    print(l)

else:
    print(l[0])
print(evolved)

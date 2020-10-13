T = int(input())

for i in range(T):
    NQ = input().split()
    N = int(NQ[0])
    Q = int(NQ[1])
    lockedfix = [int(j) for j in input().split()]
    for j in range(Q):
        SK = input().split()
        S = int(SK[0]) - 1
        K = int(SK[1])
        locked = [i for i in lockedfix]
        rooms = list(range(N))
        ind = 1

        strt = S
        sel_room = S+1
        while ind < K and rooms:
            print(ind, locked, strt, rooms)
            if strt > 0 and strt < len(locked):

                if locked[strt - 1] < locked[strt]:

                    sel_room = rooms[strt - 1]

                    rooms.remove(rooms[strt])
                    locked.remove(locked[strt - 1])
                    strt -= 1
                else:
                    sel_room = rooms[strt + 1]

                    rooms.remove(rooms[strt])
                    locked.remove(locked[strt])
            elif strt > 0:
                sel_room = rooms[strt - 1]

                rooms.remove(rooms[strt])
                locked.remove(locked[strt - 1])
                strt -= 1
            else:
                sel_room = rooms[strt + 1]

                rooms.remove(rooms[strt])
                locked.remove(locked[strt])

            print(ind,sel_room + 1)
            ind += 1

        print('')
    print('')









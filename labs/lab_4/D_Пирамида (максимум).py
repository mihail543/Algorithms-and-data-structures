import heapq as h

ls = []

while True:
    try:
        command = input().split()
        if not command:
            continue
            
        if command[0] == 'CLEAR':
            ls = []
        elif command[0] == 'ADD':
            h.heappush(ls, -1 * int(command[1]))
        elif command[0] == 'EXTRACT':
            if not ls:
                print('CANNOT')
            else:
                print(-1 * h.heappop(ls))
                
    except EOFError:
        break

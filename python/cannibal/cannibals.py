class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, item):
        self.array.append(item)

    def dequeue(self):
        if self.array:
            result = self.array[0]
            self.array = self.array[1:]
            return result
        return None

    def print(self):
        for item in self.array:
            print(item)

    def is_empty(self):
        if self.array:
            return False
        else:
            return True

public_states = Queue()
memo_moves = {}

def tester():
    while not public_states.is_empty():
        state = public_states.dequeue()
        if state[0]<0 or state[1]<0 or state[2]<0 or state[3]<0:
            continue
        if state[0]>state[1] and state[1]!=0:
            continue
        if state[2]>state[3] and state[3] != 0:
            continue
        if state[0]==0 and state[1]==0:
            break
        else:
            if state[4]=="LtoR":
                if (state[0]-1, state[1], state[2]+1, state[3], "RtoL") not in memo_moves:
                    memo_moves[(state[0]-1, state[1], state[2]+1, state[3], "RtoL")] = state
                    public_states.enqueue((state[0]-1, state[1], state[2]+1, state[3], "RtoL"))
                    
                if (state[0], state[1]-1, state[2], state[3]+1, "RtoL") not in memo_moves:
                    memo_moves[(state[0], state[1]-1, state[2], state[3]+1, "RtoL")] = state
                    public_states.enqueue((state[0], state[1]-1, state[2], state[3]+1, "RtoL"))
                    
                if (state[0]-2, state[1], state[2]+2, state[3], "RtoL") not in memo_moves:
                    memo_moves[(state[0]-2, state[1], state[2]+2, state[3], "RtoL")] = state
                    public_states.enqueue((state[0]-2, state[1], state[2]+2, state[3], "RtoL"))
                    
                if (state[0], state[1]-2, state[2], state[3]+2, "RtoL") not in memo_moves:
                    memo_moves[(state[0], state[1]-2, state[2], state[3]+2, "RtoL")] = state
                    public_states.enqueue((state[0], state[1]-2, state[2], state[3]+2, "RtoL"))
                    
                if (state[0]-1, state[1]-1, state[2]+1, state[3]+1, "RtoL") not in memo_moves:
                    memo_moves[(state[0]-1, state[1]-1, state[2]+1, state[3]+1, "RtoL")] = state
                    public_states.enqueue((state[0]-1, state[1]-1, state[2]+1, state[3]+1, "RtoL"))

            elif state[4] == "RtoL":
                if (state[0]+1, state[1], state[2]-1, state[3], "LtoR") not in memo_moves:
                    memo_moves[(state[0]+1, state[1], state[2]-1, state[3], "LtoR")] = state
                    public_states.enqueue((state[0]+1, state[1], state[2]-1, state[3], "LtoR"))
                    
                if (state[0], state[1]+1, state[2], state[3]-1, "LtoR") not in memo_moves:
                    memo_moves[(state[0], state[1]+1, state[2], state[3]-1, "LtoR")] = state
                    public_states.enqueue((state[0], state[1]+1, state[2], state[3]-1, "LtoR"))
                    
                if (state[0]+2, state[1], state[2]-2, state[3], "LtoR") not in memo_moves:
                    memo_moves[(state[0]+2, state[1], state[2]-2, state[3], "LtoR")] = state
                    public_states.enqueue((state[0]+2, state[1], state[2]-2, state[3], "LtoR"))
                    
                if (state[0], state[1]+2, state[2], state[3]-2, "LtoR") not in memo_moves:
                    memo_moves[(state[0], state[1]+2, state[2], state[3]-2, "LtoR")] = state
                    public_states.enqueue((state[0], state[1]+2, state[2], state[3]-2, "LtoR"))
                    
                if (state[0]+1, state[1]+1, state[2]-1, state[3]-1, "LtoR") not in memo_moves:
                    memo_moves[(state[0]+1, state[1]+1, state[2]-1, state[3]-1, "LtoR")] = state
                    public_states.enqueue((state[0]+1, state[1]+1, state[2]-1, state[3]-1, "LtoR"))

    return

def path_reconstruction(start):
    curr = start
    result = []
    while memo_moves[curr] != curr:
        prev = memo_moves[curr]
        if prev[4] == "LtoR":
            move = (curr[2]-prev[2], curr[3]-prev[3])
            result.append(move)
        else:
            move = (curr[0]-prev[0], curr[1]-prev[1])
            result.append(move)
        curr = prev
    result = result[::-1]
    return tuple(result)

def cannibal(c, m):
    curr = (c, m, 0, 0, "LtoR")
    public_states.enqueue(curr)
    memo_moves[curr] = curr
    tester()
    if (0, 0, c, m, "RtoL") in memo_moves:
        return path_reconstruction((0, 0, c, m, "RtoL"))
    else:
        return False


                





                
        

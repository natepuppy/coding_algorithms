
# Implement a parser for a simple beat notation language.

# You are given a notation string and a tempo in BPM. The notation consists 
# of space-separated beats. Each beat may be:

# X — a note played at the start of the beat.
# . — a rest.
# [a,b,...] — a subdivision of the beat into equal-length parts, where 
# each part is itself valid notation and may be nested recursively.

# Return a list of timestamps (in milliseconds) at which notes (X) occur, 
# assuming the first beat starts at 0 ms.

# EX: Input: "X . [X,X] [X,[X,X]]"
# Output: [0.0, 1000.0, 1250.0, 1500.0, 1750.0, 1875.0]

class BeatNotation:
    def __init__(self, notation, bpm):
        self.notation = notation
        self.beat_length = (60.0 / bpm) * 1000.0
        self.result = []
    
    def run(self):
        for i, token in enumerate(self.notation.split()):
            start = i * self.beat_length
            self._parse(token, start, self.beat_length)
        return self.result


    def _parse(self, token, start, length):
        if token == "X":
            self.result.append(start)
            return

        if token == ".":
            return

        children = self._split(token[1:-1])
        new_beat_length = length / len(children)

        for i, child_token in enumerate(children):
            new_start = start + i * new_beat_length
            self._parse(child_token, new_start, new_beat_length)

    def _split(self, string):
        res = []
        depth = 0
        current = ""

        for char in string:
            if char == "[":
                depth += 1
            elif char == "]":
                depth -= 1
            
            if char == "," and depth == 0:
                res.append(current)
                current = ""
            else:
                current += char
        
        res.append(current)

        return res

if __name__ == "__main__":
    notation = "X . [X,X] [X,[X,X]]"
    bpm = 120

    result = BeatNotation(notation, bpm).run()

    assert result == [0.0, 1000.0, 1250.0, 1500.0, 1750.0, 1875.0]

    print("Test Cases Passed!")


#  --- Day 10: Syntax Scoring ---
#  You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:

#  Syntax error in navigation subsystem on line: all of them
#  All of them?! The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).

#  The navigation subsystem syntax is made of several lines containing chunks. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must open and close with one of four legal pairs of matching characters:

#  If a chunk opens with (, it must close with ).
#  If a chunk opens with [, it must close with ].
#  If a chunk opens with {, it must close with }.
#  If a chunk opens with <, it must close with >.
#  So, () is a legal chunk that contains no other chunks, as is [].
#  More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

#  Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

#  A corrupted line is one where a chunk closes with the wrong character -
#  that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

#  Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]).
#  Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

#  For example, consider the following navigation subsystem:

#  [({(<(())[]>[[{[]{<()<>>
#  [(()[<>])]({[<{<<[]>>(
#  {([(<{}[<>[]}>{[]{[(<()>
#  (((({<>}<{<{<>}{[]{[]{}
#  [[<[([]))<([[{}[[()]]]
#  [{[{({}]{}}([{[{{{}}([]
#  {<[[]]>}<{[{[{[]{()[[[]
#  [<(<(<(<{}))><([]([]()
#  <{([([[(<>()){}]>(<<{{
#  <{([{{}}[<[[[<>{}]]]>[]]
#  Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:

#  {([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
#  [[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
#  [{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
#  [<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
#  <{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.
#  Stop at the first incorrect closing character on each corrupted line.

#  Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the first illegal character on the line and look it up in the following table:

#  ): 3 points.
#  ]: 57 points.
#  }: 1197 points.
#  >: 25137 points.
#  In the above example, an illegal ) was found twice (2*3 = 6 points),
#  an illegal ] was found once (57 points),
#  an illegal } was found once (1197 points),
#  and an illegal > was found once (25137 points).
#
#  So, the total syntax error score for this file is 6+57+1197+25137 = 26397 points!

# Find the first illegal character in each corrupted line of the navigation subsystem. What is the total syntax error score for those errors?


def file_input(file1):
    for line in file1:
        input1 = line.strip('\n').strip()
        input.append(input1)


def count_opening(char, open_char, line, curr_pos):
#    print("in count routine")
#    print(line, curr_pos)
#    print(f"Opening chars {open_char} {line.count(open_char, 0, curr_pos+1)}")
#    print(f"Closing chars {char} {line.count(char, 0, curr_pos+1)}")
#   if line.count(char, 0, curr_pos+1) > line.count(open_char, 0, curr_pos+1):
    if (line.count('[', 0, curr_pos) != line.count(']', 0, curr_pos) and
            line.count('(', 0, curr_pos) != line.count(')', 0, curr_pos) and
            line.count('[', 0, curr_pos) != line.count(']', 0, curr_pos) and
            line.count('{', 0, curr_pos) != line.count('}', 0, curr_pos)):
#        print(f"Closing chars {line.count(char, 0, curr_pos+1)} Closing chars {line.count(open_char, 0, curr_pos+1)}")
        return True




#file1 = open('d10.inth', 'r')
file1 = open('d10.in', 'r')
scores = {')':3, ']':57, '}':1197, '>':25137}
total = 0
input = []

file_input(file1)

groups = {"(": ")", "[": "]", "{": "}", "<": ">"}
values = {")": 3, "]": 57, "}": 1197, ">": 25137}
msg_points = {")": 1, "]": 2, "}": 3, ">": 4}
err_scores = []
msg_scores = []

for line in input:
    score = 0
    found = []
    for char in line:
        if char not in [")", "]", "}", ">"]:
            found.append(char)
        else:
            if char == groups[found[-1]]:
                found.pop()
            else:
                err_scores.append(values[char])
                found = []
                break
    if found:
        for m in [groups[x] for x in found[::-1]]:
            score = (score * 5) + msg_points[m]
        msg_scores.append(score)

print(f"Part 1: {sum(err_scores)}")
print(f"Part 2: {sorted(msg_scores)[len(msg_scores)//2]}")

# Your puzzle answer was 265527.
# Your puzzle answer was 3969823589.
#  --- Day 8: Seven Segment Search ---
#  Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

#    0:      1:      2:      3:      4:
#   aaaa    ....    aaaa    aaaa    ....
#  b    c  .    c  .    c  .    c  b    c
#  b    c  .    c  .    c  .    c  b    c
#   ....    ....    dddd    dddd    dddd
#  e    f  .    f  e    .  .    f  .    f
#  e    f  .    f  e    .  .    f  .    f
#   gggg    ....    gggg    gggg    ....

#    5:      6:      7:      8:      9:
#   aaaa    aaaa    aaaa    aaaa    aaaa
#  b    .  b    .  .    c  b    c  b    c
#  b    .  b    .  .    c  b    c  b    c
#   dddd    dddd    ....    dddd    dddd
#  .    f  e    f  .    f  e    f  .    f
#  .    f  e    f  .    f  e    f  .    f
#   gggg    gggg    ....    gggg    gggg
#  So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.

# a: 8, b:5, c: 8, d: 7, e: 4, f: 9, g: 7


#  The problem is that the signals which control the segments have been mixed up on each display.
#  The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly.
#  Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

#  So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on:
#  the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on.
#  With just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.

#  For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

#  For example, here is what you might see in a single entry in your notes:

#  acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
#  cdfeb fcadb cdfeb cdbaf
#  (The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

#  Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

#  Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits.
#  Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

#  For now, focus on the easy digits. Consider this larger example:

#  be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
#  fdgacbe cefdb cefbgd gcbe
#  edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
#  fcgedb cgb dgebacf gc
#  fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
#  cg cg fdcagb cbg
#  fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
#  efabcd cedba gadfec cb
#  aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
#  gecf egdcabf bgf bfgea
#  fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
#  gebdcfa ecba ca fadegcb
#  dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
#  cefg dcbef fcge gbcadfe
#  bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
#  ed bcgafe cdgba cbgef
#  egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
#  gbdfcae bgc cg cgb
#  gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
#  fgae cfgab fg bagce
#  Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits.
#  Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

#  In the output values, how many times do digits 1, 4, 7, or 8 appear?


#   Digit       Inputs      Count	Unique
#   -----       ------      -----	------
#       0       abc efg         6		/6/ only remaining 6
#       1         c  f          2		Y
#       2       a cde g         5		/5/ only remaining 5 digit
#       3       a cd fg         5		/2/ Is '7' plus two digit 'd, g'
#       4        bcd f          4		Y
#       5       ab d fg         5		/3/ Is '6' less 'e' so look for 6 digit (that isn't '9') and 5 digit differing by one digit only
#       6       ab defg         6		/4/ having found '5' have '6'
#       7       a c  f          3		Y
#       8       abcdefg         7		Y
#       9       abcd fg         6		/1/ Is '4' plus two digit 'a, g'

#  --- Part Two ---
#  Through a little deduction, you should now be able to determine the remaining digits.
#  Consider again the first example above:

#  acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
#  cdfeb fcadb cdfeb cdbaf
#  After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:


#   Digit       Inputs      Count	Unique
#   -----       ------      -----	------
#       0       abc efg         6		/10/ only remaining 6
#       1         c  f          2		/1/
#       2       a cde g         5		/9/ only remaining 5 digit
#       3       a cd fg         5		/6/ Is '7' plus two digit 'd, g'
#       4        bcd f          4		/2/
#       5       ab d fg         5		/7/ Is '6' less 'e' so look for 6 digit (that isn't '9') and 5 digit differing by one digit only
#       6       ab defg         6		/8/ having found '5' have '6'
#       7       a c  f          3		/3/
#       8       abcdefg         7		/4/
#       9       abcd fg         6		/5/ Is '4' plus two digit 'a, g'

# /1/ 1: ab, /2/ 4: eafb, /3/ 7: dab, /4/ 8: acedgfb, /5/ 9: cefabd,
# /6/ 3: fbcad, /7/ 5: cdfbe, /8/ 6: cdfgeb, /9/ 2: gcdfa, /10/ 0: cagedb

#   dddd
#  e    a
#  e    a
#   ffff
#  g    b
#  g    b
#   cccc
#  So, the unique signal patterns would correspond to the following digits:

#  acedgfb: 8
#  cdfbe: 5
#  gcdfa: 2
#  fbcad: 3
#  dab: 7
#  cefabd: 9
#  cdfgeb: 6
#  eafb: 4
#  cagedb: 0
#  ab: 1
#  Then, the four digits of the output value can be decoded:

#  cdfeb: 5
#  fcadb: 3
#  cdfeb: 5
#  cdbaf: 3
#  Therefore, the output value for this entry is 5353.

#  Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

#  fdgacbe cefdb cefbgd gcbe: 8394
#  fcgedb cgb dgebacf gc: 9781
#  cg cg fdcagb cbg: 1197
#  efabcd cedba gadfec cb: 9361
#  gecf egdcabf bgf bfgea: 4873
#  gebdcfa ecba ca fadegcb: 8418
#  cefg dcbef fcge gbcadfe: 4548
#  ed bcgafe cdgba cbgef: 1625
#  gbdfcae bgc cg cgb: 8717
#  fgae cfgab fg bagce: 4315
#  Adding all of the output values in this larger example produces 61229.


# def containsAny(str, set):
#    """ Check whether sequence str contains ANY of the items in set. """
#    return 1 in [c in str for c in set]

# def containsAll(str, set):
#    """ Check whether sequence str contains ALL of the items in set. """
#    return 0 not in [c in str for c in set]

# def containsAny(str, set):
#    for c in set:
#        if c in str: return 1
#    return 0

# def containsAll(str, set):
#    for c in set:
#        if c not in str: return 0
#    return 1

# def containsAny(st, wanted_set):
#    for c in set:
#        if c in str: return 1
#    return 0

def match_digits(segments):  # segments is diag_input
    for wanted in (1, 4, 7, 8, 9, 3, 5, 2, 0):  # don't need 6 as get from 5
        match wanted:
            case 1:
                for i, digit in enumerate(segments):
                    if len(digit) == 2:
                        #						print(str("".join(sorted(set(digit)))))
                        dicty["".join(sorted(set(digit)))] = 1
                        print(
                            f"Code for '1' {set(list(dicty.keys())[list(dicty.values()).index(1)])} Code for '9' {set(digit)}")
                        segments.pop(i)
            case 4:
                for i, digit in enumerate(segments):
                    if len(digit) == 4:
                        dicty["".join(sorted(set(digit)))] = 4
                        segments.pop(i)
            case 7:
                for i, digit in enumerate(segments):
                    if len(digit) == 3:
                        dicty["".join(sorted(set(digit)))] = 7
                        segments.pop(i)
            case 8:
                for i, digit in enumerate(segments):
                    if len(digit) == 7:
                        dicty["".join(sorted(set(digit)))] = 8
                        segments.pop(i)
            case 9:
                for i, digit in enumerate(segments):
                    if len(digit) == 6:
                        if set(list(dicty.keys())[list(dicty.values()).index(4)]) < set(digit):
                            print(
                                f"Code for '4' {set(list(dicty.keys())[list(dicty.values()).index(4)])} Code for '9' {set(digit)}")
                            dicty["".join(sorted(set(digit)))] = 9
                            segments.pop(i)
                    else:
                        continue
            case 3:
                for i, digit in enumerate(segments):
                    if len(digit) == 5:
                        if set(list(dicty.keys())[list(dicty.values()).index(7)]) < set(digit):
                            dicty["".join(sorted(set(digit)))] = 3
                            segments.pop(i)
                    else:
                        continue
            case 5:
                for i, digit in enumerate(segments):
                    for j, digit2 in enumerate(segments):
                        if len(digit) == 6 and len(digit2) == 5:
                            if set(digit2) <= set(digit):
                                dicty["".join(sorted(set(digit)))] = 6
                                dicty["".join(sorted(set(digit2)))] = 5
                                segments.pop(i)
                                if i > j:
                                    segments.pop(j)
                                else:
                                    segments.pop(j - 1)
                        else:
                            continue
            case 2:
                for i, digit in enumerate(segments):
                    if len(digit) == 5:
                        dicty["".join(sorted(set(digit)))] = 2
                        segments.pop(i)
            case 0:
                for i, digit in enumerate(segments):
                    if len(digit) == 6:
                        dicty["".join(sorted(set(digit)))] = 0
                        segments.pop(i)


#	print(dict)

def seg_disp(dsply):
    total = 0
    for val in dsply:
        total = total * 10
        val2 = "".join(sorted(set(val)))
        #		print(f"Val {val}, setted {val2}")
        total += dicty[val2]
    #		print(dict[val2])
    print(total)
    return total


# file1 = open('d08.inth', 'r')
file1 = open('d08.in', 'r')

total = 0
for line in file1:
    diag = []
    display = []
    dicty = {}
    d = line.strip('\n').split('|')
    diag = d[0].strip().split(' ')
    display = d[1].strip().split(' ')
    match_digits(diag)
    total += seg_disp(display)
    print(f"RUNNING TOTAL {total}")
file1.close()

#  Your puzzle answer was 973292.

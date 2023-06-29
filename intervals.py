import mingus.core.intervals as intervals
import mingus.core.notes as notes
from random import choice, shuffle
import curses
from sys import argv

interval_names = {"1":{"Perfect Unison":"P1"},
 "b2":{"Minor 2nd":"m2"},
 "2":{"Major 2nd":"M2"},
 "b3":{"Minor 3rd":"m3", "Augmented 2nd":"A2"},
 "3":{"Major 3rd":"M3"},
 "4":{"Perfect 4th":"P4"},
 "b5":{"Triton":"TT", "Augmented 4th":"A4","Diminished 5th":"d5"},
 "5":{"Perfect 5th":"P5"},
 "b6":{"Minor 6th":"m6","Augmented 5th":"A5"},
 "6":{"Major 6th":"M6","Diminished 7th":"d7"},
 "b7":{"Minor 7th":"m7"},
 "7":{"Major 7th":"M7"},
 "8":{"Perfect Octave":"P8"}}

def shuffleDict(input):
  l = list(input.items())
  shuffle(l)
  return dict(l)

def main(stdscr, root):
	'''This is a tool to help a user study intervals. 
	The user passes in a root note and this generates all the intervals within an octave and quizes the user on them.
	It will only use each interval once in a session. If the interval has more than one name (ex: b3 == "Minor 3rd" and "Augmented 2nd"), it will randomly chooses one.
	It also randomly chooses to show either the descending or ascending interval first.

	The idea is to have the user:
	1. see an interval prompt
	2. determine the correct pair of notes
	3. sing each note
	4. check their sung notes with their instrument
	5. validate that they got identified the correct notes
	'''
	k = 0
	current = 0
	total = 0

	max_height, max_width = stdscr.getmaxyx()
	height = 24
	width = 80

	start_y = (max_height-height) // 2
	start_x = (max_width-width) //2

	stdscr.clear()
	stdscr.refresh()

	#Start colors in curses
	curses.start_color()
	curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

	shuffled_intervals = shuffleDict(interval_names)
	total = len(shuffled_intervals)
	
	#Render header
	header = "Root: {}".format(root)
	stdscr.attron(curses.color_pair(3))
	stdscr.addstr(start_y, start_x, header)
	stdscr.addstr(start_y, start_x+len(header), " " * (width - len(header) - 1))
	stdscr.attroff(curses.color_pair(3))

	for interval in shuffled_intervals:
		#Clear working lines
		stdscr.addstr(start_y+1, start_x+0, " "*width)
		stdscr.addstr(start_y+2, start_x+0, " "*width)

		#Render status bar
		current += 1			
		statusbarstr = f"Press 'q' to exit | Root: {root} | Progress: {current}/{total}"
		stdscr.attron(curses.color_pair(3))
		stdscr.addstr(start_y+height-1, start_x, statusbarstr)
		stdscr.addstr(start_y+height-1, start_x+len(statusbarstr), " " * (width - len(statusbarstr) - 1))
		stdscr.attroff(curses.color_pair(3))

		#Grab the intervals to be displayed
		name = list(shuffleDict(shuffled_intervals[interval]).values())[0]
		asc = intervals.from_shorthand(root, interval) 
		desc = intervals.from_shorthand(root, interval, False)
		if (not asc):
			asc = root
			desc = root

		notes = shuffleDict({"asc":asc, "desc":desc})
		first = list(notes.keys())[0]
		second = list(notes.keys())[1]

		#Display the test and wait on user input
		stdscr.addstr(start_y+1, start_x+0, f" {name.ljust(3)}  {first.ljust(4)} {second.ljust(4)}")
		k = stdscr.getch()
	
		#Display first test's answer
		stdscr.addstr(start_y+2, start_x+0, f"      {notes[first].ljust(3)}")
		k = stdscr.getch()

		#Display second test's answer
		stdscr.addstr(start_y+2, start_x+0, f"      {notes[first].ljust(3)}  {notes[second].ljust(3)}")
		
		k = stdscr.getch()
		if (k == ord('q')):
			break

#mingus does not provide a list of valid notes, so we've created our own
valid_notes = ["Ab", "A", "A#", "Bb", "B", "B#", "Cb", "C", "C#", "Db", "D", "D#", "Eb", "E", "E#", "Fb", "F", "F#", "Gb", "G", "G#"]

if (len(argv) > 1):
	if(notes.is_valid_note(argv[1])):
		curses.wrapper(main, argv[1])  
	else:
		print(f"Please pass in one of these notes: {valid_notes}")
else:
	curses.wrapper(main, "C")

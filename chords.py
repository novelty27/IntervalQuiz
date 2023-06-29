import mingus.core.intervals as mingus_intervals
import mingus.core.notes as notes
from random import choice, shuffle
import curses
from sys import argv

notes = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]
chords ["m", "M", "dim", 'aug' ,"sus4", "sus2", "m7", "M7", "7", "m7b5", "dim7", ‘"mM7", "7#5", "sus47"]

def shuffleList(input):
	shuffle(input)
	return input

def main(stdscr, interval_count):
	k = 0
	current = 0
	total = 0

	max_height, max_width = stdscr.getmaxyx()
	height = 24
	width = 80

	start_y = (max_height-height) // 2
	start_x = (max_width-width) //2
	status_y = start_y+height-1

	stdscr.clear()
	stdscr.refresh()

	#Start colors in curses
	curses.start_color()
	curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

	shuffled_notes = shuffleList(notes)
	interval_set = shuffleList(intervals)[0:interval_count]
	total = len(shuffled_notes)*interval_count
	missed = []

	# for interval in interval_set:
	# 	#Render header
	# 	header = "Interval: {}".format(interval)
	# 	stdscr.attron(curses.color_pair(3))
	# 	stdscr.addstr(start_y, start_x, header)
	# 	stdscr.addstr(start_y, start_x+len(header), " " * (width - len(header) - 1))
	# 	stdscr.attroff(curses.color_pair(3))

	# 	#Clear working lines
	# 	for i in range(1,len(shuffled_notes)+1):
	# 		stdscr.addstr(start_y+i, start_x+0, " "*width)
	# 	stdscr.addstr(start_y+len(shuffled_notes)+1, start_x+0, "-"*6)
	# 	work_y = start_y

	# 	for note in shuffled_notes:
	# 		#Render status bar
	# 		current += 1			
	# 		statusbarstr = f"Press 'q' to exit | interval: {interval} | Progress: {current}/{total} | Missed: {len(missed)}"
	# 		stdscr.attron(curses.color_pair(3))
	# 		stdscr.addstr(status_y, start_x, statusbarstr)
	# 		stdscr.addstr(status_y, start_x+len(statusbarstr), " " * (width - len(statusbarstr) - 1))
	# 		stdscr.attroff(curses.color_pair(3))

	# 		# Display the tests
	# 		stdscr.addstr(work_y+1, start_x+0, f" {note.ljust(3)}")
	# 		k = stdscr.getch()
			
	# 		#Display the test and wait on user input
	# 		stdscr.addstr(work_y+1, start_x+3, f" {mingus_intervals.from_shorthand(note, interval)}")
	# 		k = stdscr.getch()
	# 		if (chr(k).isalpha()):
	# 			missed.append([note, interval])
	# 		work_y+=1

	# #### Reset and quiz the missed intervals####
	# #Render header
	# header = "Missed Intervals"
	# stdscr.attron(curses.color_pair(3))
	# stdscr.addstr(start_y, start_x, header)
	# stdscr.addstr(start_y, start_x+len(header), " " * (width - len(header) - 1))
	# stdscr.attroff(curses.color_pair(3))

	# #Clear working lines
	# for i in range(1,len(shuffled_notes)+2):
	# 	stdscr.addstr(start_y+i, start_x+0, " "*width)
	# stdscr.addstr(start_y+len(missed)+1, start_x+0, "-"*11)
	# current=0
	# work_y = start_y

	# missed = shuffleList(missed)

	# for i in missed:
	# 		#Render status bar
	# 		current += 1			
	# 		statusbarstr = f"Press 'q' to exit | Missed Intervals | Progress: {current}/{len(missed)}"
	# 		stdscr.attron(curses.color_pair(3))
	# 		stdscr.addstr(status_y, start_x, statusbarstr)
	# 		stdscr.addstr(status_y, start_x+len(statusbarstr), " " * (width - len(statusbarstr) - 1))
	# 		stdscr.attroff(curses.color_pair(3))

	# 		# Display the tests
	# 		stdscr.addstr(work_y+1, start_x+0, f" {i[0].ljust(3)} {i[1].ljust(4)}")
	# 		k = stdscr.getch()
			
	# 		#Display the test and wait on user input
	# 		stdscr.addstr(work_y+1, start_x+7, f" {mingus_intervals.from_shorthand(i[0], i[1])}")
	# 		k = stdscr.getch()
	# 		work_y+=1

if (len(argv) > 1):
	curses.wrapper(main, int(argv[1])) 
else:
	curses.wrapper(main, 11) #7 for diatonic, 11 for full set

fifteen
=======

Crossword creator from 15-letter words and phrases.

This is an old script that I found whilst tidying up an old laptop. I wondered if it was possible to create a 15x15 crossword grid from 15-letter words and phrases. This was my attempt to find out.

Unfortunately I didn't find any solutions using the official Scrabble list of words plus as many phrases as I could find. Maybe someone out there with a bigger word list might have more success.

Run the script with the test file to see it in action.

# ./grid.py < test.txt

# ./grid.py --odd < test.txt

By default the script crosses the words on the even letters and produces a grid of 7 words across and 7 down. I thought this was the most likely way to fit in the words, since it needs fewer words.

Alternatively you can cross the words on the odd letters and produce a grid of 8 words across and 8 words down.

In both cases there are likely to be several words which have the same odd or even letters. So when a solution is found the script prints out the grid of crossing letters first (7x7 or 8x8) and then prints out the full list of words underneath that have those crossing letters.

The script is quite efficient, but it will take a few hours to run on a long list of words.

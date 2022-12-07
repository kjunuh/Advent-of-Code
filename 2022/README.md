# Writeup
*just some notes from the end of each day mostly so I can remember what went right/wrong*
## day 1
Can't believe I was late to the first day. Considering I got home around 12:08 and didn't have my editor or files set up at all, I think I did alright overall. Six minutes is a far cry from the two of the leaderboard, but I'd like to think I would have had a chance if I were set up and in the correct mental space. Maybe that's just wishful thinking, hopefully there are some easy ones later on where I can steal a point or two. Only programming notes from today were that I could have done input parsing a bit faster (I should have shaken off the python rust beforehand). 
## day 2
I feel pretty stupid right now. Just spent the past 24 minutes and 30 seconds making RPS gestures at a screen and still managing to mess it up. I thought about using a dict as a lookup table, but figured that it would take me longer to write than branching if statements. Either way would have been fine with editor shortcuts if I hadn't gotten the result of RPS wrong multiple times (turns out that rock does not beat paper). A dict probably would have been more straightforward to troubleshoot but to be honest it seems like I just can't keep track of things like this in my head. I spent so long looking at the if statements and not finding the obvious error. 
## day 3
A number of issues today. Kinda forgot how ascii codes work, had to google the `ord()` function and even then took me awhile to figure out how much to shift each value by. Tried to use `char.isupper` instead of `char.isupper()` (a byproduct of writing in ts I guess) which costed me some time. Forgot the `//` operator and foolishly used `math.floor` when finding the index to split the string by in part 1. I could have been a fair bit faster on part 2 as well, but misread the problem and thought that I was supposed to split each line into 3 instead of taking 3 lines at a time.
## day 4
I took more time than I should have doing input parsing and thinking about the problem. I probably should have realized that I could use simple greater/less than operators to test, but the way the example was written got me thinking about intersections. Had to google the `issubset()` method, but didn't cost me too much time. 
## day 5
Well that input parsing was annoying, took me awhile to think of the implementation I ended up with. Other than that I just need to think things over instead of doing trial and error; I was just changing the list slicing indices around based on what came to mind at first trying to go fast, but lost time overall compared to if I had just taken a second to think about it, especially in the second part. First part was not bad overall. 
## day 6
Probably my best chance to leaderboard so far (esp since I was late to the first day), but still too slow by a factor of almost 2. Wasted some time turning my code into a function because for some reason I completely forgot that `break` existed, took me longer than I would like to read/interpret the prompt. Could have also used a normal python list, but for some reason my mind jumped to a deque and that took extra time as well. I'm pretty happy with rank 689 for part 2, but slightly annoyed knowing that I probably could have done better. 
## day 7
I'm just slow and dumb. Worst day yet by a long shot. The problem itself was easy enough to understand, I guess I'm just tired? or bad at programming? probably both. Tried solving non-recursively at first, failed, then tried solving recursively, which worked on the test input but segfaulted on the real one (still not entirely sure why to be honest, I think it was calculating some values twice but idk), then finally went back to going line by line and eventually figured it out after a painfully slow 2 hours and 12 minutes. I enjoy watching [Jonathan Paulson's](https://www.youtube.com/watch?v=ZPM5xclRInk) live code/breakdowns after I finish, and was at least happy to find that my final solution was logically almost identical to his (though a fair bit less elegant). Oh, also, I should use defaultdicts for prety much everything in the future, not that it matters much if I'm going to be this slow.
## personal stats
```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  7   02:12:34  12417      0   02:27:07  12067      0
  6   00:03:54   1122      0   00:04:10    689      0
  5   00:18:50   2434      0   00:34:55   5278      0
  4   00:09:22   4208      0   00:09:56   2445      0
  3   00:11:50   3684      0   00:16:45   2787      0
  2   00:17:22   7033      0   00:24:30   6278      0
  1   00:12:31   6228      0   00:14:13   5241      0
```
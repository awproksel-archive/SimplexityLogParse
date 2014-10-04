
## SimplexityLogParse

The term Simplexity comes from Jeffrey Kluger's book of the same name that tries to explain why simple things become complex and how complex things can be made simple.

This log parser was an interview question and I went overboard with structure and complicated the hell out of it.  In fact the ask could be handled in a single terminal command. (Hint: http://man.cx/uniq)

Repo contains an example file for parsing, as long as it is ran in the same file as the .py it will just output the results.  

A few people have asked me what the `uniq` command would be to do what this program does in a single line.  With the given structure of the included apache log file you could use this: `cat apache.log | awk '{print $4}' | sort -n | uniq -c | sort -nr | head -10`.  

Walking through the command:

* cat apache.log prints the contents of the file: `apache.log` to the screen
* however in this case we "pipe" or `|` the results to the next command 
* `awk '{print $4}'` looks at text and returns the 4th column of information, in this case the requesting IP
* again we "pipe" the result to the next command
* `sort -n` performs a numberic sort on the data, basically organizing all the like numbers next to each other
* more "pipe"-ing
* `uniq -c` takes line of import and counts the time number of times it exists in the dataset
* (can you tell by now that "pipes" are amazing?)
* we sort again, this time reversing the numberic sort
* (seriously, how many pipes can one command have? A LOT!)
* lastly we only want to display the top results and `head -10` gives up the top 10 results

Any questions? 

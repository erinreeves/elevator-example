# elevator-example
## Brief Summary
This simulates an elevator traelling the user specified floors. At the end of the trip it gives some trip information.

While this isn't the most efficient elevator it always goes to the closest next floor from where it currently is;
 starting at the first floor given in the list string of floors.

## Usage
### User Input
* The user input should be a comma delimited list of positive or negative numbers.

* There is validation of this and the program will end if invalid input is given.
### Execution Command
From the root directory you can execute `python -m elevator` to run the program

At the end of the execution a summary will be displayed of the stored/calculated trip information.


## Future Work Ideas
There is always room for improvements or diversity in functionality:

Perhaps all static methods and a data class just to store the trip information makes sense.

Adding more efficient, or simply different, methods for different elevator behaviors could be interesting.
Such as Dijkstra's algorithm or one that travels the floors in the user given order.


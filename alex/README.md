# CS347-bin-packing
Alex is the default provided for solving bin-packing problems. It greedily places items in the first container they fit in.

## Usage:

/newproblem/\<int:size>: creates a new problem with given size. Returns a dict with:

    - "problemID": an integer ID needed for later calls
    - "binEncoding": a sring encoding the newly created bin

/placeitem/\<problemID>/\<int:itemSize>: places the item in the first bin it fits in and returns a dict with:

    - "ID": the problemID
    - "size": the size of the placed item
    - "loc": which bin the item was placed in
    - "bins": a string encoding of the new state

/endproblem/\<problemID>: prevents future items being added and returns a dict with:

    - "ID": the problemID
    - "size": the total size of all placed items
    - "items": the total number of placed items
    - "count": the number of bins used
    - "wasted": the total space available in bins minus the total size of placed items
    - "bins": a string encoding of the final state


## Credit:
Alex was modified from code provided by Matthew Lepinski
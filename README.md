# pcgenerator

This is a simple program that generates an SVG file used to cut a punchcard on a die cutter.

The program takes a single file name as an argument:

    gen-punchcard.py sample.txt
    
The file must contain the pattern as a series of characters indicating where the punch holes go. An 'x' or 'X' will be punched. Any other character (including spaces) will not be punched.

A sample file looks like this:

    x-----------x-----------
    -x-----------x----------
    --x-----------x---------
    ---x-----------x--------
    ----x-----------x-------
    -----x-----------x------
    ------x-----------x-----
    -------x-----------x----
    --------x-----------x---
    ---------x-----------x--
    ----------x-----------x-
    -----------x-----------x
    x-----------x-----------
    -x-----------x----------
    --x-----------x---------
    ---x-----------x--------
    ----x-----------x-------
    -----x-----------x------
    ------x-----------x-----
    -------x-----------x----
    --------x-----------x---
    ---------x-----------x--
    ----------x-----------x-
    -----------x-----------x
    x-----------x-----------
    -x-----------x----------
    --x-----------x---------
    ---x-----------x--------
    ----x-----------x-------
    -----x-----------x------
    ------x-----------x-----
    -------x-----------x----
    --------x-----------x---
    ---------x-----------x--
    ----------x-----------x-
    -----------x-----------x

If the pattern doesn't contain enough rows to create a card of the minimum length, you must repeat the pattern one or more times to make the card long enough.

The number of rows and stitches on the card are determined by the number of rows and columns in the file.

By default, the program is configured to print 24-stitch cards. However, you can change the stitch_width variable to accommodate 12-stitch cards.

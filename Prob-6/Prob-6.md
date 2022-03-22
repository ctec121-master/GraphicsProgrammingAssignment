# Graphics - Problem 6

**Goal**

- Gain further experience with graphics objects

**Instructions**

Using the graphics library, develop a Python program to draw the a set of LEGO bricks. The desired output is shown below.

**Suggested Development Process**

- Develop a working solution for a single brick first
- Then extend that to produce a complete solution
- Once you have a complete working solution, copy the work in a file, then make update your work for bonus points.
- Time box your effort. Set what you think is a realistic time allotment for your work. If you are having problems at the end of the time allotment, ask for help.

**Alternative 1**

- One long program - just a sequence of draw commands. This will get you the basic points
- Instead of creating each object using a class from the library, clone a previously created object and use the move method to form the next brick. This is still long and tedious, but it shows use of "advanced" functionality. Bonus points for this.

**Bonuses**

- Using cloning.

**Alternative 2**

- Create a solution using functions to draw a brick
- From main() call that function 6 times to draw the 6 bricks.
- Possible function parameters
  - application window object
  - Point object for lower left corner of brick.
  - length of brick. Use this and the lower left corner point to calculate all the info needed to draw the rectangles that comprise a brick
  - color of brick
- Possible utility function
  - drawRect (win, lowerLeftCornerPoint, length, color)
  - the drawBrick function calls this function to draw the main brick rectangle as well as the 5 nib rectangles.

**Bonuses**

- Partial bonuses are possible and points scale with completeness of solution.

![Desired output](LEGOS.png)

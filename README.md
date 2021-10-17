# 2048_game
Design principles:
I have used functional programming which helps when we require same piece of code again. I have added comments to make it readable

Thoughts/probable solution/problems faced:
For merging up and down i have used transpose method and reused mergeleft and merge right code.
To display the board in an elegant way i have used length of largest number to add even spaces in the board.
To check whether player lost i have made two copies of the board and if by performing each operation on copy1 if for each instance it matches copy2 then we can say player lost

scope of making it 8x8:
i have used a single variable for the board size. So, by changing it's value to 8 will change my board size to 8.

change 2048 to 4096 as endnumber:
in the function name won changing 2048 to 4096 will change my end number.


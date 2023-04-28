# Bots

--------
- **RandomAI**: This bot is designed as our control.
  It evaluates all possible moves and chooses one at
  random. As expected, the RandomAI didn’t perform 
  all that well in the game, with its score often 
  ending in the negatives.

- **BelnapAI**: ----

- **RolloAI**: This bot is an optimization of the
  RandomAI, designed to filter the options to 
  only the most advantageous. This includes 
  choosing and saving resources for desired routes.

- **TrentonAI**: This bot reflects a greedy 
  approach to the game — for each turn it takes,
  it will choose the action that will award the 
  most points in this immediate round. Since points
  in individual rounds are most often granted by
  building routes, it has a strong bias towards
  building routes. If all other options are the
  same, it will choose randomly from the available
  options.
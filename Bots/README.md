# Bots

--------
- **RandomAI**: This bot is designed as our control.
  It evaluates all possible moves and chooses one at
  random. As expected, the RandomAI didn’t perform 
  all that well in the game, with its score often 
  ending in the negatives.

- **BelnapAI**: This bot was made to fall on the 
  extreme side of scheduling and exploiting 
  resources. The bot resembles the random bot 
  with a few key differences: this bot will buy 
  railroads as often as possible, and will never 
  choose to take a new route. This leads to shorter
  games in which this bot is included. 
  The assignments in class seemed to suggest that 
  the more outside influences, decreasing returns, 
  and dwindling options present, the sooner it made
  sense to switch from exploring to exploiting. 
  This bot intended to capitalize on these 
  observations by wasting zero time exploring.

- **DeterministicAI**: This bot was designed to 
  be non-random. If given the exact same options
   for repeated games, this bot would make exactly
  the same decisions every time. This bot helps 
  us to consider the impact of randomness being 
  present in the other bot’s performance. It’s 
  decision-making follows a simple pattern, it 
  draws a new route card if it has no uncompleted 
  routes, then it builds railroads if there is a 
  possible railroad it can build, and finally it 
  draws new train cards as a default base case.

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
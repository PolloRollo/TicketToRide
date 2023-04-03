# Ticket To Ride

Designing decision-making agents to play Ticket to Ride.

--------

### Game Environment

- Initializes a board, shuffled resource deck, and shuffled route deck
- Initialize players
- Deal initial resources and routes
- Alternate between players
- Check end game conditions

### Map

- Graph initialized unclaimed, all roads weighted by length and color
- Graph updated when road claimed



### Resource Deck

- Initialize resource deck, shuffle
- Set out 5 cards
- Check for card reset

### Route Deck

- Initialize route deck, shuffle


### Player

- Decide between 3 action: Draw resources, build, or draw routes.
    - Draw resources: Depends on what resources are shown and needed.
    - Build: Depends on roads available, desired destinations, and what resources are owned.
    - Draw routes: Desirable if current routes are complete.

- Decide between which resources
- Decide between which roads to build
-



Are players inside game
or do players interact with game
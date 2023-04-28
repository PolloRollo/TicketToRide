# Ticket To Ride

Designing decision-making agents to play Ticket to Ride.

--------
Main.py is ready to run an example of our program.

### Game Environment

- Initializes a 
    - Map (network)
    - Resource deck (shuffled)
    - Route deck (shuffled)
- Initialize players, deals initial resources and routes
- Alternate between players taking turns
- Check end game conditions

### Player

- Decide between 3 action: Draw resources, build, or draw routes.
    - Draw resources: Depends on what resources are shown and needed.
    - Build: Depends on roads available, desired destinations, and what resources are owned.
    - Draw routes: Desirable if current routes are complete.

- Decide between which resources
- Decide between which roads to build


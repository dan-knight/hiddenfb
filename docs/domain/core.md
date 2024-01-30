# Core Domain Modeling

The scope of current domain models is limited to the MVP report, which will include xG and Pitch Control. This can and should be extended later, but early optimization should be avoided wherever possible. Some measures have been taken to ensure future flexibility, but usually through exclusion rather than extra domain modeling.

## Basic Concepts

The ideas of **players**, **matches**, and **teams** are not necessarily tied to real events. For example, consider simulated data. These hypothetical player positions and actions need not be based on any real matches or players. In fact, there is considerable utility in removing the individuals entirely, modeling the prototypically "average" player. So, these models represent the underlying *idea* of a player or match.

Of course, it will be necessary in future to tie these domain models to their real-life entities. The modeling practices here have been left open to these extensions.

## Moments and Actions

In order to more faithfully model the relationship between player locations and actions, these domain models have diverged from the shape of the underlying tracking and event data. These **moments** represent a combined action and location, as it is (theoretically) impossible to separate the two concepts. For example, a shot must be taken from a specific place on the pitch by a specific player. Further, there is a wider context for each action to consider: the match, the time, and the positions and actions of *other players*. A **match moment** provides this context for **player moments**. While player moments do not always require the context of other players to be useful, the match moment can also act as part of a unique identifier. (Alongside the player, there should only be one player moment per player per frame of a match).

## Next Steps

These models represent the bare minimum for creating useful statistical models. As more models and analyses are added, these domain models will surely evolve to capture these use cases. Until then, they are simply representations of tracking and event data.
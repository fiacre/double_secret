
DISCUSION: 

Traveling Salesman Problem
Ye olde TSP ... a well know NP-Hard problem 
Given N cities, c1, c2, c3 .. cN a traveling salesman must visit
each city while minimizing cost.  For this case the cost function
is simply the euclidean distance.  (in real world optimization problems
availablity of resources, actual distance for a given transport medium,
projective (non-euclidean) distance for flight -- adjusting for wind 
and weather and a myriad of other considerations make such optimization
problems the stuff of supercomputer lore.)

As an NP-Hard problem it is known[1] that there is no algorithm
that minimizes the cost (distance) of the salesman's travel to N cities
that is not asymptotic in N.  equivalently there is no general algorithm that
solves the general TSP in polynomial time.

Since it is computationally expensive to try every combination (for
k cities O(k) = k! (or other asymptotic results)) any heuristic
that runs on polynomial time is an improvement over brute force,
so long as it gives a *reasonably* acceptable answer

Simulated Annealing is a metaheuristic that uses Monte-Carlo methods
and a "cooling" schedule to avoid getting stuck on a local maximum.
(greedily seeking a minimum cost may miss a globally better minimum)

Given a discrete optimization problem (such as an approximation of TSP)
Simulated Annealing has two advantages.  1. the algorithm will run in a
fixed amount of time.  2. the algorithm will avoid "getting stuck" on
one local optimization point, increasing the probability that a global
optimization will be found.

An implementation of SA has a fixed cooling schedule (satisfying advatage 1)
and, has been demonstrated, yields better results in practice by randomly
selecting a solution, s then randomly trying another solution, s' and iterating 
depending on:
    if cost(s') < cost(s):
        choose s'
    else if cost(s') > cost(s):
        *Maybe* move to s'

Each iteration has a "temperature"  and each choice to move to a state, s', that
has a higher cost that the current state is a fuction of the current temperature and
a random variable, r in (0, 1] , as the temperature decreases, choosing a higher
cost is less likely.

Thus, SA moves from state to state randomly but slowly decreases the likelihood
of choosing a state that has a higher cost than any previous states until
(hopefully) a global optimized state is found or the algorithm stops.

In practice this has been shown to be more likely to find an optimization that
is close to a global optimization.


For this assignment, I use flask to create a REST interface.  And unabashadly 
steal https://github.com/perrygeo/simanneal, with very minor modifications.

INSTUCTIONS: 

Use python 3.5
from a terminal on OSX or Linux create a virtualenv and source in that environment
run pip install -r requirements.txt
python tsp.py

from another terminal:

curl -H 'Content-Type: application/json' --data @anneal.json localhost:5000/anneal



[1] an open problem, I assume P != NP and leave the proof
(or counterexample) as an exercise :-)  

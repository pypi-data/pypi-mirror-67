#! /usr/bin/python

from enum import Enum
from .population import *
from typing import List, Set, Dict, Tuple, Optional
from abc import ABC, abstractmethod

# TODO: consider creating individual selectionmethod classes with the various methods and properties so that
# parameters can be set etc. For example tournament may benefit from a change in the tour size and probability
# but other types don't
# also new selection types can be added.
# SEE Tournament Selection BELOW

# Parent Selection Method Enumerator
# class ParentSelectionMethod(Enum):
#
#     # Tournament selection involves executing several "tournaments" using individuals chosen
#     # at random from the population. The winner of each tournament is selected.
#     tournament_selection = 0
#
#     # This method is often referred to as Roulette Wheel selection The analogy to a roulette
#     # wheel can be envisaged by imagining a roulette wheel in which each candidate solution
#     # represents a section of the wheel. The size of the sections are proportionate to the
#     # probability of selection of the solution. This means that fitter solutions are more
#     # likely to be selected but all solutions have a chance.
#     fitness_proportionate_selection = 1
#
#     # Stochastic Universal Sampling is a development of fitness proportionate selection.
#     # Where FPS chooses several solutions from the population by repeated random sampling,
#     # Stochastic Universal Sampling uses a single random value to sample all of the solutions
#     # by choosing them at evenly spaced intervals. This gives weaker members of the population
#     # a better chance of being chosen.
#     stochastic_universal_sampling = 2
#
#     random_selection = 3


class ParentSelectionType(ABC):

    @abstractmethod
    def select_parents(self, chromosomes: List, n: int = 2):
        pass


class RandomSelection(ParentSelectionType):

    def select_parents(self, chromosomes: List, n : int = 2):

        """Returns n parents from the population."""

        return random.sample(chromosomes, n)


class FitnessProportionateSelection(ParentSelectionType):

    def select_parents(self, chromosomes: List, n: int = 2):

        # Roulette Wheel
        # (Davis, 1992, P.14-15
        #
        # sum the fitness of all the population (TotalFitness)
        # generate n (random between 0 and total fitness
        # return the first population member whose fitness
        # added to the fitness of the precedeing population
        # members is greater or equal to n.

        # TODO: Consider Normlised Fitness...
        total_fitness = sum([o.fitness for o in chromosomes])
        parents = []

        i = 0

        while i < n:
            parents.append(self._fps_select(chromosomes, random.uniform(0.0, total_fitness)))
            i += 1

        return parents

    def _fps_select(self, chromosomes: List, rand_num: float):

        # Separated from above in order to unit test
        running_total = 0.0

        for chromosome in chromosomes:

            running_total += chromosome.fitness
            if running_total >= rand_num:
                return chromosome

        return None


class TournamentSelection(ParentSelectionType):

    def __init__(self):

        # In the first variant of tournament selection, you can control the selective pressure by specifying the
        # tournament size, the number of members chosen to compete for parenthood in each tournament. This number
        # should be two or greater, with two implying the weakest selection pressure. Tournament sizes from two
        # to ten have been successfully applied to various GA optimizations, with sizes over four to five
        # considered to represent strong selective pressure.
        #
        # The second variant of tournament selection provides weaker selective pressure than the first variant
        # just described. The tournament size is set at two, and the member with the best objective value is
        # chosen with a probability that you specify. This best-player-wins probability can range from 0.5 to 1.0,
        # with 1.0 implying that the best member is always chosen (equivalent to a conventional tournament of size
        # two) and 0.5 implying an equal chance of either member being chosen (equivalent to pure random selection).
        # Using this option, you could set the best-player-wins probability close to 0.5 in the initial stages of
        # the optimization, and gradually increase it to strengthen the selective pressure as the optimization
        # progresses, in a similar manner to the simulated annealing optimization technique.


        # TODO: consider implementing probability in the range 0.5 to 1.0 when k = 2
        # 0.5 is an equal chance of either being selected, 1.0 means fittest always selected
        # e.g.
        # choose k (the tournament size) individuals from the population at random
        # choose the best individual from pool/tournament with probability p
        # choose the second best individual with probability p*(1-p)
        # choose the third best individual with probability p*((1-p)^2)
        # and so on...

        # self.probabilty = 1.0

        self.tour_size = 2

    def select_parents(self, chromosomes: List, n : int = 2):

        # Algorithm --
        # 1.Select k individuals from the population and perform a tournament amongst them
        # 2.Select the best individual from the k individuals
        # 3. Repeat process 1 and 2 until you have the desired amount of population

        parents = []

        for i in range(n):
            tour = self._get_tour(chromosomes, self.tour_size);
            parents.append(self._get_max_chromosome(tour))

        return parents

    def _get_tour(self, chromosomes: List, k: int = 2):
        """Separated out for unit testing."""
        return random.sample(chromosomes, k)

    def _get_max_chromosome(self, chromosomes: List):
        """Separated out for unit testing."""
        return max(chromosomes, key=attrgetter('fitness'))


class StochasticUniversalSamplingSelection(ParentSelectionType):

    def select_parents(self, chromosomes: List, n: int = 2):

        total_fitness = self.total_fitness()
        parents = []

        # get the distance between pointers
        point_distance = total_fitness / n;
        starting_point = random.random() * point_distance;

        pointers = []

        for i in range(n):
            pointers.append(starting_point + (i * point_distance))

        # now the roulette part
        index = 0
        fitness = 0.0

        for point in pointers:

            selected = False
            while not selected:
                fitness += self.chromosomes[index].fitness
                if fitness < point:
                    index += 1
                else:
                    parents.append(self.chromosomes[index])
                    break

        return parents

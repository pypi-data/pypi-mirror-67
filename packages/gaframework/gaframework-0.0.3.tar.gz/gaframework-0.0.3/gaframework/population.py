#! /usr/bin/python


from enum import Enum
from operator import attrgetter
from gaframework.ga import *
from gaframework.chromosome import *
from gaframework.parent_selection_method import *
from gaframework.chromosome import *
from gaframework.exceptions import *


class Population:

    def __init__(self, chromosomes: list, parent_selection_type: ParentSelectionType):

        self.chromosomes = chromosomes
        if isinstance(parent_selection_type, ParentSelectionType):
            self.parent_selection_type = parent_selection_type
        else:
            raise ParentSelectionTypeError("The parent selection type must be an instance of ParentSelectionType.")

    def select_parents(self, n: int = 2):

            try:
                return self.parent_selection_type.select_parents(self.chromosomes, n)

            except AttributeError as ex:
                # simply re-raise for now
                raise ex

    def get_elites(self):

        return [c for c in self.chromosomes if c.elite]

    def clear_elites(self):

        for c in self.chromosomes:
            c.elite = False

    def total_fitness(self):
        """
        Reurns the sum of the fitness value of each chromosome in the population.
        :return:
        """
        #TODO: Consider Normlised Fitness...
        return sum([o.fitness for o in self.chromosomes])

    def worst_chromosome(self):
        """
        Returns the chromosome with the lowest fitness value.
        """
        return min(self.chromosomes, key=attrgetter('fitness'))

    def best_chromosome(self):
        """
        Returns the chromosome with the highest fitness value.
        """
        return max(self.chromosomes, key=attrgetter('fitness'))

    def top(self, n: int):
        """
        Returns the top n chromosomes sorted in reverse order
        :param n:
        :return:
        """
        return sorted(self.chromosomes, key=lambda x: x.fitness, reverse=True)[:n]

    def __str__(self):

        s = ""
        for chromosome in self.chromosomes:
            s += str(chromosome) + "\r\n"
        return s

    def __repr__(self):

        return self.__str__()

    def __len__(self):

        return len(self.chromosomes)
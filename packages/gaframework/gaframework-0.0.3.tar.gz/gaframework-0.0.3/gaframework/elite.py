#! /usr/bin/python3

import math

from gaframework.genetic_operator import *
from gaframework.population import *
from gaframework.event import *
from gaframework.event_args import *


class Elite(GeneticOperator):

    def __init__(self, percentage: float = 5.0):

        super().__init__(percentage)

    def invoke(self, population, fitness_function):

        if self.enabled:

            # reset the elite flag for the whole population
            population.clear_elites()

            temp = sorted(population.chromosomes, key=lambda x: x.fitness, reverse=True)

            p = len(population) * (self._p/100)
            elites = temp[:math.ceil(p)]

            for elite in elites:
                elite.elite = True



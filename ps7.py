# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
# Name:
# Collaborators:
# Time:

import numpy
import random
import matplotlib.pyplot as plt

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb


        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        # TODO

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        # TODO
        doesNotClear = random.random()
        if self.clearProb > doesNotClear:
            return True
        else:
            return False


    
    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent). 


        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        # TODO
        ProbReproduce = self.maxBirthProb * (1 - popDensity)
        ProbNotReproduce = random.random()


        if ProbReproduce > ProbNotReproduce:
            newVirus = SimpleVirus(self.maxBirthProb,self.clearProb)
            return newVirus
        else:
            raise NoChildException()



class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        # TODO

        self.viruses = viruses
        self.maxPop = maxPop


    def getTotalPop(self):

        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """

        # TODO  
        currentTotPop = len(self.viruses)   
        return currentTotPop   


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO
        survivingViruses = []
        for virus in self.viruses:
            if not virus.doesClear():
                survivingViruses.append(virus)


        pop_density = float(len(survivingViruses))/self.maxPop
        self.viruses = survivingViruses


        offsprings = []
        
        
        for virus in survivingViruses:
            try:
                child = virus.reproduce(pop_density)
                offsprings.append(child)
            except NoChildException:
                pass

        self.viruses = survivingViruses + offsprings
        return self.getTotalPop()

    

#
# PROBLEM 2
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """

    # TODO
    
    #finalResults = None

    for i in range(0, numTrials):
        results = runSimulation(numViruses, maxPop, maxBirthProb, clearProb)
        if finalResults == None:
            finalResults = results
        else:
            for j in range(0, len(results)): ## wasn't doing this, so new values from other trials weren't getting added in 
                finalResults[j] += results[j]

    for i in range(0, len(finalResults)): ## same as above, didn't iterate to add all the new values
        finalResults[i] /= float(numTrials)
    
    plt.plot(finalResults, label = "SimpleVirus")
    plt.title("SimpleVirus simulation")
    plt.xlabel("time step")
    plt.ylabel("# viruses")
    plt.legend(loc = "best")
    plt.show()


def runSimulation (numViruses, maxPop, maxBirthProb, clearProb):
    """ helper function for doing one simulation run """
    viruses = []
    
    for i in range(0, numViruses):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))

    patient = Patient(viruses, maxPop)

    numSteps = 300
    numVirusesEachStep = []
    for i in range(0, numSteps):
        numVirusesEachStep.append(patient.update())

    return numVirusesEachStep

if __name__ == '__main__':
    sim = simulationWithoutDrug()


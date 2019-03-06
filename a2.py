"""CSCA08 Assignment 2, Fall 2017
 I hereby agree that the work contained herein is solely my work and that I
 have not received any external help from my peers, nor have I used any
 resources not directly supplied by the course in order to complete this
 assignment. I have not looked at anyone else's solution, and no one has
 looked at mine. I understand that by adding my name to this file, I am
 making a formal declaration, and any subsequent discovery of plagiarism
 or other academic misconduct could result in a charge of perjury in
 addition to other charges under the academic code of conduct of the
 University of Toronto Scarborough Campus
 Name: Dean Husar
 UtorID: husardea
 Student Number: 1004311906
 Date: November 29, 2017
"""


class IllegalChromosomeValue(Exception):
    ''' An exception raised when an Animal or child class of Animal attempts
    to create a chromosome that's number is larger than the maximum amount of
    chromosomes it can have.
    '''
    def __str__(self):
        return "ChromosomeNum > self._max_chromosomes or ChromosomeNum < 0"


class Animal():
    ''' This class represents any living organism that has chromosomes and DNA.
    its purpose is to store chromosomes. The chromosome numbers will start
    from zero.
    '''
    def __init__(self):
        '''(Animal) -> NoneType
        Creates a dictionary to store Chromosomes
        '''
        # create empty dictionary
        self._chromosomes = {}
        self._markers = {}
        self._max_chromosomes = 22

    # Getters and Setters

    def get_chromosomes(self):
        '''(Animal) -> dict of {int:Chromosome}
        '''
        return self._chromosomes

    def get_markers(self):
        '''(Animal) -> dict of{str:Pair or NoneType}
        '''
        return self._markers

    def get_max_chromosomes(self):
        '''(Animal) -> int
        Returns _max_chromosomes value
        '''
        result = self._max_chromosomes
        return result

    def set_max_chromomosomes(self, new_max):
        '''(Animal, int) -> NoneType
        Sets _max_chromosomes to given integer
        REQ: int > 0
        '''
        self._max_chromosomes = new_max

    def set_by_pos(self, ChromosomeNum, position, NewPair):
        '''(Animal, int, int, str) -> NoneType
        Takes the chromosome num, saves the specific nucleotide pair to that
        chromosome at that position
        REQ: len(NewPair) == 2
        REQ: NewPair can only contain the letters 'ATGC'
        '''
        # if the chromosome number is greater than the number of allowed
        # chromosomes raise an error
        if(ChromosomeNum > self._max_chromosomes or ChromosomeNum < 0):
            raise IllegalChromosomeValue

        # check if there is already a chromosome in the dictionary
        # set the chromosomes pair at position to nucleotide_pair using its
        # built in method
        # if no chromosome is present create a new one named after the
        # ChromosomeNum

        if(ChromosomeNum in self._chromosomes):
            self._chromosomes[ChromosomeNum].set_by_pos(position, NewPair)
        else:
            self._chromosomes[ChromosomeNum] = Chromosome()
            self._chromosomes[ChromosomeNum].set_by_pos(position, NewPair)

    def get_by_pos(self, ChromosomeNum, position):
        '''(Animal, int, int) -> str
        returns the nucleotide pair from the given chromosome at the given
        position
        '''
        # find the ChromosomeNum in the dict: _chromosomes
        # run the chromosome's built in method: get_by_pos
        # return the string value found
        # if no pair is found, method will return None
        try:
            x = self._chromosomes[ChromosomeNum].get_by_pos(position)
            if (type(x) == Pair):
                result = str(self._chromosomes[ChromosomeNum]
                             .get_by_pos(position))
            else:
                result = ""
            return result
        except:
            return ""

    def set_marker(self, MarkerID, ChromosomeNum, position):
        '''(Animal, str, int, int) -> NoneType
        Using the chromosome number and position, creates a marker that saves
        the value of the nucleotide at that point.
        REQ: ID != ""
        REQ: ChromosomeNum > 0
        '''
        # if ChromosomeNum > _max_chromosomes raise error
        if(ChromosomeNum > self._max_chromosomes or ChromosomeNum < 0):
            raise IllegalChromosomeValue
        else:

            # add a new Marker to the dictionary that hold markers
            # save the chromosome number and nucleotide position in the Marker
            self._markers[MarkerID] = Marker(ChromosomeNum, position)

    def set_by_marker(self, MarkerID, NewPair):
        '''(Animal, str, str) -> NoneType
        Using the MarkerID string, searches through the saved markers,
        finds the chromosome and position of the pair, changes the
        corresponding pair to NewPair.
        given pair.
        REQ: MarkerID != ""
        REQ: len(NewPair) == 2
        REQ: NewPair can only contain the letters 'ATGC'
        '''
        # get the marker from the markers dictionary
        # get chromosome number and nucleotide position from the
        # marker class saved
        # run Animal's built in set_by_pos function

        self.set_by_pos(self._markers[MarkerID].get_chromosome_num(),
                        self._markers[MarkerID].get_position(), NewPair)

    def get_by_marker(self, MarkerID):
        '''(Animal, str) -> str
        Using the MarkerID searches through the saved markers, finds the
        chromosome and position of the pair and returns string representation
        of the pair.
        REQ: MarkerID != ""
        '''
        # get the marker from the markers dictionary
        # get chromosome number and nucleotide position from the
        # marker class saved
        # run Animal's built in get_by_pos function

        x = self.get_by_pos(self._markers[MarkerID].get_chromosome_num(),
                            self._markers[MarkerID].get_position())
        if (type(x) == str):
            result = str(x)
        else:
            result = ""
        return result

    def get_chromosome(self, ChromosomeNum):
        '''(Animal, int) -> Chromosome
        Finds Animal's chromosome based off its corresponding integer.
        '''
        # if nothing is found, string None will be returned

        # if ChromosomeNum > _max_chromosomes raise error
        if(ChromosomeNum > self._max_chromosomes or ChromosomeNum < 0):
            raise IllegalChromosomeValue
        else:
            return self._chromosomes[ChromosomeNum]

    def set_chromosome(self, ChromosomeNum, NewChromosome):
        '''(Animal, int, Chromosome) -> NoneType
        Given a chromosome # and a New chromosome replaces the original
        chromomsome with NewChromosome.
        REQ: 0 <= ChromosomeNum <= self._max_chromosomes
        '''
        # if ChromosomeNum > _max_chromosomes raise error
        if(ChromosomeNum > self._max_chromosomes or ChromosomeNum < 0):
            raise IllegalChromosomeValue
        else:

            # subtract 1 from ChromosomeNum in order to obtain the proper index
            # for the dictionary

            # set the key of the dictionary to be ChromomsomeNum
            self._chromosomes[ChromosomeNum] = NewChromosome


# ANIMAL CHILD CLASSES

class Query(Animal):
    '''This class represents a Query that has chromosomes with
    nucleotide pairs in them. Its purpose is to store up to 23 chromosomes to
    be compared against a Human class in its test method.
    '''
    def __init__(self):
        '''(Query, int) -> NoneType
        Creates a Query to store nucleotide pairs in chromosomes to then be
        tested against a Human's chromosomes. Stores memory nucleotides as
        well.
        '''
        # run parent initialization
        Animal.__init__(self)

        self._max_chromosomes = 23
        # set all memory nucleotides to default value ""
        self._1 = ""
        self._2 = ""
        self._3 = ""
        self._4 = ""
        self._5 = ""
        self._6 = ""
        self._7 = ""
        self._8 = ""
        self._9 = ""

    # check if already saved
    def conflicting_memory(self, memorynucleotide, newvalue):
        '''(Query, int, str) -> bool
        A method that checks if a different value has already been saved in
        the given memory nucleotide. If True, then another value is already
        there. If False, the memory nucleotide is empty or has the same value.
        REQ: len(newvalue) == 1
        REQ: 0 <= memorynucleotide <= 9
        '''
        # check if saved nucleotide is "", if so return False
        # check if saved nucleotide is the same as newvale, if so return False
        # otherwise return True

        if(self.get_memory_nucleotide(memorynucleotide) == "" or
           self.get_memory_nucleotide(memorynucleotide) == newvalue):
            result = False
        else:
            result = True
        return result

    # Getters and Setters
    def set_memory_nucleotide(self, memorynucleotide, newvalue):
        '''(int, str) ->
        A method to set the given memory nucleotide to a new value
        REQ: len(newvalue) == 1
        REQ: 0 <= memorynucleotide <= 9
        '''
        # returns the correct memory nucleotide depending on the int input
        if(memorynucleotide == "1"):
            self._1 = newvalue
        elif(memorynucleotide == "2"):
            self._2 = newvalue
        elif(memorynucleotide == "3"):
            self._3 = newvalue
        elif(memorynucleotide == "4"):
            self._4 = newvalue
        elif(memorynucleotide == "5"):
            self._5 = newvalue
        elif(memorynucleotide == "6"):
            self._6 = newvalue
        elif(memorynucleotide == "7"):
            self._7 = newvalue
        elif(memorynucleotide == "8"):
            self._8 = newvalue
        elif(memorynucleotide == "9"):
            self._9 = newvalue

    def get_memory_nucleotide(self, memorynucleotide):
        '''(int) -> str
        A method to get the given memory nucleotide
        REQ: 0 <= memorynucleotide <= 9
        '''
        # returns the correct memory nucleotide depending on the int input
        if(memorynucleotide == "1"):
            result = self._1
        elif(memorynucleotide == "2"):
            result = self._2
        elif(memorynucleotide == "3"):
            result = self._3
        elif(memorynucleotide == "4"):
            result = self._4
        elif(memorynucleotide == "5"):
            result = self._5
        elif(memorynucleotide == "6"):
            result = self._6
        elif(memorynucleotide == "7"):
            result = self._7
        elif(memorynucleotide == "8"):
            result = self._8
        elif(memorynucleotide == "9"):
            result = self._9
        return result


class Binder(Animal):
    '''This class represents a Binder. It stores info on up to 23
    chromosomes such as where their nucleotide pairs are Left side maternal and
    right side maternal. Its purpose is to be used in the Female classe's
    procreate function. It also stores the gender of the child to be created
    by the Female.
    '''
    def __init__(self):
        ''' (Binder) -> NoneType
        Creates a binder, default 23 total chromosomes, default sex female
        '''
        # run parent class initialization
        Animal.__init__(self)

        # set default sex as Female
        self._sex = 'F'

        # set default max chromosomes to 23
        self._max_chromosomes = 22

    # Getters and Setters
    def get_sex(self):
        '''(Binder) -> str
        Returns sex of Binder in string form 'F' or 'M'
        '''
        return self._sex

    def set_sex(self, sex):
        '''(Binder, str) -> NoneType
        REQ: len(sex) == 1
        REQ: sex is either 'F' or 'M'
        '''
        self._sex = sex

    def set_by_pos(self, binderchromosome, Position, SideMaternal):
        '''(Binder, int, int, str) -> NoneType
        A method to change the Maternal side of a pair of nucleotide
        REQ: Chromosome >= 0
        REQ: Position >= 0
        REQ: SideMaternal is either 'LM' or 'RM'
        '''
        # find binderchromosome in dict: _chromosomes
        # use the BinderChromosome's built in method to change maternal side
        # if there is no binderchromosome at the given position create one

        if(binderchromosome in self._chromosomes):
            self._chromosomes[
                binderchromosome].set_by_pos(Position, SideMaternal)
        else:
            self._chromosomes[binderchromosome] = BinderChromosome()
            self._chromosomes[
                binderchromosome].set_by_pos(Position, SideMaternal)

    def get_by_pos(self, binderchromosome, Position):
        '''(Binder, int, int, str) -> str or None
        A method to change the Maternal side of a pair of nucleotide
        REQ: BinderChromosome >= 0
        REQ: Pair >= 0
        '''
        # find binderchromosome in dict: _chromosomes
        # Used BinderChromosome's built in method to get the Maternal Side
        # if nothing is found the string None will be returned
        try:
            return self._chromosomes[binderchromosome].get_by_pos(Position)
        except:
            return ""


class Human(Animal):
    ''' This class represents a human being that has chromosomes with
    nucleotide pairs in them. Its purpose is to store 23 chromosomes.
    Chromosomes are stored by index 0-22.
    '''
    def __init__(self, id_num):
        '''(Animal, int) -> NoneType
        Creates a dictionary to store Chromosomes
        '''
        # run parent class initialization
        Animal.__init__(self)

        # save ID number
        self._ID = id_num

        # set max chromosome
        self._max_chromosomes = 22

        # if no sex is given, humans by default will be male
        self._sex = 'F'

    def set_ID(self, identification):
        '''(Human, str) -> NoneType
        '''
        self._ID = identification

    def get_ID(self):
        '''(Human) -> str
        '''
        return self._ID

    def set_sex(self, sex):
        '''
        (Human) -> NoneType
        changes sex
        REQ: len(sex) == 1
        REQ: sex is either 'F' or 'M'
        '''
        self._sex = sex

    def get_sex(self):
        '''(Female) -> str
        returns sex of Female
        '''
        return self._sex

    # Test
    def test(self, query):
        '''(Query) -> bool
        Given the Query, compares only pairs within the Query to their
        corresponding pairs in the Animal. A test is False if its  Query pair
        does not match the corresponding Animal's pair of nucleotide. A Query
        pair is different from an Animal pair as it can contain memory
        nucleotides, represented by the numbers from 0-9. A single memory
        nucleotide can match any nucleotide but cannot match more than one type
        of nucleotide at the same time.
        If this were to happen, the Query would then be False. For example:
        "every 3 can be compared against a ‘C’ or against a ’T’, but we can’t
        have one 3 compared against a ‘C’ and another compared against a ‘T’".
        If the Query pair is compared against an empty Animal pair, the test
        is not False, unless if it is in the 23rd chromosome. If the Query Pair
        is compared with an empty Animal Pair in the sex chromosome the test
        returns False.
        '''
        # set up default value if all tests pass
        # set condition for while loop

        passed = True
        keeplooping = True

        # loop through every nucleotide in query
        # check if a query nucleotide contains a memory nucleotide every
        # time you compare nucleotides
        # check if the memory nucleotide is empty, if it is, save the new
        # value if not, check if the value conflicts with a previous
        # nucleotide saved using the query's built in conflicting_memory
        # method if it returns True then there was already a value saved
        # under this memory nucleotides name and its different then the new
        # one this should cause the test to end and return a False bool
        # if it returns False then, the nucleotide
        # has the same value as the new nucleotide

        # a query's nucleotide pair matches a humans nucleotide pair if
        # both their left characters match and both their right characters
        # match
        # if they don't match and the query's characters are not memory
        # nucleotides the test should stop and passed should become False

        continue_looping = True
        chromosome_set = set(query._chromosomes.keys())

        while continue_looping is True and len(chromosome_set) > 0:

            # pop a chromosome
            chromosome = chromosome_set.pop()

            pair_set = set(query._chromosomes[chromosome]
                           ._pairs.keys())

            while continue_looping is True and len(pair_set) > 0:
                # save the corresponding pair from the human

                left_normal = False
                right_normal = False

                # obtain chromosome num and position
                chromosome_num = chromosome
                position = pair_set.pop()

                c23 = False

                # set up bool if 23rd chromosome for later use
                if(chromosome == 22):
                    c23 = True

                # start by checking if the human's nucleotide pair is empty
                if(self.get_by_pos(chromosome_num, position) == ""):
                    # nothing should happen here, unless in chromosome 23
                    # if in chromosome 23 the test should fail

                    if(c23 is True and self.get_sex() == 'M'):
                        # stops loop return false
                        passed = False
                        keeplooping = False

                # if the previous if statement was not met
                # check if the if the query chromosome has all normal
                # nucleotides
                # if so, check if they match humans, if they do not, stop loop
                # return false

                # default value left normal and right normal is false

                else:
                    if((query._chromosomes[chromosome_num].
                       _pairs[position].get_left() == 'A' or
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_left() == 'T' or
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_left() == 'G' or
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_left() == 'C') and
                       keeplooping is True):
                        left_normal = True

                    if(query._chromosomes[chromosome_num].
                       _pairs[position].get_right() == 'A' or
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_right() == 'T' or
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_right() == 'G' or
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_right() == 'C' and
                       keeplooping is True):
                        right_normal = True

                    if(left_normal is True and right_normal is True and
                       keeplooping is True):
                        # check if query nucleotide pair matches human
                        # nucleotide
                        # pair if stop loop, return False
                        if(query.get_by_pos(chromosome_num, position) !=
                           self.get_by_pos(chromosome_num, position)):
                            passed = False
                            keeplooping = False

                    # check if memory nucleotides in query nucleotide pair's
                    # left character

                    if(query._chromosomes[chromosome_num].
                       _pairs[position].get_left() != 'A' and
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_left() != 'T' and
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_left() != 'G' and
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_left() != 'C'and
                       keeplooping is True):
                        # if this code runs it means there is a memory
                        # nucleotide
                        # in the left character of the query's nucleotide pair

                        # save humans left character as a memory nucleotide
                        query_left_char = query.get_chromosome(chromosome_num)
                        query_left_char = query_left_char._pairs[position]
                        query_left_char = query_left_char.get_left()

                        human_left_char = self.get_chromosome(chromosome_num)
                        human_left_char = human_left_char._pairs[position]
                        human_left_char = human_left_char.get_left()

                        # check if there is a memory nucleotide saved at this
                        # number, if not, save it
                        # if there is one, check if it is the same value as
                        # left character in human, if not stop the loop
                        # the test has failed

                        if(query.get_memory_nucleotide(query_left_char) == ""):
                            # this code sets the memory nucleotide
                            # to the left character of human's nucleotide pair
                            query.set_memory_nucleotide(query_left_char,
                                                        human_left_char)

                        elif(query.conflicting_memory(query_left_char,
                                                      human_left_char) is
                             True):
                            # if this code runs, there are multiple
                            # characters saved to a single memory nucleotide
                            # the loop should stop and the test is failed

                            passed = False
                            keeplooping = False

                        # if neither if statement holds true, it means humans
                        # left character is the same as the memory nucleotide

                    # check if memory nucleotides in query nucleotide pair's
                    # right character

                    if(query._chromosomes[chromosome_num].
                       _pairs[position].get_right() != 'A' and
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_right() != 'T' and
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_right() != 'G' and
                       query._chromosomes[chromosome_num].
                       _pairs[position].get_right() != 'C' and
                       keeplooping is True):
                        # if this code runs it means there is a memory
                        # nucleotide
                        # in the right character of the query's nucleotide pair

                        # save humans right character as a memory nucleotide
                        query_right_char = query.get_chromosome(chromosome_num)
                        query_right_char = query_right_char._pairs[position]
                        query_right_char = query_right_char.get_right()

                        human_right_char = self.get_chromosome(chromosome_num)
                        human_right_char = human_right_char._pairs[position]
                        human_right_char = human_right_char.get_right()
                        # check if there is a memory nucleotide saved at this
                        # number, if not, save it
                        # if there is one, check if it is the same value as
                        # right character in human, if not stop the loop
                        # the test has failed

                        if(query.get_memory_nucleotide(query_right_char) ==
                           ""):
                            # this code sets the memory nucleotide
                            # to the right character of human's nucleotide pair
                            query.set_memory_nucleotide(query_right_char,
                                                        human_right_char)

                        elif(query.conflicting_memory(query_right_char,
                                                      human_right_char) is
                             True):
                            # if this code runs, there are multiple
                            # characters saved to a single memory nucleotide
                            # the loop should stop and the test is failed
                            passed = False
                            keeplooping = False
                        # if neither if statement holds true, it means humans
                        # right character is the same as the memory nucleotide
        return passed

# HUMAN CHILD CLASSES


class Male(Human):
    '''
    A child class of Human that represents the Male sex. Its purpose is to be
    used during the Female procreate method. It has all the functionality of a
    Human.
    '''
    def __init__(self, id_num):
        '''(Male, int) -> NoneType
        Runs the Animal init function and sets sex to Male
        '''
        Human.__init__(self, id_num)

        # set sex to 'M'
        self.set_sex('M')

    # Getters and Setters

    def set_sex(self, sex):
        '''
        (Male) -> NoneType
        changes sex
        REQ: len(sex) == 1
        REQ: sex is either 'F' or 'M'
        '''
        self._sex = sex

    def get_sex(self):
        '''(Male) -> str
        returns sex of Female
        '''
        return self._sex


class Female(Human):
    '''
    A child class of Human that represents the Female sex. It can procreate if
    given a Binder and Male. It has all the functionality of a Human.
    '''
    def __init__(self, id_num):
        '''(Female, int) -> NoneType
        Runs the Animal init function and sets sex to Female
        '''
        Human.__init__(self, id_num)

        # set sex to 'F'
        self.set_sex('F')

    def left_maternal(self, male, chromosome_num, position):
        '''(Female, Male, int, int) -> str
        A method that obtains the left nucleotide of a pair from a femal
        and the right nucleotide of a male and returns a nucleotide
        pair of both of them combined. If one of the pairs does not exist
        the function will return "".
        '''
        # obtain left character of female at chromosome num and position

        # obtain right charcter of male at chromosome num and position

        # if either character is "", method will return ""

        left_char = self.get_by_pos(chromosome_num, position)
        left_char = left_char[0]

        right_char = male.get_by_pos(chromosome_num, position)
        right_char = right_char[1]

        if (right_char == "" or left_char == ""):
            result = ""
        else:
            result = left_char + right_char
        return result

    def right_maternal(self, male, chromosome_num, position):
        '''(Female, Male, int, int) -> str
        A method that obtains the right nucleotide of a pair from a female
        and the left nucleotide of a male and returns a nucleotide
        pair of both of them combined. If one of the pairs does not exist
        the function will return ""
        '''
        # obtain right character of female at chromosome num and position

        # obtain left charcter of male at chromosome num and position

        # if either character is "", method will return ""

        left_char = male.get_by_pos(chromosome_num, position)
        left_char = left_char[0]

        right_char = self.get_by_pos(chromosome_num, position)
        right_char = right_char[1]

        if (right_char == "" or left_char == ""):
            result = ""
        else:
            result = left_char + right_char
        return result

    # Procreate

    def procreate(self, male, binder):
        '''(Female, Male, Binder) -> Human
        Creates a new human with the sex of the Binder. Its nucleotides
        are made up of the Female and Male's. Which nucleotides are used is
        decided by the Binder. The Binder has saved where the nucleotides are
        Right or left maternal. Right maternal means the right nucleotide in
        the pair comes from the Female and the left nucleotide comes from the
        male. Vice versa for left maternal. If the Binder does not specify
        if a pair is left or right maternal it will default to right maternal.
        '''
        # create new human
        # set sex to sex of binder
        # set id to be combination of mother and father's ids
        ID = self.get_ID() + male.get_ID()

        # set childs gender based on Binder
        # create child
        if(binder.get_sex() == 'M'):
            child = Male(ID)
        else:
            child = Female(ID)

        # loop through all binder chromosome pairs
        # check if pair is left maternal
        # if a pair's maternal side is not within the Binder
        # it will not appear in the child class

        # if the binder pair is
        # run either the left_maternal or right_maternal
        # built in method of female
        # set the binder pair to checked
        # if the left_maternal or right_maternal methods return "" then one
        # of the parent's pairs are empty, in this case do not set
        # this child's pair to anything

        # binder chromosomes and binder pairs

        # create a set of all Binder chromosomes
        chromosome_set = set(binder._chromosomes.keys())

        while len(chromosome_set) > 0:

            # pop a chromosome and go through all of its pairs
            # repeat this until all chromosomes have been fully searched
            chromosome = chromosome_set.pop()

            pair_set = set(binder._chromosomes[chromosome]._pairs.keys())
            # remove pairs from the set until all pairs have been
            # checked

            while len(pair_set) > 0:

                # get an individual pair
                position = pair_set.pop()
                pair = binder._chromosomes[chromosome]._pairs[position]

                # find maternal side

                ms = binder.get_by_pos(chromosome, position)

                # obtain childs nucleotide
                # use proper method based on maternal side

                if(ms == 'LM'):

                    # create the nucleotide pair of the child
                    newpair = self.left_maternal(male,
                                                 chromosome,
                                                 position)

                    # if the newpair is "" do nothing
                    # otherwise set by position in child

                    if(newpair != ""):
                        child.set_by_pos(chromosome,
                                         position,
                                         newpair)

                elif(ms == 'RM'):
                    # create the nucleotide pair of the child
                    newpair = self.right_maternal(male,
                                                  chromosome,
                                                  position)

                    # if the newpair is "" do nothing
                    # otherwise set by position in child
                    if(newpair != ""):
                        child.set_by_pos(chromosome,
                                         position,
                                         newpair)

        return child

    # Getters and Setters

    def set_sex(self, sex):
        '''
        (Female) -> NoneType
        changes sex
        REQ: len(sex) == 1
        REQ: sex is either 'F' or 'M'
        '''
        self._sex = sex

    def get_sex(self):
        '''(Female) -> str
        returns sex of Female
        '''
        return self._sex
# CHROMOSOME


class Chromosome():
    ''' This class represents a single chromosome within a living animal, its
    purpose is to store pairs of nucleotides at certain positions in mutable
    lists.
    '''
    def __init__(self):
        '''(Chromosome, int) -> NoneType
        Creates a dictionary, that holds 2 character long strings that
        represent nucleotide pairs.
        '''
        # create empty dictionary to store Pair classes
        self._pairs = {}

    # Getters and Setters

    def set_by_pos(self, position, NewPair):
        '''(Chromosome, int, str) -> NoneType
        sets the nucleotide at the given position to the given string.
        REQ: len(NewPair) == 2
        REQ: pair can only contain the letters 'ATGC'
        REQ: position >= 0
        '''
        # if no pair is present, create a new one
        # if a pair is present set it to the NewPair str using
        # the pair's methods

        if(position in self._pairs):
            self._pairs[position].set_pair(NewPair)
        else:
            self._pairs[position] = Pair(NewPair)

    def get_pairs(self):
        '''(Chromosome) -> dict of {int:Pair}
        A method to return the dictionary of a chromosome's Pairs
        '''
        return self._pairs

    def get_by_pos(self, position):
        '''(Chromosome, int) -> str
        Returns the proper nucleotide from the saved pairs in the chromosome
        based off the position given. If no pair is there, the method will
        return an empty string.
        REQ: position >= 0
        '''
        # return the value found in the dict: pairs in the key: position
        # convert index 0 and 1 of list into str and return
        # if no pair is found return None

        try:
            return self._pairs[position]
        except:
            return ""

    def set_empty_pair(self, position, none):
        '''(Chromosome, NoneType) -> NoneType
        A function to set an empty pair, when a marker is created for the
        location of a pair that doesn't exist
        '''
        self._pairs[position] = ""


# Child classes of Chromosome


class BinderChromosome(Chromosome):
    ''' A chromosome created to be stored in the class Binder, to store
    BinderPairs that store data on which pairs of nucleotides are right
    maternal and which are left maternal
    '''

    def __init__(self):
        '''(BinderChromosome, int) -> NoneType
        Creates a dictionary, that holds 2 character long strings that
        represent nucleotide pairs.
        '''
        # has the same initialization as a normal Chromosome
        Chromosome.__init__(self)

    # Getters and Setters

    def set_by_pos(self, position, MaternalDirection):
        '''(BinderChromosome, int, str) -> NoneType
        Given a position of a pair of nucleotide, changes the pair's
        Maternal Side.
        REQ: position >= 0
        REQ: MaternalDirection is either "RM" or "LM"
        '''
        # if a BinderPair exists already in this position, change its
        # maternal direction
        # if a BinderPair in this position does not yet exist create one
        # with the given maternal direction

        if(position in self._pairs):
            self._pairs[position].set_ms(MaternalDirection)
        else:
            self._pairs[position] = BinderPair(MaternalDirection)

    def get_by_pos(self, position):
        '''(BinderChromosome, int) -> str
        Given the position of the nucleotide pair in the BinderChromosome
        returns a string representation of wether or not the pair is
        Right Maternal or Left Maternal in the form of either "LM" or "RM"
        '''
        # if a BinderPair exists at this position return a string
        # representation of it
        # if no BinderPari exists at this position return None

        try:
            return str(self._pairs[position])
        except:
            return ""


# Nucleotide Pairs and Nucleotide storage

class Pair():
    ''' A class that represents nucleotide pairs. Its purpose is to store and
    return string representations of nucleotide pairs'''

    def __init__(self, pair):
        '''(Pair, str) -> NoneType)
        Given the left and right nucleotides, stores them in a nucleotide pair
        REQ: len(LeftCharacter) == 1
        REQ: len(RightCharacter) == 1
        '''
        self._L = pair[0]
        self._R = pair[1]
        self._checked = False

    def __str__(self):
        ''' (Pair) -> str
        Returns a string representation of a Pair
        '''
        result = self._L + self._R
        return result

    def set_checked(self, bool):
        ''' (Pair, bool) -> NoneType
        A function to set a pair's checked bool to True
        '''
        self._checked = True

    def get_checked(self):
        '''(Pair) -> bool
        '''
        return self._checked

    def set_pair(self, newpair):
        '''(Pair, str) -> NoneType
        A method to set both the left and right characters of a nucleotide pair
        REQ: len(newpair) == 2
        '''
        self._L = newpair[0]
        self._R = newpair[1]

    def set_left(self, newchar):
        '''(Pair, str) -> NoneType
        A method to set the left character of a nucleotide pair
        REQ: len(newchar) == 1
        '''
        self._L = newchar

    def set_right(self, newchar):
        '''(Pair, str) -> NoneType
        A method to set both the left and right characters of a nucleotide pair
        REQ: len(newchar) == 1
        '''
        self._R = newchar

    def get_right(self):
        ''' A method to obtain the right character of a pair
        '''
        result = str(self._R)
        return result

    def get_left(self):
        ''' (BinderPair) -> str
        A method to obtain the right character of a pair
        '''
        result = str(self._L)
        return result

# Binder and Maternal Side Storage


class BinderPair():
    ''' A class created to store information of wether a nucleotide pair
    at a certain location is left maternal or right maternal
    '''

    def __init__(self, MaternalSide):
        '''(BinderPair, str) -> NoneType
        Recieves a string representation of the maternal side the pair is
        and stores it.
        REQ: MaternalSide is either "LM" or "RM"
        '''
        self._ms = MaternalSide

    def __str__(self):
        '''(BinderPair) -> str
        A method that returns a string representation of a Binder Pair
        '''
        return self._ms

    # Getters and Setters

    def set_ms(self, MaternalSide):
        ''' (BinderPair, str) -> NoneType
        A method to set the maternal side of a binder pair
        REQ: MaternalSide is either "LM" or "RM"
        '''
        self._ms = MaternalSide

    def get_ms(self):
        '''(BinderPair) -> str
        A method to get the maternal side of a binder pair
        '''
        return self._ms

# Marker


class Marker():
    ''' A class that's purpose is to store chromosome numbers and nucleotide
    positions.
    '''
    def __init__(self, ChromosomeNum, position):
        '''(Marker, int, int) -> NoneType
        creates a new marker with the given chromosome number and position
        of nucleotide pair
        '''
        self._chromosome_num = ChromosomeNum
        self._position = position

    def get_chromosome_num(self):
        '''(Marker) -> int
        '''
        return self._chromosome_num

    def get_position(self):
        '''(Marker) -> int
        '''
        return self._position

    def set_position(self, newpos):
        '''(Marker, int) -> NoneType
        '''
        self._position = newpos

    def set_chromosome_num(self, newnum):
        '''(Marker, int) -> NoneType
        '''
        self._position = newnum


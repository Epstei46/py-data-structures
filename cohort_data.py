"""Functions to parse a file containing student data."""
# Exercise located at https://ed.devmountain.com/materials/data-bp-1/exercises/py-data-structures/

def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()
    
    data = open(filename)
    
    for line in data:
      # below if statement skips lines for Instructors and Ghosts, which have no house.
      if line[-2] != 'I' and line[-2] != 'G':
        line = line.rstrip()
        line_list = line.split('|')
        house = line_list[2]
        if house not in houses:
          houses.add(house)
    data.close()

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []
    
    data = open(filename)
    # data = open('cohort_data.txt')
    
    for line in data:
      first, last, _, _, cohort_name = line.rstrip().split('|')
      # print(f"{first} {last} is in {cohort_name}") # check to make sure above line is working as intended
      if cohort == 'All' and cohort_name != 'I' and cohort_name != 'G':
        students.append(f"{first} {last}")
      elif cohort_name == cohort and cohort_name != 'I' and cohort_name != 'G':
        students.append(f"{first} {last}")
    # print(sorted(students))
    
    data.close()

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    data = open(filename)
    # data = open('cohort_data.txt')
    
    for line in data:
      first, last, house, _, cohort = line.rstrip().split('|')
      # print(f"{first} {last} is in {cohort_name}")
      if cohort == 'I':
        instructors.append(f'{first} {last}')
      elif cohort == 'G':
        ghosts.append(f'{first} {last}')
      elif house == 'Slytherin':
        slytherin.append(f'{first} {last}')
      elif house == 'Ravenclaw':
        ravenclaw.append(f'{first} {last}')
      elif house == 'Hufflepuff':
        hufflepuff.append(f'{first} {last}')
      elif house == 'Gryffindor':
        gryffindor.append(f'{first} {last}')
      elif house == "Dumbledore's Army":
        dumbledores_army.append(f'{first} {last}')
    
    data.close()

    return [sorted(dumbledores_army), sorted(gryffindor), sorted(hufflepuff), sorted(ravenclaw), sorted(slytherin), sorted(ghosts), sorted(instructors)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    data = open(filename)
    # data = open('cohort_data.txt')
    
    for line in data:
      first, last, house, instructor, cohort = line.rstrip().split('|')
      # print(f"{first} {last} is in {cohort_name}")
      all_data.append((f'{first} {last}', house, instructor, cohort))
    
    data.close()

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Someone else')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    data = all_data(filename)
    for i in range(len(data)):
      # print(data[i][-1])
      if data[i][0] == name:
        return data[i][-1]
      
    # for full_name, _, _, cohort_name in all_data(filename):
    #     if full_name == name:
    #         return cohort_name


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    once = set()
    dupe = set()
    for name, _, _, cohort in all_data(filename):
      last_name = name.split()[-1]
      if last_name not in once:
        once.add(last_name)
      else:
        dupe.add(last_name)
      # if last_name in once:
      #   dupe.add(last_name)
      # once.add(last_name)
        
    return dupe


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code
    
    housemates = set()
    student_cohort = get_cohort_for(filename, name)
    
    for full_name, house, _, _ in all_data(filename):
        if full_name == name:
            student_house = house
    
    for full_name, house, _, cohort in all_data(filename):
      if student_cohort == cohort and student_house == house and full_name != name:
        housemates.add(full_name)
    
    # target_person = None
    # for person in all_data(filename):
    #     full_name, house, advisor, cohort_name = person
    #     if full_name == name:
    #         target_person = person
    #         break
    # if target_person:
    #     target_name, target_house, _, target_cohort = target_person
    #     for full_name, house, _, cohort_name in all_data(filename):
    #         if ((house, cohort_name) == (target_house, target_cohort) and
    #                 full_name != name):
    #             housemates.add(full_name)
    
    return housemates
      


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')

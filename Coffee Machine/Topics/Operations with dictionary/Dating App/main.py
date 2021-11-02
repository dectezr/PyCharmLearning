def select_dates(potential_dates):
    persons = ''
    for person in potential_dates:
        if person['age'] > 30 and 'art' in person['hobbies'] and person['city'] == 'Berlin':
            persons += person['name'] + ', '
    return persons.rstrip(', ')

people = {
    1: {
        'Name': 'John',
        'Age': '27',
        'Sex': 'Male',
        'other_detail': {
            "Mobile_Number": "5152823685",
            "Alternate_Number": "1234567891",
            "current_address": None,
            "permanentAddress": "CDEF"
        }
    },
    2: {
        'Name': 'Marie',
        'Age': '22',
        'Sex': None,
        'other_detail': {
            "Mobile_Number": "5152823685",
            "Alternate_Number": None,
            "current_address": "ABCDE",
            "permanentAddress": "CDEF"
        }
    },
    3: {
        'Name': 'Emily',
        'Age': '30',
        'Sex': 'Female',
        'other_detail': {
            "Mobile_Number": "5152823685",
            "Alternate_Number": "1234567891",
            "current_address": None,
            "permanentAddress": "CDEF"
        }
    },
    4: {
        'Name': 'Akash',
        'Age': '24',
        'Sex': 'Male',
        'other_detail': {
            "Mobile_Number": "5152823685",
            "Alternate_Number": None,
            "current_address": "ABCDE",
            "permanentAddress": "CDEF"
        }
    },
    5: {
        'Name': 'Alok',
        'Age': '44',
        'Sex': None,
        'other_detail': {
            "Mobile_Number": "5152823685",
            "Alternate_Number": "1234567891",
            "current_address": None,
            "permanentAddress": "CDEF"
        }
    },
    6: {
        'Name': 'Pradeep',
        'Age': '55',
        'Sex': 'Male',
        'other_detail': {
            "Mobile_Number": "5152823685",
            "Alternate_Number": None,
            "current_address": "ABCDE",
            "permanentAddress": "CDEF"
        }
    },
    7: {
        'Name': 'Rahul',
        'Age': '85',
        'Sex': None,
        'other_detail': {
            "Mobile_Number": "5152823685",
            "Alternate_Number": "1234567891",
            "current_address": None,
            "permanentAddress": "CDEF"
        }
    },
    8: {
        'Name': 'Narendra',
        'Age': '23',
        'Sex': 'Male',
        'other_detail': {
            "Mobile_Number": "5152823685",
            "Alternate_Number": None,
            "current_address": "ABCDE",
            "permanentAddress": "CDEF"
        }
    },
    9: {
        'Name': 'Sharukh',
        'Age': '50',
        'Sex': None,
        'other_detail': {
            "Mobile_Number": "5152823685",
            "Alternate_Number": "1234567891",
            "current_address": "ABCDE",
            "permanentAddress": "CDEF"
        }
    }
}

for people_id, people_data in people.items():
    print("\nPerson ID: ", people_id)

    for keys in list(people_data.keys()):
        if people_data[keys] == None:
            people_data.pop(keys)
    for keyss in list(people_data['other_detail'].keys()):
        if people_data['other_detail'][keyss] == None:
            people_data['other_detail'].pop(keyss)

    for keys in list(people_data.keys()):
        # print(str(keys) + " : " + str(people_data[keys]))
        if keys != 'other_detail':
            print(str(keys) + " : " + str(people_data[keys]))
        else:
            for keyss in list(people_data['other_detail'].keys()):
                print(str(keyss) + " : " + str(people_data['other_detail'][keyss]))

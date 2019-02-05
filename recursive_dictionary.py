people = {
    1: {
        'Name': 'John',
        'Age': '27',
        'Sex': 'Male',
        'other_detail': {
                'Mobile_Number': '5152823685',
                'Alternate_Number': '1234567891',
                'current_address': None,
                'permanentAddress': 'CDEF'
        }
    },
    2: {
        'Name': 'Marie',
        'Age': '22',
        'Sex': None,
        'other_detail': {
                'Mobile_Number': '5152823685',
                'Alternate_Number': None,
                'current_address': 'ABCDE',
                'permanentAddress': 'CDEF'
        }
    },
    3: {
        'Name': 'Emily',
        'Age': '30',
        'Sex': 'Female',
        'other_detail': {
                'Mobile_Number': '5152823685',
                'Alternate_Number': '1234567891',
                'current_address': None,
                'permanentAddress': 'CDEF'
        }
    },
    4: {
        'Name': 'Akash',
        'Age': '24',
        'Sex': 'Male',
        'other_detail': {
                'Mobile_Number': '5152823685',
                'Alternate_Number': None,
                'current_address': 'ABCDE',
                'permanentAddress': 'CDEF'
        }
    },
    5: {
        'Name': 'Alok',
        'Age': '44',
        'Sex': None,
        'other_detail': {
                'Mobile_Number': '5152823685',
                'Alternate_Number': '1234567891',
                'current_address': None,
                'permanentAddress': 'CDEF'
        }
    },
    6: {
        'Name': 'Pradeep',
        'Age': '55',
        'Sex': 'Male',
        'other_detail': {
                'Mobile_Number': None,
                'Alternate_Number': None,
                'current_address': None,
                'permanentAddress': None
        }
    },
    7: {
        'Name': 'Rahul',
        'Age': '85',
        'Sex': None,
        'other_detail': {
                'Mobile_Number': '5152823685',
                'Alternate_Number': '1234567891',
                'current_address': None,
                'permanentAddress': 'CDEF'
        }
    },
    8: {
        'Name': 'Narendra',
        'Age': '23',
        'Sex': 'Male',
        'other_detail': {
                'Mobile_Number': '5152823685',
                'Alternate_Number': None,
                'current_address': 'ABCDE',
                'permanentAddress': 'CDEF'
        }
    },
    9: {
        'Name': 'Sharukh',
        'Age': '50',
        'Sex': None,
        'other_detail': {
                'Mobile_Number': None,
                'Alternate_Number': None,
                'current_address': None,
                'permanentAddress': None
        }
    }
}

def recursive_func(mydict):
    for key, value in list(mydict.items()):
        if isinstance(value, dict):
            recursive_func(value)
            print("-------------------------------------")
        else:
            if (value == None):
                mydict.pop(key)
            else:
                print("{} - {}".format(key, value))
    
    return mydict
                

if __name__ == "__main__":
    new_dict = recursive_func(people)
    print("")
    print("")
    print(new_dict)

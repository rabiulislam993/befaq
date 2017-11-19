# utility functions for student app

def grade_calculator(result_obj):
    '''calculate grade for given result object'''

    average_number = result_obj.average_num

    if average_number < 33:
        return 'rasib'
    elif average_number < 50:
        return 'makbul'
    elif average_number < 65:
        return 'jaiyed'
    elif average_number < 80:
        return 'jaiyed_jiddan'
    elif average_number <= 100:
        return 'mumtaz'

    return ''
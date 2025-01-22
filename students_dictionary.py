

def mean_per_student(dictionaries: list[dict[str, object]]) -> None:
    for dictionary in dictionaries:
        total_grades = 0
        for grade in dictionary['grades']: # type: ignore
            total_grades += int(grade) # type: ignore
        
        average = total_grades / len(dictionary['grades'])  # type: ignore
        print(f"{dictionary['first_name']}, {dictionary['last_name']}, {dictionary['school_class']} --- Average: {average}")


test: list[dict[str, object]] = [{
        'first_name': 'John',
        'last_name': 'Doe',
        'school_class': '4A',
        'grades': [4, 8, 9, 4]
        },
        {'first_name': 'Juan',
          'last_name': 'Tacos',
          'school_class': '2C',
          'grades': [4, 8, 9, 10]
        },
    ]

def main():
    mean_per_student(test)
if __name__ == '__main__':
    main()
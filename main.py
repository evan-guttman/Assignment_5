# Resources used:
    # ChatGPT was used to help explain the assignment requirements and check if fulfilled.
    # Some VS Code auto fill was also used to provide guidance on Python syntax and structure.
    # Class notes and in-class assignments were also used to help with the assignment.

# Open input file and check for issues
def check_file(input_filename):
    # Prime loop
    input_file = None

    # Keep trying until a file opens
    while input_file is None:
        # Read file 
        try:
            input_file = open(input_filename, 'r')
        # File not found
        except FileNotFoundError:
            print('File not found. Please try again.')
            input_filename = input('Please enter the name of the input data file: ')

    # Give main the open file.
    return input_file

# Check for curve score issues
def check_curve(input_curve):
    # Get a Y or N
    while input_curve != 'Y' and input_curve != 'N':
        print('Please enter Y or N.')
        input_curve = input('Would you like to curve the grades? (Y/N) ')
            
    # Prime loop for curve check
    curve_score = None

    if input_curve == 'Y':
        while curve_score is None:
            # Invalid curve
            try:
                curve_score = float(input("Please enter the score that should map to a '100%' grade: "))
                # negative error
                if curve_score <= 0:
                    print('Please enter a number greater than zero.')
                    curve_score = None
            # Non-number error
            except ValueError:
                    print('Please enter a valid number.')
    
    # Give back to Main
    return input_curve, curve_score

# Check for bad data + explain/fix
def bad_data(category, name, score):
    # Category check: Grad or Undergrad.
    if category != 'GRAD' and category != 'UNDERGRAD':
        print('Unknown student category detected (' + category + ').')
        return True

    # Name check
    if name == '':
        print('Student name is missing.')
        return True

    # Number check: valid number
    try:
        number = float(score)
    except ValueError:
        print('Invalid numerical grade detected (' + score + ').')
        return True

    # Number check: 0 - 100
    if number < 0 or number > 100:
        print('Grade must be between 0 and 100.')
        return True

    # All checks passed.
    return False

# Proceces a students data 
def process_data(input_file):
    category = input_file.readline().rstrip('\n')
    name = input_file.readline().rstrip('\n')
    score = input_file.readline().rstrip('\n')

    # End and return to main
    return category, name, score

# Convert to curved score
def curve(score, curve_score):
    # Adjust to curve
    new_score = score / curve_score * 100
    # Return score to main
    return new_score

# Determine grade
def determine_grade(category, score):
    # Grad
    if category == 'GRAD':
        if score >= 95:
            letter = 'H'
        elif score >= 80:
            letter = 'P'
        elif score >= 70:
            letter = 'L'
        else:
            letter = 'F'

    # Undergrad
    else:
        if score >= 90:
            letter = 'A'
        elif score >= 80:
            letter = 'B'
        elif score >= 70:
            letter = 'C'
        elif score >= 60:
            letter = 'D'
        else:
            letter = 'F'

    # Send grade main
    return letter

# Main function
def main():
    # Ask for input of filename + save
    input_filename = input('Please enter the name of the input data file: ')
    # Call check_file func
    input_file = check_file(input_filename)

    # Ask for output filename + save
    output_filename = input('Please enter the name of the output data file: ')

    # Ask for curve or not (Y/N)
    input_curve = input('Would you like to curve the grades? (Y/N): ')
    # Filter and fix erros (call check_curve func)
    input_curve, curve_score = check_curve(input_curve)

    # Create the output file.
    output_file = open(output_filename, 'w')
    
    # Process data (call process_data func)
    category, name, score = process_data(input_file)
    # Loop through all students
    # Prime loop
    success = True
    while category != '':
        # Check for bad data (call bad_data func)
        if bad_data(category, name, score):
            print('Error occurred while determining letter grade. Aborting.')
            success = False
            break
        # Check/change to valid number
        score = float(score)
        # Curve scores (if needed) (call curve func)
        if input_curve == 'Y':
            score = curve(score, curve_score)
        # Determin Grades (Call Grade func)
        letter = determine_grade(category, score)
        # write name and grade in output file
        output_file.write(name + '\n')
        output_file.write(letter + '\n')
        # Finish loop
        category, name, score = process_data(input_file)

    # Close files
    input_file.close()
    output_file.close()

    # Display final status
    if success:
        print('All data was successfully processed and saved to the requested output file.')
    else:
        print('Please fix the input data before retrying.')

# Run Program
main()
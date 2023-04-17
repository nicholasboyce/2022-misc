def remove_numbers(filename, result_file):
    """
    Receives filename as a parameter. Opens said file and iterates over each
    line. Identifies any line where it begins with "#." Removes that, and 
    leaves text without any "#1."
    """
    the_file = open(filename)
    lines = the_file.readlines()
    final_file = open(result_file, 'w')
    for line in lines:
        line = line[4:]
        final_file.write(line)
    the_file.close()
    final_file.close()
    
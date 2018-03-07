#The purpose of this python program is to scan for code files
#based on the inputs provided by the user
# 1. Open the file specified by the user
# 2. Read the contents on the specified line number

#This dict will contain line number, line pairs
open_braces_dict = {}

def get_code_from_application(application_file_path, line_number):
    previousline = "";
    try:
        with open(application_file_path) as codeFile:
            for line_index,line in enumerate(codeFile):
                if(line_index == line_number -1 ): # the line index will be one below the line number
                    open_braces_dict[line_index+1] = line.strip()
                    return open_braces_dict
                else:
                    if "{" in line or "}" in line:
                        track_unclosed_open_flower_brace(line_index, line.strip(), previousline.strip())
                previousline = line
            track_hierarchy_lines()
    except IOError:
        print("Did not find the application file in the specified path. Please retry")
        return -1

#The purpose of this function is to find out all the unclosed { braces before the matching line is found in the code file
def track_unclosed_open_flower_brace(line_index, currentline, previousline):
    if "{" in currentline:
        open_braces_dict[line_index+1] = track_hierarchy_lines(currentline, previousline)
    elif "}" in currentline:
        ## remove the last added line
        highest_number = 0
        for key in open_braces_dict:
            if key > highest_number:
                highest_number = key
        if highest_number > 0:
            del open_braces_dict[highest_number]

#The purpose of this function is to find out the lines in the hierarchy of the concerned statement
#Note: The hierarchy statement may have the { brace in the same line or in separate lines. We will have to factor that
def track_hierarchy_lines(current_line, previous_line):
    if(len(current_line) == 1) :  #this means that the current line has only {. So need to return the previous line
        return previous_line
    else:
        return current_line.replace("{", "").strip()
        

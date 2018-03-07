# The purpose of this program is to collect the input details from the user
import os
from global_reference import training_features_dict, line_type_dict, user_input_dict

def get_training_features():
    print("Select a feature to train the code learner from one of the options below")
    for key in training_features_dict:
        print(str(key) + ". " + training_features_dict.get(key))
    user_selected_feature = str(raw_input("Please select from one of the options above "))
    if(user_selected_feature != "1"):
        print("Sorry. You selected an option that is not supported currently")
        exit()
    else:
        return int(user_selected_feature)

def get_application_root_directory():
    application_path_str = raw_input("Please enter the root directory of the application")
    application_path = os.path.abspath(application_path_str)
    return application_path

def get_application_file_name():
    file_path_str = raw_input("Please enter the file (absolute file path) where the" \
                                + " feature can be found ")
    file_path = os.path.abspath(file_path_str)
    return file_path

def get_line_number_having_pattern():
    line_num = int(raw_input("Please enter the line number that has the pattern "))
    if line_num < 1:
        print("Sorry. Incorrect line number. Please retry")
        get_line_number_having_pattern()
    else:
        return line_num

def get_type_of_line():
    print("What does this line number signify? Please select one of the below options")
    for key in line_type_dict:
        print(str(key) + ". " + line_type_dict.get(key))
    line_type_option = int(raw_input())
    if line_type_option == 1 or line_type_option == 2:
        return line_type_option
    else:
        print("Sorry. Incorrect option provided. Please retry")
        get_type_of_line()

def get_user_input():

    user_input_dict["feature"]= get_training_features()

    #user_input_dict["application_path"] = get_application_root_directory()

    user_input_dict["application_file"] = get_application_file_name()

    user_input_dict["line_number"] = get_line_number_having_pattern()

    #user_input_dict["line_type"] = get_type_of_line()

    print("Thanks for training me in {} pattern.".format(training_features_dict.get(user_input_dict.get("feature"))))
    return user_input_dict

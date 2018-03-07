#This python program serves as the entrypoint into the code learner application
from user_interaction import get_user_input
from global_reference import training_features_dict
from scancodefile import get_code_from_application
from javaparser import get_list_of_words_from_statement, parse_java_code_line
#import sys
# sys.path.append('javalang')
# import javalang

# Step 1. Get the required input from the user
user_input_dict = get_user_input()

# Step 2. Extract the line from the application based on user inputs
code_extracted = get_code_from_application(user_input_dict.get("application_file"), user_input_dict.get("line_number"))
if code_extracted == -1:
    exit()


#Step 3.
#javalang experimentation
# print(code_extracted.strip())
# tokens = javalang.tokenizer.tokenize(code_extracted.strip())
# token_list = list(tokens)
# print(token_list)
# for token in token_list:
#     print(type(token))
# parser = javalang.parser.Parser(javalang.tokenizer.tokenize('String url = "hi"'))
# print(parser.parse_expression())
#end of experimentation

#Step 3
#Make sense of all the code extracted. Loop through each of the lines code_extracted and tokenize them
code_dict = {}
for key in code_extracted:
    code_dict[key] = get_list_of_words_from_statement(code_extracted.get(key))

#Step 4 - Order the code lines. Ignore line number from now on
code_lines_list = [code_dict.get(key) for key in sorted(code_dict.iterkeys())]

#Step 4 - Run the extracted dictionary on the java parser to identify key java elements
user_input_feature = training_features_dict.get(user_input_dict.get('feature'))
user_provided_line = code_extracted.get(user_input_dict.get("line_number"))
user_provided_line_info = {}
metadata_info= []
print("******Beginning to parse for information******")
for line in code_lines_list:
    parsed_line_dict = parse_java_code_line(line)
    
    if (parsed_line_dict.get('statement') == user_provided_line):
        user_provided_line_info = parsed_line_dict
    else:
        metadata_info.append(parsed_line_dict)

print("Trained Feature = {}".format(user_input_feature))
print
print("User Provided Line = {}".format(user_provided_line))
print
print("Line Info = {}".format(user_provided_line_info))
print
print("Metadata Info = {}".format(metadata_info))
print

#The purpose of this python program is to expose different functions
# that can parse java code statements.
from global_reference import java_identifiers_access_modifier_list, java_identifiers_data_types_list, \
java_identifiers_inheritance_keywords_list,java_identifiers_exception_keywords_list, java_identifiers_user_data_type_identifier_list, \
line_type_dict, java_identifiers_return_types_list, java_identifiers_assignment_operators_list, \
java_identifiers_arithmentic_operators_list, java_identifiers_comparison_operators_list, java_identifiers_other_keywords_list


def get_list_of_words_from_statement(javastatement):
    return split_line_by_delimiter(javastatement," ")


def split_line_by_delimiter(line, delimiter_char):
    return [word.strip() for word in line.split(delimiter_char)]

def parse_java_code_line(code_statement_in_word_tokens):

    #0. Extract the type of statement
    type_of_statement = identify_type_of_statement(code_statement_in_word_tokens)

    #2. Extract all access modifiers
    access_modifiers_identified = [token for token in code_statement_in_word_tokens if is_access_modifier(token)]

    #3. Extract all java data types
    data_types_identified = [token for token in code_statement_in_word_tokens if is_data_type(token)]

    #4. Extract all return types (Do this only for method declaration statements)
    return_types_identified = []
    if type_of_statement == line_type_dict.get(2):
        return_types_identified = [token for token in code_statement_in_word_tokens if is_return_type_keyword(token)]

    #5. Extract all inheritance tokens
    inheritance_keywords_identified = [token for token in code_statement_in_word_tokens if is_inheritance_keyword(token)]

    #6. Extract all exception tokens
    exception_keywords_identified = [token for token in code_statement_in_word_tokens if is_exception_keyword(token)]

    #7. Extract user_defined_data_types such as class or interface or enum
    user_defined_data_type_type_identified = [token for token in code_statement_in_word_tokens if is_user_data_type_keyword(token)]

    #8. If a user defined data type is present, the retrieve the token that immediately follows it.
    # For e.g. Given a statement such as class SampleClass, the earlier step identified the 'class' token.
    # In this step, we must retrieve 'SampleClass' token
    user_defined_data_type_identified = []
    for index,token in enumerate(code_statement_in_word_tokens):
        for data_type_type in user_defined_data_type_type_identified:
            if data_type_type == token:
                user_defined_data_type_identified.append(code_statement_in_word_tokens[index+1])
                break; #Goes with assumption that a line can have only one token such as class or interface

    #9. Keyword markers = A dictionary of all the indices that has a token that we have identified so far.
    # For e.g given a statement such as Class SampleClass => our dict will be {0:['class'], 1:['SampleClass']}
    keywords_markers_dict = {}
    for index, token in enumerate(code_statement_in_word_tokens):
        if (token in access_modifiers_identified \
            or token in data_types_identified \
            or token in return_types_identified \
            or token in inheritance_keywords_identified \
            or token in exception_keywords_identified \
            or token in user_defined_data_type_type_identified \
            or token in user_defined_data_type_identified):
            keywords_markers_dict[index] = token

    #10. Identify inheritance and exception key words in the code statement
    inheritance_marker_positions = []
    exception_marker_positions = []
    for key in sorted(keywords_markers_dict.iterkeys()):
        keyword = keywords_markers_dict.get(key)
        if keyword in inheritance_keywords_identified:
            inheritance_marker_positions.append(key)
        elif keyword in exception_keywords_identified:
            exception_marker_positions.append(key)

    exceptions_and_inheritances_identified = []
    startedReading = False
    for index, token in enumerate(code_statement_in_word_tokens):
        if index in inheritance_marker_positions or index in exception_marker_positions:
            startedReading = True
        elif startedReading and token != ",":
            exceptions_and_inheritances_identified.append(token.replace(",",""))



    #11. The remaining are all user_defined
    remaining_words_identified = []
    for token in code_statement_in_word_tokens:
        if(token.replace(",","") not in access_modifiers_identified \
            and token.replace(",","") not in data_types_identified \
            and token.replace(",","") not in return_types_identified \
            and token.replace(",","") not in user_defined_data_type_type_identified \
            and token.replace(",","") not in user_defined_data_type_identified \
            and token.replace(",","") not in inheritance_keywords_identified \
            and token.replace(",","") not in exception_keywords_identified \
            and token.replace(",","") not in exceptions_and_inheritances_identified):
            remaining_words_identified.append(token)

    #12. If the type of statement is either a field declaration or processing statement,
    # Then we must capture the left_hand_side and right hand side of '='
    expression_list=[]
    if type_of_statement == line_type_dict.get(1) or type_of_statement == line_type_dict.get(5):
        expression_list = get_tokens_for_field_declaration_and_processing_statements(remaining_words_identified)

    left_hand_side_list = []
    right_hand_side_list = []
    remaining_words_filtered = []
    if len(expression_list) > 0:
        left_hand_side_list = expression_list[0]
        right_hand_side_list = expression_list[1]
        for token in remaining_words_identified:
            if token not in expression_list and token not in '=':
                remaining_words_filtered.append(token)

    # print("Code => {}".format(" ".join(code_statement_in_word_tokens)))
    # print("\tType of statement => {}".format(type_of_statement))
    # print("\tLeft-side expression => {}".format(left_hand_side_list))
    # print("\tRight-side expression => {}".format(right_hand_side_list))
    # print("\tAccess modifiers => {}".format(access_modifiers_identified))
    # print("\tJava Data Types identified => {}".format(data_types_identified))
    # print("\tJava Return Types identified => {}".format(return_types_identified))
    # print("\tUser Defined Data Type Type =>{}".format(user_defined_data_type_type_identified))
    # print("\tUser Defined data type =>{}".format(user_defined_data_type_identified))
    # print("\tInheritance keywords =>{}".format(inheritance_keywords_identified))
    # print("\tException keywords =>{}".format(exception_keywords_identified))
    # print("\tException and inheritances identified =>{}".format(exceptions_and_inheritances_identified))
    # print("\tRemaining Words => {}".format(remaining_words_filtered))

    parsed_line_dict = {}
    parsed_line_dict["statement"] = " ".join(code_statement_in_word_tokens)
    parsed_line_dict["statement_type"] = type_of_statement
    parsed_line_dict["left_side_expression"] = left_hand_side_list
    parsed_line_dict["right_side_expression"] = right_hand_side_list
    parsed_line_dict["access_modifiers"] = access_modifiers_identified
    parsed_line_dict["java_data_types"] = data_types_identified
    parsed_line_dict["java_return_types"] = return_types_identified
    parsed_line_dict["user_data_type_type"] = user_defined_data_type_type_identified
    parsed_line_dict["user_data_type"] = user_defined_data_type_identified
    parsed_line_dict["inheritance_type"] = inheritance_keywords_identified
    parsed_line_dict["exception_type"] = exception_keywords_identified
    parsed_line_dict["exceptions_and_inheritances"] = exceptions_and_inheritances_identified
    parsed_line_dict["unknown"] = remaining_words_filtered

    return parsed_line_dict

def get_tokens_for_field_declaration_and_processing_statements(remaining_words_list):
    token_is_equal_to_sign_only = False
    index_having_equal_to_sign = -1;
    left_hand_side_token_list = []
    right_hand_side_token_list = []

    #Remove other special java keywords that may still be in the statement. Like. static, final, etc.
    temp_list = [word for word in remaining_words_list if word.lower() not in java_identifiers_other_keywords_list ]
    remaining_words_list = temp_list

    for index, remaining_word in enumerate(remaining_words_list):
        #find the position of = It can be a separate token or part of a token
        if '=' in remaining_word:
            if(len(remaining_word) == 1):
                #This is an exclusive token having just =
                token_is_equal_to_sign_only = True
            index_having_equal_to_sign = index
            break


    #print(remaining_words_list,token_is_equal_to_sign_only,index_having_equal_to_sign)

    if index_having_equal_to_sign >= 0 and token_is_equal_to_sign_only:
        left_hand_side_token_list = [word for index,word in enumerate(remaining_words_list) if index < index_having_equal_to_sign]
        right_hand_side_token_list = [word for index,word in enumerate(remaining_words_list) if index > index_having_equal_to_sign]
        #For right-hand side alone, append each of the tokens separated by space.
        #For e.g for a statement a = b + c, right side must be 'b + c'
        right_hand_side_token_list = [' '.join(right_hand_side_token_list)]
    elif index_having_equal_to_sign >= 0 and not(token_is_equal_to_sign_only):
        left_portion = remaining_words_list[index_having_equal_to_sign][:remaining_words_list[index_having_equal_to_sign].find('=')]
        right_portion = remaining_words_list[index_having_equal_to_sign][remaining_words_list[index_having_equal_to_sign].find('=')+1:]

        if len(left_portion) > 0:
            left_hand_side_token_list.append(left_portion)
        if len(right_portion) > 0:
            right_hand_side_token_list.append(right_portion)

        if len(left_hand_side_token_list) <= 0:
            left_hand_side_token_list.append(remaining_words_list[index_having_equal_to_sign-1])
        if len(right_hand_side_token_list) <= 0:
            right_hand_side_token_list = [' '.join(remaining_words_list[index_having_equal_to_sign+1:])]
    #else:
        #did not find the equal to sign or something is wrong

    combined_list = left_hand_side_token_list + right_hand_side_token_list
    return combined_list

def is_access_modifier(token):
    return token in java_identifiers_access_modifier_list

def is_data_type(token):
    return token in java_identifiers_data_types_list

def is_inheritance_keyword(token):
    return token in java_identifiers_inheritance_keywords_list

def is_exception_keyword(token):
    return token in java_identifiers_exception_keywords_list

def is_user_data_type_keyword(token):
    return token in java_identifiers_user_data_type_identifier_list

def is_return_type_keyword(token):
    return token in java_identifiers_return_types_list

def is_class_statement(code_statement_list):
    # public class A{} ==> this statement must return True
    # class A = new A() ==> this statement must return False
    return "class" in code_statement_list and "new" not in code_statement_list

def is_method_statement(code_statement_list):
    openingBraceFound = False
    openingBraceIndex = -1
    closingBraceFound = False
    returnTypeFound = False

    #the specialKeyWordFound and specialKeywordList is used to ignore statements containing keywords such as new, Arrays.asList(, etc.
    #It is because such statements must be treated as field declaration statements.
    specialKeyWordFound = False
    specialKeywordList = ['new', 'Arrays.asList'] + java_identifiers_arithmentic_operators_list + java_identifiers_comparison_operators_list
    for index,token in enumerate(code_statement_list):
        if "(" in token:
            openingBraceFound = True
            openingBraceIndex = index
        if ")" in token:
            closingBraceFound = True
        for specialKeyword in specialKeywordList:
            if specialKeyword.lower() in token.lower():
                specialKeyWordFound = True
                break
    #print(code_statement_list,openingBraceFound,openingBraceIndex,closingBraceFound,specialKeyWordFound)
    if(openingBraceFound and closingBraceFound and openingBraceIndex != -1 and not(specialKeyWordFound)):
        #Narrow down to whether this is a method signature or a method Invocation
        if(openingBraceIndex == 0):
            #This means that this is a method Invocation
            return 3
        else:
            #Need to do additional checks before concluding
            word_before_opening_brace = code_statement_list[openingBraceIndex-1]

            if word_before_opening_brace in java_identifiers_return_types_list:
                #This means that this is a method signature and not an invocation statement.
                #E.g. statement => public void foo()
                return 2
            elif word_before_opening_brace in java_identifiers_access_modifier_list:
                #This also means that this is a method signature.
                #But this method is not a normal method, but a constructor instead
                return 4
            else:
                return 3
    else:
        return -1

def expression_or_field_delcaration(code_statement_list):
    found_in_arithmetic_list = False
    found_in_assignment_list = False
    found_in_data_type_list = False
    new_token_found = False
    for token in code_statement_list:
        for operator in java_identifiers_assignment_operators_list:
            if operator in token:
                found_in_assignment_list = True
                if operator == 'new':
                    new_token_found = True
        for operator in java_identifiers_arithmentic_operators_list:
            if operator in token:
                found_in_arithmetic_list = True
        for operator in java_identifiers_data_types_list:
            if operator in token:
                found_in_data_type_list = True

    #print(code_statement_list,found_in_data_type_list,found_in_arithmetic_list,found_in_assignment_list,new_token_found)

    if found_in_data_type_list:
        return 1 #This can be something like int a = 5;
    elif (found_in_arithmetic_list and found_in_assignment_list):
        return 5 # This is an expression statement e.g. a = b+c
    elif (found_in_arithmetic_list):
        return 5 #This is an expression statement e.g. a = 100 / 10
    elif (found_in_assignment_list):
        if new_token_found:
            return 1 #This is a field declaration statement. eg. SampleClass sampleClass = new SampleClass()
        return 5 #This is a processing statemnt. e.g. a = 5
    else:
        return 1 #This can also be a field declaration statement. For e.g. int a, b, c; or String a, b, c, d;

def identify_type_of_statement(code_statement_list):
    if is_class_statement(code_statement_list):
        return line_type_dict.get(6)

    method_check = is_method_statement(code_statement_list)
    if method_check != -1:
        return line_type_dict.get(method_check)

    expression_or_field_declaration_check = expression_or_field_delcaration(code_statement_list)
    if expression_or_field_declaration_check != -1:
        return line_type_dict.get(expression_or_field_declaration_check)

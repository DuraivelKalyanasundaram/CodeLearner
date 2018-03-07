# The purpose of this python file is to enlist all the global dictionaries.
# This can be imported into other python programs for standard reference

training_features_dict =  { 1: "JDBC Connection String dection",
                            2: "JDBC Password detection"
                            }

line_type_dict = {
                    1: "Field declaration",
                    2: "Method declaration",
                    3: "Method Invocation",
                    4: "Constructor definition",
                    5: "Processing statement",
                    6: "Class Declaration",
                    7: "Others"
                    }

user_input_dict = {
                    "feature" : "",
                    "application_path" : "",
                    "application_file" : "",
                    "line_number" : "",
                    "line_type" : ""
}

final_learnt_dict = {
                    "feature" : "",
                    "application_file_name" : "",
                    "file_name_extension" : "",
                    "line" : "",
                    "access_modifier" : "",
                    "datatype" : "",
                    "user_identifier" : "",  #this field identifies the user provided token. It could refer to the variable or the method name, etc.
                    "value" : "", #value if in case this is a field declaration statement
                    "method" : "", #if the line is inside the method, then the method info should come here.
                    "class" : "" #if the line is inside the class, then the class info should come here.
}

java_identifiers_access_modifier_list = ['public', 'protected', 'internal', 'private']
java_identifiers_data_types_list = ['String', 'int', 'float', 'double', 'long']
java_identifiers_return_types_list = java_identifiers_data_types_list + ['void']
java_identifiers_user_data_type_identifier_list = ['class', 'interface', 'enum']
java_identifiers_inheritance_keywords_list = ['extends', 'implements']
java_identifiers_exception_keywords_list = ['throws', 'catch', 'try']
java_identifiers_assignment_operators_list = ['=', 'new']
java_identifiers_arithmentic_operators_list = ['+=', '-=', '++', '--', '*', '/', '+', '-']
java_identifiers_comparison_operators_list = ['==', '!=', '&&', '||', '>', '>=', '<=', '<']
java_identifiers_other_keywords_list = ['static','final']

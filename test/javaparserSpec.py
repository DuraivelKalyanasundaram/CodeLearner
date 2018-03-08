import unittest
import sys
sys.path.insert(0, '/Users/cloudlift/CodeLearner')
from javaparser import get_tokens_for_field_declaration_and_processing_statements, identify_type_of_statement, parse_java_code_line, get_list_of_words_from_statement
from global_reference import line_type_dict

class TestJavaParser4_get_tokens_for_field_declaration_and_processing_statements(unittest.TestCase):

    def test_spacetokenized1(self):
        input_remaining_words_list = ['url','=','"jdbc:mysql://localhost:3306/airline";']
        actual_output = get_tokens_for_field_declaration_and_processing_statements(input_remaining_words_list)
        expected_output = [input_remaining_words_list[0], input_remaining_words_list[2]]

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'get_tokens_for_field_declaration_and_processing_statements'" \
        "\nActual output is {} \nExpected output is{}".format(actual_output, expected_output))

    def test_spacetokenized2(self):
        input_remaining_words_list = ['a','=','b','+','c']
        actual_output = get_tokens_for_field_declaration_and_processing_statements(input_remaining_words_list)
        expected_output = ['a', 'b + c']

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'get_tokens_for_field_declaration_and_processing_statements' \nActual output is {} \n" \
        "Expected output is {}".format(actual_output, expected_output))

    def test_nonspacetokenized1(self):
        input_remaining_words_list = ['url=','"jdbc:mysql://localhost:3306/airline";']
        actual_output = get_tokens_for_field_declaration_and_processing_statements(input_remaining_words_list)
        expected_output = ['url', input_remaining_words_list[1]]

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'get_tokens_for_field_declaration_and_processing_statements'. \n Actual output is {} \n" \
        "Expected output is {}".format(actual_output, expected_output))

    def test_nonspacetokenized2(self):
        input_remaining_words_list = ['url','="jdbc:mysql://localhost:3306/airline";']
        actual_output = get_tokens_for_field_declaration_and_processing_statements(input_remaining_words_list)
        expected_output = [input_remaining_words_list[0], '"jdbc:mysql://localhost:3306/airline";']

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'get_tokens_for_field_declaration_and_processing_statements'. \n Actual output is {} \n" \
        "Expected output is {}".format(actual_output, expected_output))

    def test_nonspacetokenized3(self):
        input_remaining_words_list = ['a','=','b+','c']
        actual_output = get_tokens_for_field_declaration_and_processing_statements(input_remaining_words_list)
        expected_output = ['a', 'b+ c']

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'get_tokens_for_field_declaration_and_processing_statements'. \n Actual output is {} \n" \
        "Expected output is {}".format(actual_output, expected_output))

    def test_nonspacetokenized4(self):
        input_remaining_words_list = ['a','=','b','+c']
        actual_output = get_tokens_for_field_declaration_and_processing_statements(input_remaining_words_list)
        expected_output = ['a', 'b +c']

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'get_tokens_for_field_declaration_and_processing_statements'. \n Actual output is {} \n" \
        "Expected output is {}".format(actual_output, expected_output))

    def test_nonspacetokenized5(self):
        input_remaining_words_list = ['a=','b','+','c']
        actual_output = get_tokens_for_field_declaration_and_processing_statements(input_remaining_words_list)
        expected_output = ['a', 'b + c']

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'get_tokens_for_field_declaration_and_processing_statements'. \n Actual output is {} \n" \
        "Expected output is {}".format(actual_output, expected_output))

    def test_nonspacetokenized6(self):
        input_remaining_words_list = ['a=','b+','c']
        actual_output = get_tokens_for_field_declaration_and_processing_statements(input_remaining_words_list)
        expected_output = ['a', 'b+ c']

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'get_tokens_for_field_declaration_and_processing_statements'. \n Actual output is {} \n" \
        "Expected output is {}".format(actual_output, expected_output))

    def test_nonspacetokenized7(self):
        input_remaining_words_list = ['a=','b','+c']
        actual_output = get_tokens_for_field_declaration_and_processing_statements(input_remaining_words_list)
        expected_output = ['a', 'b +c']

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'get_tokens_for_field_declaration_and_processing_statements'. \n Actual output is {} \n" \
        "Expected output is {}".format(actual_output, expected_output))

class JavaParserTest4_identify_type_of_statement(unittest.TestCase):

    def test_class_check1(self):
        input_code_statement_list=['public', 'class', 'SampleClass{']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(6)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_class_check2(self):
        input_code_statement_list=['public', 'class', 'SampleClass']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(6)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_method_declaration1(self):
        input_code_statement_list = ['public','void','doGet(','String','name){']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(2)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_method_declaration2(self):
        input_code_statement_list = ['public','void','doGet(String', 'name){']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(2)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_method_invocation1(self):
        input_code_statement_list = ['Person','person','=','doGet(name);']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(3)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_method_invocation2(self):
        input_code_statement_list = ['doGet(name);']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(3)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_method_invocation3(self):
        input_code_statement_list = ['person','=','doGet(name);']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(3)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_method_invocation4(self):
        input_code_statement_list = ['person=','doGet(name);']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(3)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_method_invocation5(self):
        input_code_statement_list = ['person','=doGet(name);']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(3)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_field_declaration1(self):
        input_code_statement_list = ['int','a','=','5;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(1)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_field_declaration2(self):
        input_code_statement_list = ['String','a','=','"hello;"']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(1)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_field_declaration3(self):
        input_code_statement_list = ['float','a','=','3.5']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(1)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))


    def test_field_declaration4(self):
        input_code_statement_list = ['SampleClass','sampleClass','=','new', 'SampleClass();']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(1)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_field_declaration5(self):
        input_code_statement_list = ['SampleClass','sampleClass;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(1)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_field_declaration6(self):
        input_code_statement_list = ['int','a;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(1)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_field_declaration7(self):
        input_code_statement_list = ['int','a,b;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(1)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_field_declaration8(self):
        input_code_statement_list = ['int','a,','b;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(1)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))


    def test_field_declaration9(self):
        input_code_statement_list = ['int','[]','a;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(1)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))


    def test_field_declaration10(self):
        input_code_statement_list = ['int','[]','a', '=','Arrays.asList(', '5,','2,', '3);']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(1)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement1(self):
        input_code_statement_list = ['a','=','b', '+', 'c;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))


    def test_processing_statement2(self):
        input_code_statement_list = ['a','=','100', '*', '10;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement3(self):
        input_code_statement_list = ['a','=','b;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement4(self):
        input_code_statement_list = ['a=','b;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {} \n Input is {}".format(actual_output, expected_output,input_code_statement_list))

    def test_processing_statement5(self):
        input_code_statement_list = ['a','=b;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement6(self):
        input_code_statement_list = ['a','=b', '+', 'c;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement7(self):
        input_code_statement_list = ['a=','b', '+', 'c;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement8(self):
        input_code_statement_list = ['a=','b+c;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement9(self):
        input_code_statement_list = ['a=','b;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement10(self):
        input_code_statement_list = ['a++;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement11(self):
        input_code_statement_list = ['b--;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))


    def test_processing_statement12(self):
        input_code_statement_list = ['a', '+=', '5;']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {} \ninput is{}".format(actual_output, expected_output,input_code_statement_list))

    def test_processing_statement13(self):
        input_code_statement_list = ['a', '+=', '5',';']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement14(self):
        input_code_statement_list = ['a', '-=', '5',';']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement15(self):
        input_code_statement_list = ['a', '*=', '5',';']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))


    def test_processing_statement16(self):
        input_code_statement_list = ['a', '/=', '5',';']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement17(self):
        input_code_statement_list = ['a', '=', 'b','+','(c','/','d)',';']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {} \nInput is{}".format(actual_output, expected_output, input_code_statement_list))

    def test_processing_statement18(self):
        input_code_statement_list = ['s', '=', '"Hello";']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

    def test_processing_statement19(self):
        input_code_statement_list = ['s', '=', '"Hello"',';']
        actual_output = identify_type_of_statement(input_code_statement_list)
        expected_output = line_type_dict.get(5)

        self.assertEqual(actual_output, expected_output, \
        "Did not get the expected output for method 'identify_type_of_statement' " \
        "\nActual output is {} \nExpected output is {}".format(actual_output, expected_output))

class JavaParserTest4_parse_java_code_line(unittest.TestCase):

    def test_Processing_Statement1(self):
        input_code_statement = 'String url = "jdbc:mysql://localhost:3306/airline";'
        input_word_tokens = get_list_of_words_from_statement(input_code_statement)
        actual_output_dict = parse_java_code_line(input_word_tokens)
        self.assertEqual('"jdbc:mysql://localhost:3306/airline";', actual_output_dict.get('right_side_expression'))
        self.assertEqual('url', actual_output_dict.get('left_side_expression'))
        self.assertEqual(input_code_statement, actual_output_dict.get('statement'))
        self.assertEqual(line_type_dict.get(1), actual_output_dict.get('statement_type'))
        self.assertTrue(actual_output_dict.get('java_data_types'))
        self.assertFalse(actual_output_dict.get('java_return_types'))
        self.assertFalse(actual_output_dict.get('access_modifiers'))
        self.assertFalse(actual_output_dict.get('inheritance_type'))
        self.assertFalse(actual_output_dict.get('exceptions_and_inheritances'))
        self.assertFalse(actual_output_dict.get('unknown'))

    def test_Processing_Statement2(self):
        input_code_statement = 'public class CustomerFlightDetails extends HttpServlet'
        input_word_tokens = get_list_of_words_from_statement(input_code_statement)
        actual_output_dict = parse_java_code_line(input_word_tokens)

        self.assertFalse(actual_output_dict.get('right_side_expression'))
        self.assertFalse(actual_output_dict.get('left_side_expression'))
        self.assertEqual(input_code_statement, actual_output_dict.get('statement'))
        self.assertEqual(line_type_dict.get(6), actual_output_dict.get('statement_type'))
        self.assertFalse(actual_output_dict.get('java_data_types'))
        self.assertFalse(actual_output_dict.get('java_return_types'))

        self.assertTrue(actual_output_dict.get('access_modifiers'))
        self.assertEqual(['public'], actual_output_dict.get('access_modifiers'))

        self.assertTrue(actual_output_dict.get('inheritance_type'))
        self.assertEqual(['extends'], actual_output_dict.get('inheritance_type'))

        self.assertTrue(actual_output_dict.get('exceptions_and_inheritances'))
        self.assertEqual(['HttpServlet'], actual_output_dict.get('exceptions_and_inheritances'))

        self.assertFalse(actual_output_dict.get('unknown'))

    def test_Processing_Statement3(self):
        input_code_statement = 'private static final long serialVersionUID = 1L;'
        input_word_tokens = get_list_of_words_from_statement(input_code_statement)
        actual_output_dict = parse_java_code_line(input_word_tokens)

        self.assertTrue(actual_output_dict.get('left_side_expression'))
        self.assertEqual('serialVersionUID', actual_output_dict.get('left_side_expression'))

        self.assertTrue(actual_output_dict.get('right_side_expression'))
        self.assertEqual('1L;', actual_output_dict.get('right_side_expression'))

        self.assertEqual(input_code_statement, actual_output_dict.get('statement'))
        self.assertEqual(line_type_dict.get(1), actual_output_dict.get('statement_type'))

        self.assertTrue(actual_output_dict.get('java_data_types'))
        self.assertEqual(['long'], actual_output_dict.get('java_data_types'))

        self.assertFalse(actual_output_dict.get('java_return_types'))

        self.assertTrue(actual_output_dict.get('access_modifiers'))
        self.assertEqual(['private'], actual_output_dict.get('access_modifiers'))

        self.assertFalse(actual_output_dict.get('inheritance_type'))

        self.assertFalse(actual_output_dict.get('exceptions_and_inheritances'))

        self.assertTrue(actual_output_dict.get('unknown'))
        self.assertEqual(['static','final'], actual_output_dict.get('unknown'))


    def test_Processing_Statement4(self):
        input_code_statement = 'public CustomerFlightDetails()'
        input_word_tokens = get_list_of_words_from_statement(input_code_statement)
        actual_output_dict = parse_java_code_line(input_word_tokens)

        self.assertFalse(actual_output_dict.get('left_side_expression'))

        self.assertFalse(actual_output_dict.get('right_side_expression'))

        self.assertEqual(input_code_statement, actual_output_dict.get('statement'))
        self.assertEqual(line_type_dict.get(4), actual_output_dict.get('statement_type'))

        self.assertFalse(actual_output_dict.get('java_data_types'))

        self.assertFalse(actual_output_dict.get('java_return_types'))

        self.assertTrue(actual_output_dict.get('access_modifiers'))
        self.assertEqual(['public'], actual_output_dict.get('access_modifiers'))

        self.assertFalse(actual_output_dict.get('inheritance_type'))

        self.assertFalse(actual_output_dict.get('exceptions_and_inheritances'))

        self.assertFalse(actual_output_dict.get('unknown'))

    def test_Processing_Statement5(self):
        input_code_statement = 'super();'
        input_word_tokens = get_list_of_words_from_statement(input_code_statement)
        actual_output_dict = parse_java_code_line(input_word_tokens)

        self.assertFalse(actual_output_dict.get('left_side_expression'))

        self.assertFalse(actual_output_dict.get('right_side_expression'))

        self.assertEqual(input_code_statement, actual_output_dict.get('statement'))
        self.assertEqual(line_type_dict.get(3), actual_output_dict.get('statement_type'))

        self.assertFalse(actual_output_dict.get('java_data_types'))

        self.assertFalse(actual_output_dict.get('java_return_types'))

        self.assertFalse(actual_output_dict.get('access_modifiers'))

        self.assertFalse(actual_output_dict.get('inheritance_type'))

        self.assertFalse(actual_output_dict.get('exceptions_and_inheritances'))

        self.assertFalse(actual_output_dict.get('unknown'))

    def test_Processing_Statement6(self):
        input_code_statement = 'protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException'
        input_word_tokens = get_list_of_words_from_statement(input_code_statement)
        actual_output_dict = parse_java_code_line(input_word_tokens)

        self.assertFalse(actual_output_dict.get('left_side_expression'))

        self.assertFalse(actual_output_dict.get('right_side_expression'))

        self.assertEqual(input_code_statement, actual_output_dict.get('statement'))
        self.assertEqual(line_type_dict.get(2), actual_output_dict.get('statement_type'))

        self.assertFalse(actual_output_dict.get('java_data_types'))

        self.assertTrue(actual_output_dict.get('java_return_types'))
        self.assertEqual(['void'],actual_output_dict.get('java_return_types'))

        self.assertTrue(actual_output_dict.get('access_modifiers'))
        self.assertEqual(['protected'],actual_output_dict.get('access_modifiers'))

        self.assertFalse(actual_output_dict.get('inheritance_type'))

        self.assertTrue(actual_output_dict.get('exception_type'))
        self.assertEqual(['throws'], actual_output_dict.get('exception_type'))

        self.assertTrue(actual_output_dict.get('exceptions_and_inheritances'))
        self.assertEqual(['ServletException','IOException'],actual_output_dict.get('exceptions_and_inheritances'))

        self.assertFalse(actual_output_dict.get('unknown'))



if __name__ == '__main__':
    unittest.main()

import re


def list_split(string, split_list, removechar=('<', '>')):
    """
        Take a string and remove the item inside a list and return the splited string as a list


    Modified (heavily) from https://stackoverflow.com/a/4697047/7332922

    :param string: The string to process
    :param split_list: Element to remove from the string -> MUST BE IN ORDER
    :param removechar: Special characters to remove
    :return: List of the remaining elements in the string
    """
    try:
        # Split the string
        splited_string = []
        for c in split_list:
            v = string.split(c)
            string = v[1]
            splited_string.append(v[0])
            try:
                splited_string.remove('')
            except:
                pass

        # Remove the chars
        for c in removechar:
            string = string.replace(c, '')

        # If the list is not empty, there is an item remaining
        if string != "":
            splited_string.append(string)

        return splited_string

    except:
        # In case of error, return an empty list
        return []


def rule_to_regex(rule: str) -> tuple:
    """
        Transform the rule in a regex and provide a tuple

        Future update :
                - HEX

    :param rule:
    :return: a tuple containing :
            - rule : Regex of the rule
            - arguments : List of custom variable in the rule (and their order)
            - forbidden_elements : List to easily fetch arguments when the route is query
    """
    # Variables setted to default
    arguments = []
    forbidden_elements = []
    arguments_splited_list = []

    # Build the argument list
    for i in re.findall('<([a-zA-Z]+:[a-zA-Z]+|[a-zA-Z]+)>+', rule):
        l = i.split(":")
        arguments_splited_list.append("<" + i + ">")  # for forbidden_elements
        # No type -> <test>
        if len(l) == 1:
            arguments.append(l[0])

        # Typed -> <str:test>
        elif len(l) == 2:
            arguments.append(l[1])

    forbidden_elements = list_split(rule, arguments_splited_list)

    # Match int var type
    rule = re.sub(r'<int:[a-zA-Z]+>', '\\\d+', rule)

    # Match str var type
    rule = re.sub(r'<str:[a-zA-Z]+>', '[a-zA-Z]+', rule)

    # Math all other
    rule = re.sub(r'<[a-zA-Z0-9]+>', '[a-zA-Z0-9]+', rule)

    # Add the endline in case
    if not rule.endswith('$'):
        rule += '$'

    return rule, arguments, forbidden_elements

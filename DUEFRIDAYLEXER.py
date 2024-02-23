import re
import string

def CutOneLineTokens(thing):
    output_list = []
    key = ""
    #output_list.append("hi")
    up = ""
    up_2 = ""
    up_3 = ""
    up_4 = ""
    # key = re.match(r"\b(if|else|int|float)\b", thing)
    # iden = re.match(r"[a-zA-Z0-9]\d", thing)
    # op = re.match(r"[=+>*/]", thing)
    # lit = re.match(r"\b\d+\b", thing)

    target_keyword = re.match(r"\b(if|else|int|float)\b", thing)
    target_idenifier = re.search(r"[a-zA-Z0-9]\d", thing)
    target_operator = re.search(r"[=+>*/]", thing)
    target_literal = re.search(r"\b\d+\b", thing)
   # for x in output_list:
    #if re.match(r"\b(if|else|int|float)\b", thing):  # finished
    if target_keyword:
        up = ("<key," + target_keyword.group() + ">")
        output_list.append(up)
        #print(output_list)
    else:
        print("No match for keyword")
    if target_idenifier:
            up_2 = ("<id," + target_idenifier.group() + ">")
            output_list.append(up_2)
           # print(output_list)
    else:
            print("No match for idenifier")

    if target_operator:
            up_3 = ("<op," + target_operator.group() + ">")
            output_list.append(up_3)
           # print(output_list)
    else:
            print("No match for operator")

    if target_literal:
        up_4 = ("<lit," + target_literal.group() + ">")
        output_list.append(up_4)
       # print(output_list)
    else:
        print("No match for literal")

    print(output_list)



        #    output_list.append(up)
       #     print(output_list)
 #   if re.match(r"[a-zA-Z0-9]\d", thing):  # finished

         #   iden = ("<id," + thing + ">")
           # output_list[x] = output_list.append(x)
            # x += 1
   # if re.match(r"[=+>*/]", thing):  # finished

         #   op = ("<op," + thing + ">")
            #output_list[x] = output_list.append(x)
            # x += 1
   # if re.match(r"\b\d+\b", thing):  # finished

           # lit = ("<lit," + thing + ">")
            #output_list[x] = output_list.append(x)
            # x += 1
        # if re.match(r"[()\":;]", thing):  # finished
   # else:
    #        print("No match")

test_cases = [
    "int A1=5",
    "float DSDXD =1034.2",
    "float cresult = A1 +BBB2 * BBB2",
    'if (cresult >10):',
    'print("TinyPie ")',
    'float int float',
]


if __name__ == '__main__':
    s = "int A1 = 5"
    d = "float DSDXD =1034.2"
    CutOneLineTokens(s)
    CutOneLineTokens(d)

    cut
from entroPy import generator

x = generator()
x.int_gen(column='Integer Column')
x.str_gen(column='String Column')
x.bool_gen(column='Boolean Column', trinary='Unknown')

dataframe = x.output()

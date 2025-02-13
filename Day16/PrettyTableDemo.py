import prettytable

table= prettytable.PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Charmandar"])
table.add_column("Type",["Electric","Fire"])

table.align="l"

print(table)


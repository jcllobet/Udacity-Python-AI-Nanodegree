def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
      for line in f:
        name = (line.strip().split(",")[0])
        cast_list.append(name)
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)

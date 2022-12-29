import random 

def file_to_list(filename):
    file = open(filename, 'r')
    ingredients = []
    for line in file:
        ingredients.append(line.strip())
    file.close()
    return ingredients

options = file_to_list('ingredients.txt')

def segment_list(lst):
  random.shuffle(lst)
  nested_lst = []
  while len(lst) > 0:
    chunk_size = random.randint(1, len(lst))
    chunk = lst[:chunk_size]
    nested_lst.append(chunk)
    lst = lst[chunk_size:]
  return nested_lst

def list_to_string(lst):
  result = ""
  for i, item in enumerate(lst):
    result += str(item)
    if i == len(lst) - 2:
      result += " and "
    elif i < len(lst) - 1:
      result += ", "  
  return result



def recipe_get(options):
    total_time = 0
    cur_ingredients = random.sample(options, random.randint(6, len(options)))
    random.shuffle(cur_ingredients)
    steps = random.randint(1, 5)
    tool = random.choice(['pan', 'pot'])
    print("Todays recipe:\n" + "-"*20)
    print("Heat up your " + tool + " to " + str(random.randint(50, 100)) + " percent heat.")
    cur_ingredients = segment_list(cur_ingredients)
    for x in range(len(cur_ingredients)):
        cur_step_ingredients = cur_ingredients[x]
        cur_sub_step_ingredients = segment_list(cur_step_ingredients)
        for y in range(len(cur_sub_step_ingredients)):
            cur_add_str = "Add to " + tool + ": "
            cur_add_str += ' ' + list_to_string(cur_sub_step_ingredients[y])
            sub_step_cook_time = random.randint(2, 10)
            total_time += sub_step_cook_time
            print(cur_add_str + " and cook for " + str(sub_step_cook_time) + " minutes.")
        step_cook_time = random.randint(10, 20)
        total_time += step_cook_time
        print("Leave to cook for " + str(step_cook_time) + " more minutes before moving on.")
    print('-'*20)
    print("Bon Apetite!")
    print("Total Cooktime: " + str(total_time) + " minutes.")
    print('-'*20)

while True:
    ui = input('-: ')
    print(recipe_get(options))
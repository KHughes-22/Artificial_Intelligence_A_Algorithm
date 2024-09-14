import sys
import math

def expression(city1,arrive):
  """
  Uses the Haversine formula to calculate the straight line distance between two cities

  :param str city1: the current city to the destination
  :param str arrive: the destination that we would get the straight line to
  :return: the Haversine calculation
  """
  if (city1 == arrive):
    return 0
  else:
    return(math.pi / 180 * ((2 * 3958.8 * math.sqrt((math.sin((arrive[0] - city1[0]) / 2) ** 2) + 
                                   (math.cos(city1[0]) * math.cos(arrive[0]) * (math.sin((arrive[1] - city1[1]) / 2) ** 2)) ))))


def straight_line_distance(arrive):
  """
  Opens coordinates and gets the distance between 

  :param str: the destination city
  :return: a dictionary {str, float} containing the the current city and the Haversine calculation
  """

  coords = open("coordinates-2.txt", "r")
  arrive_coords = []
  #find the coordinates of the arrive city and stor in arrive_coords
  for line in coords:
    line_info = line.split(":")
    #print(line_info)
    if line_info[0].lower() == arrive.lower():
      #creates the arrival coordinaates in formate [float, float]
      arrive_coords = line_info[1].strip('\n')[1:-1].split(',')
      arrive_coords = [float(arrive_coords[0]), float(arrive_coords[1]) ]
      break
  coords.seek(0)
  straight_line_distance_dict = {}
  for line in coords:
    current_city = line.split(':')[1].strip('\n')[1:-1].split(',')
    current_city = [float(current_city[0]), float(current_city[1])]
    straight_line_distance_dict[line.split(':')[0]] = expression(current_city, arrive_coords)

  return straight_line_distance_dict

#creates a dictionary containing a key of the city and a value of a dictionary to the connecting city and its value
def create_map():
  """
  creates a dictionary using the map2

  :return: returns a dictionary Key: starting city, value: the corresponding cities
  """
  map = open("map-2.txt", "r")
  map_dict = {}
  for line in map:
    city_dict = []
    line_split = line.split('-')
    connecting_split = line_split[1][:-1].split(',')
    for connecting_city in connecting_split:
      split_connecting_city = connecting_city.split('(')
      city_dict.append([float(split_connecting_city[1].strip(')')), split_connecting_city[0]])
    map_dict[line_split[0]] = city_dict
  return map_dict

  
def main(depart, arrive):
  """
  finds the shortes path using the A* algorithm and prints the output

  :param str depart: the departing city
  :param str arrive: the arriving city
  """
  straight_line_distance_dict = straight_line_distance(arrive)
  map_dict = create_map()

  all_paths = [x for x in map_dict[depart]]
  shortest_path_index = 0
  shortest_value = 50000
  path_found = False

  while(not path_found):
    current_index = 0
    shortest_value = all_paths[0][0] + straight_line_distance_dict[all_paths[0][-1]]
    shortest_path_index = 0

    for next_city in all_paths:
      #next_city[0] is your current value for the path and add to straight line distance to arrive
      if(next_city[1] not in all_paths[current_index]):
        current_straight_value = next_city[0] + straight_line_distance_dict[next_city[-1]]
        if current_straight_value < shortest_value:
          shortest_value = current_straight_value
          shortest_path_index = current_index
      current_index += 1

      if (straight_line_distance_dict[all_paths[shortest_path_index][-1]] == 0):
        path_found = True
      
      #create a new path while updating the current value.
      #all new paths would be the current path plus all nodes linked to shortest path
      else:
        for x in map_dict[all_paths[shortest_path_index][-1]]:
          #print(x)
          temp = all_paths[shortest_path_index].copy()
          temp[0] = temp[0] + x[0]
          temp.append(x[1])
          all_paths.append(temp)

      #remove the shortest path that doesn't contain the new cities
        all_paths.pop(shortest_path_index)

  print("From city: " + depart + '\n')
  print("To City: " + arrive + '\n')
  print("Best Route: " + depart, end =' - ')
  for element in all_paths[shortest_path_index][1:-1]:
    print(element, '-', end = '')
  print(' ' + all_paths[shortest_path_index][-1])
  print("\nTotal distance: {:0.2f}".format(all_paths[shortest_path_index][0]))
  print()

if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2])

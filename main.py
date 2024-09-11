import sys
import math
import re

#straight line formula
#returns float
def expression(city1,arrive):
  if (city1 == arrive):
    return 0
  else:
    return((2 * 3958.8 * math.sqrt((math.sin((arrive[0] - city1[0]) / 2) ** 2) + 
                                   (math.cos(city1[0]) * math.cos(arrive[0]) * (math.sin((arrive[1] - city1[1]) / 2) ** 2)) )))

#Gets the distance between two points.
#returns a list of the city and the distance between the city and the arrival city [str, float]
def straight_line_distance(arrive):
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

def create_map():
  map = open("map-2.txt", "r")
  map_dict = {}
  for line in map:
    line_split = line.split('-')
    map_dict[line_split[0]] = line_split[1][:-1].split(',')
  return map_dict

  
def main(depart, arrive):
  straight_line_distance_dict = straight_line_distance(arrive)
  map_dict = create_map()

  all_paths = [[0, depart]]
  while(True):
    shortest_index = 0
    smallest_value = 10000
    for path in all_paths:
      print(map_dict[path[-1]])
    break
  #print(all_paths)

  
def test_cases():
  main("SanJose", "Sacramento")

if __name__ == "__main__":
  test_cases()
  #main(sys.argv[1], sys.argv[2])

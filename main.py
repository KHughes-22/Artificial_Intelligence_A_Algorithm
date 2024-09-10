import sys
import math


def expression(city1,arrive):
  return 2 * 3958.8 * math.asin(math.sqrt(math.sin((arrive[0] - city1[0]) / 2) ** 2) + 
    math.cos(city1[0]) * math.cos(arrive[0]) 
    * math.sin((arrive[1] - city1[1]) / 2) ** 2)

#Gets the distance between two points.
#returns a list of the city and the distance between the city and the arrival city [str, float]
def straight_line_distance(arrive):
  coords = open("coordinates-2.txt", "r")
  arrive_coords = []
  #find the coordinates of the arrive city and stor in arrive_coords
  for line in coords:
    line_info = line.split(":")
    print(line_info)
    if line_info[0].lower() == arrive.lower():
      #creates the arrival coordinaates in formate [float, float]
      arrive_coords = line_info[1].strip('\n')[1:-1].split(',')
      arrive_coords = [float(arrive_coords[0]), float(arrive_coords[1]) ]
      break
    
  straight_line_distance_list = []
  for line in coords:
    current_city = line.split(':')[1].strip('\n')[1:-1].split(',')
    current_city = [float(current_city[0]), float(current_city[1])]
    straight_line_distance_list.append([line.split(':')[0], expression(current_city, arrive_coords)])

  return straight_line_distance_list


def main(depart, arrive):
  print(straight_line_distance(arrive))
  #map = open("map-2.txt", "r")
  

if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2])

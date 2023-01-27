


running command: python exercise04/main.py 

Two types of testcases written
run python exercise04/main.py and then give choice 1:
    Need to give how many file to be tested. Value can be upto 28(<=28)
    Then it will run test for all those files. 
choice 2:
    It will run test case for individual file. In main.py, 54th line is where the name of the file is mentioned.

***In main.py, line no 40, U can change the time bound given to perform 2opt heuristic. currently given 100 seconds. 

choice 8:
 This test cases is for eight cities distributed on a circle at a distance of 1000 from the origin.
Each city is located at an angle of 0°, 10°, 30°, 60°, 100°, 150°, 210° and 280° around the semi-clock. In this order, IDs 1 to 8 are assigned.
Clearly, the optimal solution for these cities is a clockwise or anti-clockwise route around the cities from any given city.

(a) NN_1.
The search starts from city 3. In this case, the route first goes clockwise around cities 3, 2 and 1 in order of proximity. City 1 to city 4 is at an angle of 60° and city 1 to city 8 is at an angle of 80° apart, so move on to city 4 next. Then it goes anti-clockwise round cities 5,6,7,8 and back to city 1.
Answer-> {3,2,1,4,5,6,7,8}

(b) NN_2.
Start the search from city 4. In this case, in order of proximity, first go around cities 4, 3, 2 and 1. City 5 is 100° away from city 1 and city 8 is 80° away from city 1, so the search continues anti-clockwise to city 8,7,6,5 and returns to city 4. This means that in this case the optimal solution is obtained.
Answer-> {4,3,2,1,8,7,6,5}

(c) 2-Opt.
With {1,8,3,2,7,6,5,4} as the initial solution, a search is conducted at 2Opt.
The search proceeds from the initial solution {1,8,3,2,7,6,5,4} -> {1,2,3,8,7,6,5,4} -> {1,2,3,4,5,6,7,8}.If you want to check the search process, uncomment #printTour(s) in L23 of two_opt.py and run this testcase.
   

Extra package used: tsplib95 (For reading tsp files)

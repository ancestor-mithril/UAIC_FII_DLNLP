Sometimes engineers and mathematicians need to perform calculations or run simulation for their problem. They usually use an easy to learn programming language such as Python and they do not require extensive knowledge of programming. 
Even so, writing code in Python requires time spent in learning or searching for language constructs and characteristics. 
We propose an application which helps transforming semi-formal language (using engineering and mathematical formalism combined with natural language) into Python code. Using this application, the engineer can write a higher level pseudocode using language constructs specific to his domain which can be transformed into running Python code. 
The application needs syntactic and dependency parsing, used for understanding both the pseudocode and the informal words and transforming them into working python code. 
The tree generated from syntactic and dependency parsing is later used for applying (mapping) functors (represented by predicates) with parameters (represented by words correlated with the predicate) on transformed arguments (subjects on which transformations denoted by their corresponding attributes were applied).


Apply a force of 5 Newtons on a cube of mass 5 at an angle of pi/6 radians for 5 seconds. Check the speed of the cube. ->
```py
cube_mass = 5
force = 5 * cos(math.PI / 6)
acceleration = force / cube_mass 
speed = acceleration * 5
print(speed)
```

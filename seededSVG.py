from qiskit.tools.visualization import plot_histogram
from qiskit import QuantumCircuit, execute, Aer, IBMQ, ClassicalRegister, QuantumRegister
from qiskit.compiler import transpile, assemble
import numpy as np
#from numpy import binary_repr


from qiskit.visualization import *


from numpy import pi
from numpy import sqrt
from numpy import abs

from numpy import round
from numpy import round_

max_distance = 3
grid_size = 10


# Gives us four x,y coordinates and distance/direction for random
seed = input('Provide a string seed of length 8 containing numbers less than '+str(grid_size)+': ')
print("Seed is {}", seed)


xmlDecl = '<?xml version="1.0" standalone="no"?>'
svgOpen = '<svg width="15cm" height="15cm" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg" version="1.1"> '
svgTitle = '  <title>Seed for SVG path was '+seed+'</title> '
svgDescr = '  <desc>A path generated from a seed by a quantum algorithm</desc> '
# svgBorder = ' <rect x="1" y="1" width="1000" height="1000" fill="none" stroke="black" /> '
svgPathStart = '<path d="'
svgPathEnd = '" fill="rgb(255, 158, 44)"  />'

# svgPathEnd = '" fill="rgb(255, 158, 44)" stroke="blue" stroke-width="3" />'

  # <path d="M 100 100 L 300 100 L 200 300 z"
  #       fill="red" stroke="blue" stroke-width="3" />
svgClose = '</svg>'


def svgPath(pathCoords, r=10, g=150, b=44):
    pathDef = ''.join(pathCoords)
    pathString = '<path d="'+pathDef+'" fill="rgb('+str(r)+', '+str(b)+', '+str(b)+')"  /> '
    return pathString

r, g, b = 0, 155, 10


def get_variation(pos, seed=8):
    (x, y) = pos

    # initialize a circuit
    # arbitrarily chosen to have 2 qubits
    qc = QuantumCircuit(2, 2)

    # fill the circuits with gates that depend on x,y and seed
    # (arbitrarily chosen)
    for j in range(seed):
        qc.ry(x * pi / seed, 0)
        qc.ry(y * pi / seed, 1)
        qc.cx(0, 1)

    # put in some measure gates so we can get an output
    qc.measure(0, 0)
    qc.measure(1, 1)

    # run and get the counts dict
    counts = execute(qc, Aer.get_backend('qasm_simulator')).result().get_counts()

    # make sure that every possible outpt has a non-zero entry in the counts dict
    for output in ['00', '10', '11', '01']:
        if output not in counts:
            counts[output] = 1

    # use a couple of these numbers to define the 2D vector
    # (arbitrarily chosen to be the counts for 00 and 11
    # print(counts)
    gradient = [counts['00'], counts['01'],counts['10'], counts['11']]
    # normalize the vector
    length = np.sqrt(gradient[0] ** 2 + gradient[1] ** 2+gradient[2] ** 2 + gradient[3] ** 2)
    gradient = [gradient[0] / length, gradient[1] / length, gradient[2] / length, gradient[3] / length]

    print(gradient)
    # and output it
    return gradient



pathDefArray = []
qPathDefArray = []
qColourArray = []

#Original provided see
isFirst = True
for idx in range(len(seed)):
    if idx % 2 == 0:
        x = int(seed[idx])
        y = int(seed[idx+1])

        if isFirst:
            pathDefArray.append(' M ')
            isFirst = False
        else:
            pathDefArray.append(' L ')

        pathDefArray.append(str(100*x))
        pathDefArray.append(' ')

        pathDefArray.append(str(100*y))
        pathDefArray.append(' ')

        # qColourArray.append(newCoord[1])

def generateQSeededPath(seededPathArr):
    _isFirst = True
    ret_qPathDefArray = []

    for idx in range(len(seededPathArr)):
        if idx % 2 == 0:
            x = int(seededPathArr[idx])
            y = int(seededPathArr[idx + 1])

            if _isFirst:
                ret_qPathDefArray.append(' M ')
                _isFirst = False
            else:
                ret_qPathDefArray.append(' L ')
            # Vary adjacent path
            newCoord = get_variation((x, y))

            randomJiggle = np.random.choice(range(3))
            ret_qPathDefArray.append(str(randomJiggle)+str(1000*round(newCoord[0], 2)))
            ret_qPathDefArray.append(' ')

            ret_qPathDefArray.append(str(1000*round(newCoord[1], 2)))
            ret_qPathDefArray.append(' ')

            qColourArray.append(newCoord[1])
    return ret_qPathDefArray


f= open("qSeededSVG.svg","w+")
f.write(xmlDecl)
f.write(svgOpen)
f.write(svgTitle)
f.write(svgDescr)

f.write('<g>')

for i in range(30):
    colour = list(np.random.choice(range(250), size=3))
    colourR = list(np.random.choice(range(10), size=3))

    f.write(svgPath(generateQSeededPath(seed), colourR[0], colour[1], colour[2]))

f.write('</g>')
f.write(svgClose)
f.close()




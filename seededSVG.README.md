# Procedural generation of SVG paths using quantum circuit

The notebook and application requests an even length string of numbers from the user and converts this to the x, y elements of a path.
Uses the path as a seed which gets passed to a quantum circuit which uses rotation and a controlled not to 
generate new paths.
The resulting paths are used to generate an Scalar Vector Graphics (SVG) file.

The file can be opened in any browser or software supporting the SVG format.

## Technologies used

* Qiskit
* Jupyter notebook
* Python
* Numpy

## Acknowledgments

* This project was developed for "Qiskit Camp Africa" which was held from December 11-14, 2019. We could like to thank the organisers of this event.
* We would like to thank our coach https://github.com/artnas/Python-Map-Generator who provided the inspiration and starting point for this project.
* We would also like to thank Ken Nixon who provided support and direction during the event.

## Background
Qiskit Camps are an immersive experience that consists of training sessions, deep technical talks, and a hackathon alongside the Qiskit core development team. 

https://community.qiskit.org/events/africa/


## Note
This code was rapidly developed as part of a hackathon and could be cleaned up or improved on.

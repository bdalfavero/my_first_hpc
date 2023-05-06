# `my-first-hpc`: A minimal working example of building grid jobs with Docker.

This repo shows how to use Docker to build images that can be run on the nodes of a grid computing setup. Containerization software like Docker or Singularity help make the environment for your programs more portable.

## The simulation

Firstly, let's talk about the simulation itself. For now, we will use SciPy to build a simple simulation of a Lorenz attractor. The point here is just to run Python code in an environment where the proper libraries are installed. To get an idea for how the simulation works, run the shell command `lorenz.py --help`. An example of the simulation input is shown in `input_template.toml` in this repo. Go ahead and run the simulation like you would normally run any Python program. 

## Using Docker

At this point we have a program written in Python. In order to run, it uses various libraries  that are installed on your machine. If you need a package on your local machine, you can just `pip3 install <package name>` at the terminal, and it's ready to use. However, our goal is to run our programs on a remote machine, and we can't be sure whether they have the right packages installed, or if they will even let you install some. In these cases, Docker is very useful. 

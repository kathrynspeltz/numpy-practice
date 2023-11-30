import numpy as np

#### Create an array of 10 zeros 
print(np.zeros(10))


#### Create an array of 10 ones
print(np.ones(10))


#### Create an array of 10 fives
print(np.ones(10) + 4)

#### Create an array of the integers from 10 to 50
print(np.arange(10,51))


#### Create an array of all the even integers from 10 to 50
print(np.arange(10,51,2))


#### Create a 3x3 matrix with values ranging from 0 to 8
print(np.arange(0,9).reshape(3,3))


#### Create a 3x3 identity matrix
print(np.identity(3))


#### Use NumPy to generate a random number between 0 and 1
print(np.random.rand(1))


#### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print(np.random.randn(25))


#### Create the following matrix:
print(np.arange(1,101).reshape(10,10) / 100)


#### Create an array of 20 linearly spaced points between 0 and 1:
print(np.linspace(0,1,20))


#### Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
mat = np.arange(1,26).reshape(5,5)

 
# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
print(mat[2:, 1:])


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
print(mat[3,4])


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
print(mat[0:3, 1:2])

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
print(mat[4,:])

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
print(mat[3:5, :])


#### Get the sum of all the values in mat
print(mat.sum())


#### Get the standard deviation of the values in mat
print(mat.std())


#### Get the sum of all the columns in mat
print(mat.sum(axis=0))

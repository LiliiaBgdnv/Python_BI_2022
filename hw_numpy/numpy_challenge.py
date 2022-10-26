if __name__ == "__main__":
  import numpy as np
  a = np.ones((3, 5))
  b = np.arange(0, 60, 5).reshape(3, 4)
  c = np.random.random((10, 10))

# matrix multiplication
def matrix_multiplication(first_arr, second_arr):
   if first_arr.shape[1] == second_arr.shape[0]:
     return(np.dot(first_arr, second_arr))

# check if it is possible to multiply arrays
def multiplication_check(arr):
  b = np.vectorize(lambda x: x.shape)(np.array(list(map(lambda x: np.array(x), arr))))
  if all(b[0][1:] == b[1][:-1]) == True:
    return True
  else:
    return False

# matrix multiplication from list
def multiply_matrices(arr):
  if multiplication_check(arr) == True:
    for i in range(len(arr)-1):
      a = np.dot(arr[i], arr[i+1])
    return(a)
  else:
    return('None')

# the distance between 2 one-dimensional arrays
def compute_2d_distance(first_arr, second_arr):
  if (len(first_arr.shape) == len(second_arr.shape) == 1) and len(first_arr) == len(second_arr) == 2:
    return(np.linalg.norm(second_arr - first_arr))


# the distance between 2 arrays
def compute_multidimensional_distance(first_arr, second_arr):
  if (len(first_arr.shape) == len(second_arr.shape) == 1) and len(first_arr) == len(second_arr):
    return(np.linalg.norm(second_arr - first_arr))


# matrix of pair distances
def compute_pair_distances(arr):
  return(np.linalg.norm(arr[:, None, :] - arr[None, :, :], axis=-1))

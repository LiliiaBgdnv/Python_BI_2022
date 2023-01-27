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
def multiplication_check(matrices_list):
  combined_array = np.array(list(map(lambda x: np.array(x), matrices_list)))
  shapes_array = np.vectorize(lambda x: x.shape)(combined_array)
  return all(shapes_array[0][1:] == shapes_array[1][:-1])

# matrix multiplication from list
def multiply_matrices(matrices_list):
  if multiplication_check(matrices_list):
    result_matrix = matrices_list[0]
    for i in range(1, len(result_matrix)):
      result_matrix = np.dot(result_matrix, arr[i])
    return a 
  else:
    return None

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

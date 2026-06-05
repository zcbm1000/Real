import numpy as np

# py_list = [1, 2, 3, 4, 5]
# print(f'py_list: {py_list}')              # 구분자 , 있음
# print(f'py_list type: {type(py_list)}')   # class 'list'

# np_arr = np.array(py_list)
# print(f'np_arr: {np_arr}')                # 구분자 , 없음
# print(f'np_arr type: {type(np_arr)}')     # class 'numpy.ndarray


# # n 차원 numpy 배열 생성

# # 2차원

# np_arr = np.array(
#     [
#         [1, 2, 3, 4,5], # 인덱스 번호 0짜리 []
#         [6, 7, 8, 9, 0] # 인덱스 번호 1짜리 []
#     ])

# print(f'np_arr: \n{np_arr}')           
# print(f'np_arr type: {type(np_arr)}') 
# print(np_arr[1][3]) # 인덱스 번호 1에서 3에해당되는 인덱스인 9 가 출력


# for idx, arr in enumerate(np_arr):
#     print(f'idx: {idx}')
#     for num in arr:
#         print(f'num: {num}')


# # 3차원 
# np_arr = np.array(
#     [
#         [
#             [1, 2, 3, 4, 5],
#             [6, 7, 8, 9, 0]
#         ],
#         [
#             [10, 20, 30, 40, 50],
#             [60, 70, 80 ,90, 100]
#         ],
#         [
#         [100, 200, 300, 400, 500],
#         [600, 700, 800 ,900, 1000]
#         ]
#     ]
# )

# for arr1th in np_arr:
#     for arr2th in arr1th:
#         for arr3th in arr2th:
#             print(f'arr3th: {arr3th}')

# # numpy 복사
# np_arr = ([1, 2, 3, 4, 5])
# print(f'np_arr: {np_arr}')
# np_arr_copy = np_arr.copy()        # 깊은 복사
# print(np_arr is np_arr_copy)       # 메모리 주소 비교: False

# # 값 자체를 비교
# print(np.array_equal(np_arr, np_arr_copy)) # 값이 같은지 비교: True

# # 원소(item)마다 비교
# print(np_arr == np_arr_copy)       # 원소(item)마다 비교 [True, True, True, True, True]


# # numpy 배열 연산
# np_arr = np.array([10, 20, 30, 40, 50])
# print(f'np_arr: {np_arr}')
# print(f'np_arr + 10: {np_arr + 10}')
# print(f'np_arr - 10: {np_arr - 10}')
# print(f'np_arr * 10: {np_arr * 10}')
# print(f'np_arr / 10: {np_arr / 10}')
# print(f'np_arr % 10: {np_arr % 10}')
# print(f'np_arr // 10: {np_arr // 10}')

# numpy 배열 속성 확인(속성은 차원이나 갯수가 몇개인지 등등)

# 1. 배열 원소 데이터 타입 설정
# np_arr = np.array([1, 2, 3], dtype = float)   # 타입을 float로 설정
# print(f'np_arr: {np_arr}')                    # 1. 2. 3. 출력

# np_arr = np_arr.astype(np.int64)              # 타입을 정수형으로 설정
# print(f'nP_arr: {np_arr}')                    # 1 2 3 출력
# print(f'np_arr type: {type(np_arr)}')         # class 'numpy.ndarray'

# 2. 배열 속성 확인(차원, 형태, 데이터타입)
# np_arr = np.array(
#     [
#         [1., 2., 3., 4., 5.],
#         [10, 20, 30, 40, 50],
#         [100, 200, 300, 400, 500]
#     ]
# )

# # 배열 차원 확인
# print(f'차원: {np_arr.ndim}')           # ndim 은 차원을 출력 2

# # 배열 형태 확인
# print(f'차원: {np_arr.shape}')          # shape 는 형태를 출력 (3,5) 3행 5열

# # 배열 데이터타입 확인
# print(f'차원: {np_arr.dtype}')          # dtype 은 데이터 타입 출력 float64


# 모든 원소가 x인 배열 만들기
# 1. ones() & oned_like()
# 모든 원소가 1임

np_arr = np.ones((3, 5), dtype=int)
print(f'np_arr: {np_arr}')

py_list = [1, 2, 3]
np_arr = np.ones_like(py_list, dtype=float)
print(f'np_arr: {np_arr}')

py_list = [[1, 2, 3], [4, 5, 6]]
np_arr = np.ones_like(py_list, dtype=float)
print(f'np_arr: {np_arr}')

# 2. zeros() & zero_like()
# 모든 원소가 0임

np_arr = np.zeros((3, 5), dtype = float)      # 원소가 0인 3행 5열짜리 구조 
print(f'np_arr: {np_arr}')

py_list = [1, 2, 3]                           # py_list 는 [1, 2, 3] 이나 
np_arr = np.zeros_like(py_list, dtype = int)  # 모든 원소를 0으로 함 
print(f'np_arrf:{np_arr} ')


py_list = [[1, 2, 3],[4, 5, 6]]
np_arr = np.zeros_like(py_list, dtype = int)
print(f'np_arrf:{np_arr} ')

# 3. empty() & empty_like()
# 모든 원소가 비어있음(그러나 0으로 채워짐)
np_arr = np.empty((3, 5), dtype=int)
print(f'np_arr: {np_arr}')

py_list = [1, 2, 3]
np_arr = np.empty_like(py_list, dtype=int)
print(f'np_arr: {np_arr}')




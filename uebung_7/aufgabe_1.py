def create_square(size):
    assert size >=2, "size must be >=2"   


a=create_square(2)
print(a)
# soll ergeben:
# [[ 1.1. ]
#  [ 1.1. ]]


a=create_square(5)
print(a)
# # soll ergeben:
# [[ 1.1.1.1.1.]
#  [ 1.0.0.0.1.]
#  [ 1.0.0.0.1.] 
#  [ 1.0.0.0.1.]
#  [ 1.1.1.1.1.]]
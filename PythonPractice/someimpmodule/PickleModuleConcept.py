import pickle

'''
The process of preserving any python obj is called as pickling
'''

# Process of Pickling

ll = ["Name1", "Name2", "Name3", "Name3"]
pk_file = "MyObj.pkl"
pk_file_obj = open(pk_file, 'wb')
pickle.dump(ll, pk_file_obj)
pk_file_obj.close()

# Process of De-pickling

pkl_file = "MyObj.pkl"
pkl_file_obj = open(pkl_file, 'rb')
obj = pickle.load(pkl_file_obj)
print(obj)

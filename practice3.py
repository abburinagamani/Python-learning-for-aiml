'''word="python"
print(word[-4:-2])

#normal formatting
a=5
b=7
print("The value of a is {} and b is {}".format(a,b))

#index-based formatting
a=5
b=7
print("The value of a is {0} and b is {1}".format(a,b))

#value-based formatting
print("The value of a is {a} and b is {b}".format(a=3,b=2))

#lists
nums=[1,2,3,4,5]
nums.reverse()
print(nums)

#loops
nums=[1,6,2,5,3,4,2,2]
idx=0
value=5
for i in nums:
    if i==value:
        print("Found value {} at index {}".format(value, idx))
    idx+=1
nums.count(2)
nums.index(5)'''

#dictionaries
info={
    "name":"mani",
    "age":21,
    "cgpa":8.8,
    "city":"mumbai"
}
dict_keys=info.keys()
dict_values=info.values()
dict_items=info.items()
dict_get=info.get("place") #to control the flow of error if we use info["keys"] it gives error
print(dict_get)
info.update({"place":"india"})
print(info)


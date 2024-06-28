#this is a pure function because for an input it will always
#produce the same output. #it also doesnt produce any side effects
#the function does not effect anything outside its scope. 
#note: the print is not a part of the function
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))
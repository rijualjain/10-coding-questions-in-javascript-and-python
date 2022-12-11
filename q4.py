def exercise4(trans,init_state,input_list):
    state = init_state
    output = []
    for i in range(len(input_list)):
        inp = input_list[i]
        key = state + '/' + inp
        value = trans[key]
        state = value.split('/')[0]
        output.append(value.split('/')[1])
    return output
a = {"a/0": "a/1","a/1": "b/0","b/0": "b/0","b/1": "a/1"}
b = 'a'
c = ['0', '0', '1', '1', '0', '0']

print(exercise4(a,b,c))

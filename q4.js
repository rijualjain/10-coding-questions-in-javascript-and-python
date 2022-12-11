function exercise4(trans, init_state, input_list) {
    let state = init_state;
    let output = [];
    for (let i = 0; i < input_list.length; i++) {
      let input = input_list[i];
      let key = state + '/' + input;
      let value = trans[key];
      state = value.split('/')[0];
      output.push(value.split('/')[1]);
    }
      return output;
  }

let a = {"a/0": "a/1","a/1": "b/0","b/0": "b/0","b/1": "a/1"}
let b = 'a'
let c = ['0', '0', '1', '1', '0', '0']

console.log(exercise4(a, b, c))
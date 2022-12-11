function median(n_num){
  let median1 = 0
  let median2 = 0
  let median = 0
    n_num.sort((a,b)=>a-b)
    n = n_num.length
    if (n % 2 == 0){
        median1 = n_num[Math.floor(n/2)]
        median2 = n_num[Math.floor(n/2) - 1]
        median = (median1 + median2)/2
    }
    else{
        median = n_num[Math.floor(n/2)]
    }
    return median
}

function squares(l){
    return l.map(i => i**2)
}

function exercise3(l){
    average = l.reduce((a,b) => a + b)/l.length
    maximum = Math.max(...l)
    med = median(l)
    minimum = Math.min(...l)
    //For the squares
    S_l = squares(l)
    S_average = S_l.reduce((a,b) => a + b)/S_l.length
    S_maximum = Math.max(...S_l)
    console.log(S_l)
    S_med = median(S_l)
    console.log(S_med)
    S_minimum = Math.min(...S_l)
    tuple1 = [minimum,average,med,maximum]
    tuple2 = [S_minimum,S_average,S_med,S_maximum]
    list_of_tuples = [tuple1,tuple2]
    return list_of_tuples
}
const EXERCISE3_TESTS = [
    { input: [[1, 2, 3, 4, 5]]}

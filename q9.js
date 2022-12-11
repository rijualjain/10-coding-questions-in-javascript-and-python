const fs = require('fs');
let words = fs.readFileSync('wordle.txt', 'utf8').split('\n');
function exercise9(green, yellow, gray) {
    let wordle = [];
    for (let i of words) {
        let flag = [...gray].some(j => i.includes(j));
        flag = flag || Object.entries(green).some(([pos, letter]) => i[pos] !== letter);
        flag = flag || Object.entries(yellow).some(([letter, positions]) => [...positions].some(pos => i[pos] === letter) || !i.includes(letter));
        if (!flag) {
            wordle.push(i);
        }
    }
    return wordle.length;
}
const green_2 = {2:'a'}
const yellow_2 = {'a':new Set([3]),'i':new Set([2]),'l':new Set([3,4]),'r':new Set([1])}
const gray_2 = new Set(['e', 't', 'u', 'o', 'p', 'g', 'h', 'c', 'm', 's'])

console.log(exercise9(green_2, yellow_2, gray_2));
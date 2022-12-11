const fs = require('fs');

function getWordles(green, yellow, gray) {
    let words = fs.readFileSync('wordle.txt', 'utf8').split('\n');
    let wordle = [];
    for (let i of words) {
        let flag = [...gray].some(j => i.includes(j));
        flag = flag || Object.entries(green).some(([pos, letter]) => i[pos] !== letter);
        flag = flag || Object.entries(yellow).some(([letter, positions]) => [...positions].some(pos => i[pos] === letter) || !i.includes(letter));
        if (!flag) {
            wordle.push(i);
        }
    }
    return wordle;
}

function exercise10(green, yellow, gray) {
    const wordle = getWordles(green, yellow, gray);
    
    let scores = {};

    for (let v of wordle) {
        scores[v] = 0;
        for (let w of wordle) {
            if (v === w) {
                continue;
            }
            let newGreen = { ...green };
            let newYellow = { ...yellow };
            let newGray = new Set(gray);
            for (let i = 0; i < v.length; i++) {
                let vi = v[i];
                let wi = w[i];
                if (vi === wi) {
                    newGreen[i] = vi;
                }
                else {
                    if (w.includes(vi)) {
                        newYellow[vi] = new Set([...(newYellow[vi] || []), i]);
                    }.
                    else {
                        newGray.add(vi);
                    }
                }
            }
          
            scores[v] += getWordles(newGreen, newYellow, newGray).length;

        }
    }
    console.log(scores)
    return Object.entries(scores).filter(([word, score]) => score === Math.min(...Object.values(scores))).map(([word, score]) => word);
}

const green_1 = { 1: 'i', 3: 'c' }
const yellow_1 = {'e': new Set([3])}
const gray_1 = new Set(['r', 'a', 's', 'd', 'f'])

const green_2 = {2:'a'}
const yellow_2 = {'a':new Set([3]),'i':new Set([2]),'l':new Set([3,4]),'r':new Set([1])}
const gray_2 = new Set(['e', 't', 'u', 'o', 'p', 'g', 'h', 'c', 'm', 's'])
console.log(exercise10(green_1, yellow_1, gray_1));


function exercise8(s) {
    let file = require('fs').readFileSync
    let text = file("wordle.txt", 'utf8')
    let words = text.match(/[a-zA-Z0-9]+/g) || []
    let count = 0
    for (let i = 0; i < words.length; i++) {
        let word = words[i]
        let check = true
        let s_copy = s
        for (let j = 0; j < word.length; j++) {
            let letter = word[j]
            if (s_copy.includes(letter)) {
                s_copy = s_copy.replace(letter, "")
            } else {
                check = false
            }
        }
        if (check) {
            count++
        }
    }
    return count
}

console.log(exercise8("sehuoh"))

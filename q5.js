function exercise5(filename) {
    let file = require('fs').readFileSync
    let text = file(filename, 'utf8')
    let letters = text.match(/[a-zA-Z]/g) || []
    let numbers = text.match(/[0-9]/g) || []
    let symbols = text.match(/[^a-zA-Z0-9\s]/g) || []
    let words = text.match(/[a-zA-Z0-9]+/g) || []
    let sentences = text.match(/[.?!]/g) || []
    let paragraphs = text.match(/\n\n/g) || []
    console.log(symbols)
    return [letters.length, numbers.length, symbols.length, words.length, sentences.length, paragraphs.length + 1]
}


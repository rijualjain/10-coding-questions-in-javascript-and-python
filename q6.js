function exercise6(list) {
    return Array.isArray(list) ? 
    1 + Math.max(0, ...list.map(exercise6)) :
    0;
}

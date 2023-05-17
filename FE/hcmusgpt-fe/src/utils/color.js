function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}
function random_rgba() {
    var o = Math.round, r = Math.random, s = 255, a = getRandomArbitrary(0.2, 1);
    return 'rgba(' + o(r() * s) + ',' + o(r() * s) + ',' + o(r() * s) + ',' + a.toFixed(1) + ')';
}

export default random_rgba;
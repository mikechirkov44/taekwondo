function random(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
  }
  
  function range(cur, next, count) {
    // ищем интервал между промежуточными значениями, если интервал слишком маленький устанавливаем 1
    var diff = Math.floor((next - cur) / count) || 1;
  
    // получаем промежуточные значения
    var res = [cur];
    for (var i = cur + diff; Math.abs(i - next) > Math.abs(diff); i += diff) {
      res.push(i);
    }
    res.push(next);
  
    return res;
  }
  
  var timer = null
  
  function generate(min, max) {
    window.clearInterval(timer);
    var current = +out.value;
    var next = random(min, max);
    var rng = range(current, next, 25);
    timer = setInterval(() => {
      // на каждой итерации берем следующее значение, пока они не закончатся.
      out.value = rng.shift();
      if (!rng.length) window.clearInterval(timer);
    }, 10);
  }
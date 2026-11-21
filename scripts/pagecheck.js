(function(){
  var imgs = document.querySelectorAll('img');
  var out = [];
  for (var i = 0; i < imgs.length; i++) {
    var im = imgs[i];
    out.push({src:(im.currentSrc||im.getAttribute('src')||'').slice(-46), nw:im.naturalWidth, cw:im.clientWidth, ch:im.clientHeight});
  }
  var h1 = document.querySelector('h1[data-split]');
  var words = h1 ? h1.querySelectorAll('.split-word').length : -1;
  var tilt = document.querySelectorAll('.tilt-card').length;
  var stag = document.querySelectorAll('[data-stagger]').length;
  var orb = document.querySelectorAll('.orb-field .orb').length;
  var glow = !!document.getElementById('dq-cursor-glow');
  var fig = document.querySelector('figure.pi-figure');
  var figIn = fig ? fig.className.indexOf('is-inview') >= 0 : false;
  return JSON.stringify({imgs:out, splitWords:words, tilt:tilt, stagger:stag, orbs:orb, glow:glow, figureInview:figIn});
})()

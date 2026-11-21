(function(){
  var imgs = document.querySelectorAll('img');
  var out = [];
  for (var i = 0; i < imgs.length; i++) {
    var im = imgs[i];
    var cs = getComputedStyle(im);
    out.push({
      src: (im.getAttribute('src')||'').slice(0,70),
      complete: im.complete,
      nw: im.naturalWidth,
      cw: im.clientWidth,
      ch: im.clientHeight,
      display: cs.display,
      opacity: cs.opacity
    });
  }
  return JSON.stringify({count: imgs.length, imgs: out});
})()

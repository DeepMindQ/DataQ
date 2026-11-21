#!/bin/bash
# Brand style: deep navy + orange glow, cinematic, no text
STYLE="cinematic premium 3D render, deep dark navy blue environment color 18142D, glowing vivid orange accents color FE5722, volumetric soft lighting, elegant enterprise technology aesthetic, ultra detailed, high quality, no text, no words, no letters, no logos, no people faces"
OUT=/home/z/my-project/site/public/images/gen
gen() { # $1=name $2=prompt
  if [ -s "$OUT/$1.png" ]; then echo "SKIP $1 (exists)"; return; fi
  z-ai image -p "$2, $STYLE" -o "$OUT/$1.png" -s 1344x768 >/dev/null 2>&1 && \
    echo "OK $1 $(stat -c%s "$OUT/$1.png")" || echo "FAIL $1"
}
case "$1" in
svc)
 gen svc-applied-ai "abstract glowing neural network mesh with luminous orange nodes flowing over dark navy glass architecture, depth of field"
 gen svc-agentic "swarm of small glowing orange robotic orbs moving in coordinated formation along illuminated data lanes, dark navy background, motion trails"
 gen svc-data "layered translucent glass data platform strata with streams of orange light cascading between layers, dark navy scene, isometric"
 gen svc-cyber "hexagonal shield lattice with orange radar sweep guarding a glowing core, dark navy cyber defense scene, particles"
 gen svc-cloud "isometric network of glowing edge nodes connected by orange light beams rising into a luminous core, dark navy cloudscape"
 gen svc-quantum "elegant golden-orange quantum orbit rings circling a radiant compute core, dark navy void, fine particle dust"
 gen svc-blockchain "chain of crystalline translucent blocks linked by glowing orange connectors, floating in dark navy space, reflections"
 gen svc-iot "industrial digital twin hologram of a factory floor mirrored above machinery, orange wireframe glow, dark navy ambience"
 ;;
ind)
 gen ind-banking "flowing river of luminous data streams and floating glass panels with rising orange light trails, dark navy financial district abstraction"
 gen ind-health "glowing pulse line traveling through translucent organic network vessels, orange heartbeat glow, dark navy medical technology scene"
 gen ind-retail "isometric retail channels with glowing orange demand curve rising across holographic storefronts, dark navy commerce scene"
 gen ind-manufacturing "vast industrial energy grid with glowing orange power flows connecting factories turbines and control towers, dark navy night scene"
 gen ind-gov "monumental glass dome with governed light arcs connecting service points, orange glow, dark navy civic technology scene"
 gen ind-telecom "planet-wide mesh of glowing orange arcs linking cities across a dark navy globe, luminous network constellation"
 ;;
plat)
 gen plat-nexus "executive decision cockpit hologram, ranked glowing data columns orbiting a central orange intelligence sphere, dark navy"
 gen plat-forge "towering layered platform strata being assembled by streams of orange construction light, dark navy industrial elegance"
 gen plat-swarm "fleet of glowing orange agent vessels flying in precise formation through dark navy clouds, light trails, aerial view"
 gen plat-sentinel "wall of glowing monitoring cells with one alerting orange cell, radar circles, dark navy security operations center"
 gen plat-twinverse "mirror city: photorealistic city and its glowing orange wireframe twin reflection, dark navy, symmetrical composition"
 gen plat-quanta "swirling optimizer vortex of orange schedule ribbons converging to a single bright solution point, dark navy"
 gen plat-ledger "distributed constellation of trust nodes linked by orange verified paths forming a glowing graph, dark navy"
 gen plat-compass "elegant governance compass hologram with orange needle pointing north over layered policy rings, dark navy"
 ;;
co)
 gen co-home "abstract data intelligence field: flowing luminous particles converging into a bright orange horizon over dark navy landscape, cinematic wide"
 gen co-about "warm modern delivery center at dusk, glass building silhouettes with orange interior glow, dark navy sky, abstract no faces"
 gen co-careers "ascending staircase of glowing orange steps rising through dark navy space toward bright light, symbolizing growth"
 gen co-approach "six elegant stone-like slabs floating in sequence connected by orange light path, dark navy, method journey abstraction"
 gen co-contact "glowing orange communication beam rising from a dark navy surface toward a bright convergence point, minimal elegant"
 ;;
esac
echo "DONE $1"

---
layout: null
---
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>12 ANALOGS</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=Special+Elite&family=VT323&family=Cormorant+Garamond:wght@700&family=Press+Start+2P&family=Fredericka+the+Great&family=Bangers&family=Monoton&family=Ewert&family=Playfair+Display:ital@1&family=Shrikhand&family=Abril+Fatface&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      background: #0b0d0f;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: 'Cormorant Garamond', serif;
      padding: 16px;
	  transition: background-color 0.5s ease;
    }
    .clock-container {
      background: #1c1f22;
      padding: 24px 24px 32px;
      border-radius: 56px 56px 32px 32px;
      box-shadow: 0 30px 40px -12px #000000cc, inset 0 1px 3px #ffffff1a;
      border: 1px solid #3f464a;
    }
    canvas {
      display: block;
      margin: 0 auto;
      width: min(75vw, 75vh, 660px);
      height: min(75vw, 75vh, 660px);
      border-radius: 50%;
      box-shadow: 0 0 0 3px #2e3438, 0 22px 40px -6px black, inset 0 6px 8px #0000004d;
      cursor: crosshair;
    }
    .legend {
      margin-top: 20px;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 8px 16px;
      font-size: 0.75rem;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: #b9b3a6;
      border-top: 1px dashed #5a6064;
      padding-top: 20px;
      font-family: 'Special Elite', monospace;
    }
    .legend span {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: #21262a;
      padding: 4px 12px;
      border-radius: 40px;
      border-left: 8px solid;
      box-shadow: inset 0 1px 3px #0b0d0e;
      font-weight: bold;
      color: #e6ddd0;
    }
    .legend .s0 { border-left-color: #a0988c; } .legend .s1 { border-left-color: #d4af37; }
    .legend .s2 { border-left-color: #6fbf4c; } .legend .s3 { border-left-color: #a52a5e; }
    .legend .s4 { border-left-color: #1e3a8a; } .legend .s5 { border-left-color: #f4e9d8; }
    .legend .s6 { border-left-color: #b8860b; } .legend .s7 { border-left-color: #ff69b4; }
    .legend .s8 { border-left-color: #00ffff; } .legend .s9 { border-left-color: #f7c8d6; }
    .legend .s10 { border-left-color: #7f8c8d; } .legend .s11 { border-left-color: #cd7f32; }
    .time-digital {
      text-align: right;
      font-family: 'VT323', monospace;
      font-size: 1.8rem;
      margin-top: 10px;
      color: #c9bcab;
      letter-spacing: 6px;
      text-shadow: 0 0 6px #2f5575;
    }
    .footnote {
      font-family: 'Cinzel', serif;
      font-size: 0.7rem;
      color: #6e767b;
      margin-top: 6px;
      text-align: center;
    }
    .progress-badge {
      background: #2a3036;
      color: #c9bcab;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.8rem;
      margin-left: 8px;
    }
	
	.control-panel {
  margin-top: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  flex-wrap: wrap;
  color: #b9b3a6;
  font-family: 'Special Elite', monospace;
}
.control-panel input[type=range] {
  width: 80px;
  cursor: pointer;
}
.control-panel button {
  background: #2a3036;
  color: #e6ddd0;
  border: 1px solid #5a6064;
  padding: 6px 14px;
  border-radius: 30px;
  font-family: inherit;
  font-size: 0.8rem;
  cursor: pointer;
  transition: 0.2s;
}
.control-panel button:hover {
  background: #3f464a;
}

  </style>
</head>
<body>
<div class="clock-container">
  <canvas id="clockCanvas" width="800" height="800"></canvas>
  <div class="time-digital" id="digitalDisplay">--:--:--</div>
  <div class="legend">
    <span class="s0">⓪ brutalist ★</span> <span class="s1">① gear/engine</span> <span class="s2">② pixel retro</span>
    <span class="s3">③ organic</span> <span class="s4">④ maximal chaos</span> <span class="s5">⑤ cyber-lines</span>
    <span class="s6">⑥ fire field</span> <span class="s7">⑦ light/dark minimal</span> <span class="s8">⑧ bubble fantasy</span>
    <span class="s9">⑨ balloon sky</span> <span class="s10">⑩ crescent starry</span> <span class="s11">⑪ chronos brass</span>
    <span class="progress-badge">★COMPLETED★</span>
  </div>
  <div class="footnote">12 ANALOG</div>
</div>

<div class="control-panel">
  <label style="color:#ccc; margin-right:10px;">UI背景色</label>
  <input type="range" id="bgR" min="0" max="255" value="28"> R
  <input type="range" id="bgG" min="0" max="255" value="31"> G
  <input type="range" id="bgB" min="0" max="255" value="34"> B
  <button id="toggleBodyBg">⏸ 背景自動変化を停止</button>
</div>

<script>
  (function(){
    "use strict";

    const canvas = document.getElementById('clockCanvas');
    const ctx = canvas.getContext('2d');
    const digitalEl = document.getElementById('digitalDisplay');

    const SIZE = 800;
    canvas.width = SIZE;
    canvas.height = SIZE;
    const CX = SIZE/2, CY = SIZE/2;
    const R = SIZE * 0.43;
	// オフスクリーンCanvas（背景専用）
	const bgCanvas = document.createElement('canvas');
	bgCanvas.width = SIZE;
	bgCanvas.height = SIZE;
	const bgCtx = bgCanvas.getContext('2d');

let lastBackgroundUpdate = 0;
let enableBodyBgAutoChange = true;  // 自動変化の有効/無効
const BACKGROUND_INTERVAL = 1000; // ミリ秒（1秒ごとに背景更新）
    const IR = SIZE * 0.14;
	
	// テーマ別外部背景色
const themeBgColors = [
  '#DCE0E8', // 0: brutalist
  '#8F8F8F', // 1: gear/engine
  '#49C949', // 2: pixel retro
  '#00A100', // 3: organic
  '#DA6FF2', // 4: maximal chaos
  '#1E2EBD', // 5: cyber-lines
  '#D61111', // 6: fire field
  '#F5F1ED', // 7: light/dark minimal
  '#3874CF', // 8: bubble fantasy
  '#4A90D9', // 9: balloon sky
  '#FFE53D', // 10: crescent starry
  '#B59A22'  // 11: chronos brass
];

// 現在の針テーマ（ランダムに決定）
let currentHandTheme = 0;
const handThemes = [
  { hour: '#5d4e3c', min: '#b8860b', sec: '#d4af37', shadow: '#3a281f' }, // gear
  { hour: '#1f2c3d', min: '#0ff', sec: '#ff44cc', shadow: '#0ff' },        // cyber
  { hour: '#8b0000', min: '#ff4500', sec: '#ffd700', shadow: '#ff8c00' },  // fire
  { hour: '#3f6792', min: '#a35d8e', sec: '#e3b3c9', shadow: '#b380aa' },  // bubble
  { hour: '#2e4c6b', min: '#e06767', sec: '#87CEEB', shadow: '#b0d0e8' },  // balloon
  { hour: '#1e2f4b', min: '#f9f3c1', sec: '#e0e7ff', shadow: '#b7b7d9' },  // starry
  { hour: '#5c4033', min: '#cdb38c', sec: '#f5e6c4', shadow: '#a67c45' },  // brass
  { hour: '#111', min: '#333', sec: '#666', shadow: '#aaa' }               // minimal
];

    const SECTORS = [];
    for (let i=0; i<12; i++) {
      const start = (i * 30 - 90) * Math.PI/180;
      const end = ((i+1) * 30 - 90) * Math.PI/180;
      SECTORS.push({ start, end, idx: i });
    }

    function clipSector(idx) {
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R, SECTORS[idx].start, SECTORS[idx].end);
      ctx.closePath();
      ctx.clip();
    }

    // ========== セクション0: ブルータリスト空間 ==========
    function drawBrutalistSpace(ctx) {
      // 1. 背景（コンクリート調）
      ctx.fillStyle = '#8a9299';
      ctx.fillRect(CX-R, CY-R, R*2, R*2);
      
      // 2. 扇形クリッピング
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[0].start, SECTORS[0].end);
      ctx.closePath();
      ctx.clip();

      ctx.fillStyle = '#8a9299';
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      // 3. コンクリートのテクスチャ（微細な斑点）
      ctx.fillStyle = '#6a7278';
      ctx.globalAlpha = 0.15;
      for (let i=0; i<40; i++) {
        ctx.beginPath();
        ctx.arc(CX-R*0.1 + Math.random()*R*1.2, CY-R*0.1 + Math.random()*R*1.2, 2+Math.random()*6, 0, 2*Math.PI);
        ctx.fill();
      }
      ctx.globalAlpha = 1.0;

      // 4. 幾何学的な柱（縦長ブロック）
      ctx.fillStyle = '#4a5056';
      ctx.shadowColor = '#1a1c1e';
      ctx.shadowBlur = 8;
      for (let i=0; i<12; i++) {
        const x = CX + R*0.2 + i * 18;
        ctx.fillRect(x, CY-R*0.4, 6, R*0.7);
      }
      
      // 横梁
      ctx.fillStyle = '#3a4046';
      ctx.fillRect(CX+R*0.25, CY-R*0.1, R*0.6, 8);
      ctx.fillRect(CX+R*0.2, CY+R*0.15, R*0.7, 6);

      // 5. テキスト
      ctx.font = "bold 28px 'Special Elite', monospace";
      ctx.fillStyle = '#14171a';
      ctx.shadowBlur = 4;
      ctx.fillText("RAW", CX+R*0.45, CY-R*0.1);
      
      ctx.font = "18px 'Special Elite', monospace";
      ctx.fillStyle = '#2a3036';
      ctx.fillText("BRUT", CX+R*0.5, CY+R*0.3);
      
      ctx.shadowBlur = 0;
      ctx.restore();
    }
	    // ========== セクション1: 高密度歯車エンジン空間 ==========
function drawGear(targetCtx, gx, gy, outerR, innerR, teethCount, colorLight, colorDark, holeR = null) {
  if (holeR === null) holeR = innerR * 0.3;
  const midR = outerR - 8;
  if (midR <= 0) return;
  
  targetCtx.save();
  targetCtx.translate(gx, gy);
  
  targetCtx.beginPath();
  targetCtx.lineJoin = "bevel";
  const numPoints = teethCount * 2;
  for (let n = 0; n < numPoints; n++) {
    const radius = (n % 2 === 0) ? outerR : innerR;
    const theta = ((Math.PI * 2) / numPoints) * (n + 1);
    const x = radius * Math.sin(theta);
    const y = radius * Math.cos(theta);
    if (n === 0) targetCtx.moveTo(x, y);
    else targetCtx.lineTo(x, y);
  }
  targetCtx.closePath();
  
  const grad = targetCtx.createLinearGradient(-outerR/2, -outerR/2, outerR/2, outerR/2);
  grad.addColorStop(0, colorLight);
  grad.addColorStop(1, colorDark);
  targetCtx.fillStyle = grad;
  targetCtx.shadowColor = '#2a1e0e'; targetCtx.shadowBlur = 8;
  targetCtx.fill();
  targetCtx.strokeStyle = '#3d2e1e'; targetCtx.lineWidth = 2.5; targetCtx.stroke();
  
  targetCtx.beginPath();
  targetCtx.arc(0, 0, midR, 0, 2 * Math.PI);
  const grad2 = targetCtx.createRadialGradient(-midR*0.3, -midR*0.3, 2, 0, 0, midR);
  grad2.addColorStop(0, colorLight);
  grad2.addColorStop(1, colorDark);
  targetCtx.fillStyle = grad2;
  targetCtx.fill();
  targetCtx.strokeStyle = '#4a3828'; targetCtx.lineWidth = 2; targetCtx.stroke();
  
  targetCtx.beginPath();
  targetCtx.arc(0, 0, holeR, 0, 2 * Math.PI);
  targetCtx.fillStyle = '#1a1510';
  targetCtx.shadowBlur = 6; targetCtx.shadowColor = '#000';
  targetCtx.fill();
  targetCtx.strokeStyle = '#8b7355'; targetCtx.lineWidth = 1.5; targetCtx.stroke();
  
  targetCtx.shadowBlur = 0;
  targetCtx.restore();
}

    function drawGearEngineSpace(ctx) {
      const grad = ctx.createRadialGradient(CX-30, CY-20, 10, CX, CY, R);
      grad.addColorStop(0, '#2a2a2a');
      grad.addColorStop(0.7, '#1a1510');
      grad.addColorStop(1, '#0d0a07');
      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);
      
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[1].start, SECTORS[1].end);
      ctx.closePath();
      ctx.clip();
      
      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);
      
      ctx.fillStyle = '#3a2e24';
      ctx.globalAlpha = 0.2;
      for (let i=0; i<30; i++) {
        ctx.beginPath();
        ctx.ellipse(CX+R*0.1 + Math.random()*R*0.8, CY-R*0.1 + Math.random()*R*0.7, 15, 8, 0, 0, 2*Math.PI);
        ctx.fill();
      }
      ctx.globalAlpha = 1.0;
      
      for (let g = 0; g < 50; g++) {
        const angle = SECTORS[1].start + Math.random() * (SECTORS[1].end - SECTORS[1].start);
        const dist = R * 0.2 + Math.random() * (R * 0.7);
        const gx = CX + Math.cos(angle) * dist;
        const gy = CY + Math.sin(angle) * dist;
        
        const sizeFactor = 0.4 + Math.random() * 0.8;
        const outerR = 20 * sizeFactor;
        const innerR = outerR * 0.6;
        const teeth = 6 + Math.floor(Math.random() * 6);
        
        const hue = 30 + Math.random() * 20;
        const lightColor = `hsl(${hue}, 50%, 65%)`;
        const darkColor = `hsl(${hue}, 60%, 30%)`;
        
drawGear(ctx, gx, gy, outerR, innerR, teeth, lightColor, darkColor);
      }
      
      for (let g = 0; g < 30; g++) {
        const angle = SECTORS[1].start + Math.random() * (SECTORS[1].end - SECTORS[1].start);
        const dist = R * 0.1 + Math.random() * (R * 0.8);
        const gx = CX + Math.cos(angle) * dist;
        const gy = CY + Math.sin(angle) * dist;
        
        const outerR = 12 * (0.5 + Math.random() * 0.6);
        const innerR = outerR * 0.6;
        const teeth = 5 + Math.floor(Math.random() * 5);
        
        const hue = 25 + Math.random() * 30;
        const lightColor = `hsl(${hue}, 55%, 70%)`;
        const darkColor = `hsl(${hue}, 65%, 25%)`;
        
drawGear(ctx, gx, gy, outerR, innerR, teeth, lightColor, darkColor);
      }
      
      ctx.font = "bold 18px 'Cinzel', serif";
      ctx.fillStyle = '#d4af37';
      ctx.shadowColor = '#3a281f'; ctx.shadowBlur = 8;
      ctx.fillText("GEAR", CX+R*0.45, CY-R*0.25);
      ctx.shadowBlur = 0;
      
      ctx.restore();
    }
	
	    // ========== セクション2: ピクセルレトロ空間 ==========
    function drawPixelSword(ctx, x, y, size, color) {
      ctx.fillStyle = color;
      const s = size;
      ctx.fillRect(x - s*0.5, y - s*3, s, s*3);
      ctx.fillRect(x - s, y - s, s*2, s);
      ctx.fillRect(x - s*0.5, y, s, s*2);
      ctx.fillStyle = '#c0c0c0';
      ctx.fillRect(x - s*0.5, y - s*2.5, s*0.5, s*2);
    }

    function drawPixelShield(ctx, x, y, size, color) {
      ctx.fillStyle = color;
      const s = size;
      ctx.beginPath();
      ctx.moveTo(x, y - s*2);
      ctx.lineTo(x + s*1.5, y - s);
      ctx.lineTo(x + s*1.5, y + s);
      ctx.lineTo(x, y + s*2);
      ctx.lineTo(x - s*1.5, y + s);
      ctx.lineTo(x - s*1.5, y - s);
      ctx.closePath();
      ctx.fill();
      ctx.fillStyle = '#ffffff';
      ctx.beginPath();
      ctx.arc(x, y, s*0.8, 0, 2 * Math.PI);
      ctx.fill();
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.arc(x, y, s*0.4, 0, 2 * Math.PI);
      ctx.fill();
    }

    function drawPixelHeart(ctx, x, y, size, color) {
      ctx.fillStyle = color;
      const s = size;
      ctx.fillRect(x - s*1.5, y - s, s, s*2);
      ctx.fillRect(x + s*0.5, y - s, s, s*2);
      ctx.fillRect(x - s*2.5, y - s*0.5, s, s);
      ctx.fillRect(x + s*1.5, y - s*0.5, s, s);
      ctx.fillRect(x - s*1.5, y, s*3, s);
      ctx.fillRect(x - s*0.5, y + s, s, s);
    }

    function drawPixelStar(ctx, x, y, size, color) {
      ctx.fillStyle = color;
      const s = size;
      ctx.fillRect(x - s*0.5, y - s*2, s, s*4);
      ctx.fillRect(x - s*2, y - s*0.5, s*4, s);
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(45 * Math.PI/180);
      ctx.fillRect(-s*1.5, -s*0.5, s*3, s);
      ctx.rotate(-90 * Math.PI/180);
      ctx.fillRect(-s*1.5, -s*0.5, s*3, s);
      ctx.restore();
    }

    function drawPixelInvader(ctx, x, y, size, color) {
      ctx.fillStyle = color;
      const s = size;
      ctx.fillRect(x - s*2, y - s*2, s, s);
      ctx.fillRect(x + s, y - s*2, s, s);
      ctx.fillRect(x - s*1.5, y - s, s*3, s*2);
      ctx.fillStyle = '#000000';
      ctx.fillRect(x - s*0.5, y, s*0.8, s*0.8);
      ctx.fillStyle = color;
      ctx.fillRect(x - s*1, y + s, s*2, s*2);
      ctx.fillRect(x - s*1.5, y + s*2, s, s);
      ctx.fillRect(x + s*0.5, y + s*2, s, s);
    }

    function drawPixelBlock(ctx, x, y, size, color) {
      ctx.fillStyle = color;
      ctx.fillRect(x - size, y - size, size*2, size*2);
    }

    function drawPixelRetroSpace(ctx) {
      ctx.fillStyle = '#1e3a1e';
      ctx.fillRect(CX-R, CY-R, R*2, R*2);
      
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[2].start, SECTORS[2].end);
      ctx.closePath();
      ctx.clip();
      
      ctx.fillStyle = '#1e3a1e';
      ctx.fillRect(CX-R, CY-R, R*2, R*2);
      
      ctx.strokeStyle = '#6fbf4c';
      ctx.lineWidth = 1;
      ctx.globalAlpha = 0.15;
      const gridSize = 20;
      for (let i = 0; i < R*2; i += gridSize) {
        ctx.beginPath();
        ctx.moveTo(CX-R + i, CY-R);
        ctx.lineTo(CX-R + i, CY+R);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(CX-R, CY-R + i);
        ctx.lineTo(CX+R, CY-R + i);
        ctx.stroke();
      }
      ctx.globalAlpha = 1.0;
      
      for (let i = 0; i < 35; i++) {
        const angle = SECTORS[2].start + Math.random() * (SECTORS[2].end - SECTORS[2].start);
        const dist = R * 0.2 + Math.random() * (R * 0.7);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        
        const elementType = Math.floor(Math.random() * 5);
        const pixelSize = 4 + Math.floor(Math.random() * 6);
        const hue = Math.floor(Math.random() * 360);
        const color = `hsl(${hue}, 80%, 60%)`;
        
        switch (elementType) {
          case 0: drawPixelSword(ctx, px, py, pixelSize, color); break;
          case 1: drawPixelShield(ctx, px, py, pixelSize, color); break;
          case 2: drawPixelHeart(ctx, px, py, pixelSize, color); break;
          case 3: drawPixelStar(ctx, px, py, pixelSize, color); break;
          case 4: drawPixelInvader(ctx, px, py, pixelSize, color); break;
          case 5: drawPixelBlock(ctx, px, py, pixelSize, color); break;
        }
      }
      
      for (let i = 0; i < 20; i++) {
        const angle = SECTORS[2].start + Math.random() * (SECTORS[2].end - SECTORS[2].start);
        const dist = R * 0.15 + Math.random() * (R * 0.75);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        drawPixelBlock(ctx, px, py, 2 + Math.random()*4, `hsl(${Math.random()*360}, 70%, 55%)`);
      }

      ctx.font = "bold 18px 'Press Start 2P', cursive";
      ctx.fillStyle = '#f8f0d0';
      ctx.shadowColor = '#6fbf4c'; ctx.shadowBlur = 8;
      ctx.fillText("8-BIT", CX+R*0.3, CY-R*0.25);
      ctx.font = "12px 'Press Start 2P', cursive";
      ctx.fillText("RETRO", CX+R*0.45, CY-R*0.1);
      ctx.shadowBlur = 0;
      
      ctx.restore();
    }
	
	    // ========== セクション3: オーガニック空間 ==========
    function drawBlob(ctx, x, y, size, colorLight, colorDark) {
      ctx.save();
      ctx.translate(x, y);
      const points = 5 + Math.floor(Math.random() * 4);
      const grad = ctx.createRadialGradient(-size*0.2, -size*0.2, 2, 0, 0, size);
      grad.addColorStop(0, colorLight);
      grad.addColorStop(1, colorDark);
      ctx.fillStyle = grad;
      ctx.beginPath();
      for (let i = 0; i < points; i++) {
        const angle = (i / points) * Math.PI * 2 + Math.random() * 0.3;
        const radius = size * (0.7 + Math.random() * 0.5);
        const px = Math.cos(angle) * radius;
        const py = Math.sin(angle) * radius;
        if (i === 0) ctx.moveTo(px, py);
        else ctx.quadraticCurveTo(Math.cos(angle - 0.5) * radius * 1.3, Math.sin(angle - 0.5) * radius * 1.3, px, py);
      }
      ctx.closePath();
      ctx.shadowColor = '#2a4a2a'; ctx.shadowBlur = 8;
      ctx.fill();
      ctx.strokeStyle = '#4a6a4a'; ctx.lineWidth = 1.5; ctx.stroke();
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawLeaf(ctx, x, y, size, hue) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(Math.random() * Math.PI * 2);
      const grad = ctx.createLinearGradient(-size*0.5, -size*0.5, size*0.5, size*0.5);
      grad.addColorStop(0, `hsl(${hue}, 70%, 50%)`);
      grad.addColorStop(1, `hsl(${hue}, 80%, 30%)`);
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.moveTo(0, -size);
      ctx.quadraticCurveTo(size*0.7, -size*0.3, size*0.3, size*0.8);
      ctx.quadraticCurveTo(0, size*0.2, -size*0.3, size*0.8);
      ctx.quadraticCurveTo(-size*0.7, -size*0.3, 0, -size);
      ctx.fill();
      ctx.strokeStyle = `hsl(${hue}, 60%, 25%)`; ctx.lineWidth = 1.5; ctx.stroke();
      ctx.beginPath();
      ctx.strokeStyle = `hsl(${hue}, 50%, 35%)`; ctx.lineWidth = 1.2;
      ctx.moveTo(0, -size*0.8); ctx.lineTo(0, size*0.7); ctx.stroke();
      for (let i=1; i<4; i++) {
        const yPos = -size*0.5 + i * size*0.3;
        ctx.beginPath();
        ctx.moveTo(0, yPos); ctx.lineTo(size*0.3, yPos - size*0.1); ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(0, yPos); ctx.lineTo(-size*0.3, yPos - size*0.1); ctx.stroke();
      }
      ctx.restore();
    }

    function drawSpiral(ctx, x, y, size, hue) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(Math.random() * Math.PI * 2);
      ctx.beginPath();
      ctx.strokeStyle = `hsl(${hue}, 70%, 45%)`;
      ctx.lineWidth = size * 0.25;
      ctx.lineCap = 'round';
      let angle = 0, radius = size * 0.8;
      ctx.moveTo(0, 0);
      for (let i=0; i<20; i++) {
        angle += 0.5; radius *= 0.9;
        ctx.lineTo(Math.cos(angle) * radius * 0.5, Math.sin(angle) * radius * 0.5);
      }
      ctx.stroke();
      ctx.beginPath();
      ctx.fillStyle = `hsl(${hue}, 80%, 55%)`;
      ctx.arc(0, 0, size*0.3, 0, 2*Math.PI);
      ctx.fill();
      ctx.restore();
    }

    function drawAmoeba(ctx, x, y, size, hue) {
      ctx.save();
      ctx.translate(x, y);
      const grad = ctx.createRadialGradient(-size*0.3, -size*0.2, 2, 0, 0, size*1.2);
      grad.addColorStop(0, `hsl(${hue}, 60%, 60%)`);
      grad.addColorStop(1, `hsl(${hue}, 70%, 35%)`);
      ctx.fillStyle = grad;
      ctx.beginPath();
      const lobes = 3 + Math.floor(Math.random() * 3);
      for (let i=0; i<lobes; i++) {
        const angle = (i / lobes) * Math.PI * 2;
        const lobeSize = size * (0.6 + Math.random() * 0.5);
        const px = Math.cos(angle) * lobeSize;
        const py = Math.sin(angle) * lobeSize;
        if (i===0) ctx.moveTo(px, py);
        else ctx.quadraticCurveTo(Math.cos(angle - 0.6) * size * 0.8, Math.sin(angle - 0.6) * size * 0.8, px, py);
      }
      ctx.closePath();
      ctx.shadowColor = '#2a3a1a'; ctx.shadowBlur = 6;
      ctx.fill();
      ctx.strokeStyle = `hsl(${hue}, 60%, 25%)`; ctx.lineWidth = 1.5; ctx.stroke();
      ctx.shadowBlur = 0;
      ctx.beginPath();
      ctx.fillStyle = `hsl(${hue}, 50%, 50%)`;
      ctx.arc(size*0.2, -size*0.1, size*0.2, 0, 2*Math.PI);
      ctx.fill();
      ctx.restore();
    }

    function drawVine(ctx, x, y, size, hue) {
      ctx.save();
      ctx.translate(x, y);
      ctx.beginPath();
      ctx.strokeStyle = `hsl(${hue}, 60%, 40%)`;
      ctx.lineWidth = size * 0.2;
      ctx.lineCap = 'round';
      let px = 0, py = 0;
      ctx.moveTo(0, 0);
      for (let i=0; i<8; i++) {
        const angle = i * 0.8 + Math.sin(i) * 0.5;
        const dist = size * (0.8 + i * 0.3);
        px = Math.cos(angle) * dist; py = Math.sin(angle) * dist;
        ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.fillStyle = `hsl(${hue}, 70%, 50%)`;
      for (let i=2; i<7; i+=2) {
        const angle = i * 0.8 + Math.sin(i) * 0.5;
        const dist = size * (0.8 + i * 0.3);
        const lx = Math.cos(angle) * dist;
        const ly = Math.sin(angle) * dist;
        ctx.beginPath();
        ctx.ellipse(lx + Math.cos(angle+1.5)*size*0.4, ly + Math.sin(angle+1.5)*size*0.4, size*0.25, size*0.15, angle+0.5, 0, 2*Math.PI);
        ctx.fill();
        ctx.beginPath();
        ctx.ellipse(lx + Math.cos(angle-1.5)*size*0.4, ly + Math.sin(angle-1.5)*size*0.4, size*0.25, size*0.15, angle-0.5, 0, 2*Math.PI);
        ctx.fill();
      }
      ctx.restore();
    }

    function drawSpore(ctx, x, y, size, hue) {
      ctx.save();
      ctx.translate(x, y);
      const grad = ctx.createRadialGradient(-size*0.2, -size*0.2, 1, 0, 0, size);
      grad.addColorStop(0, `hsl(${hue}, 80%, 70%)`);
      grad.addColorStop(1, `hsl(${hue}, 70%, 40%)`);
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.ellipse(0, 0, size, size*0.8, 0, 0, 2*Math.PI);
      ctx.fill();
      ctx.strokeStyle = `hsl(${hue}, 60%, 30%)`; ctx.lineWidth = 1; ctx.stroke();
      ctx.beginPath();
      ctx.strokeStyle = `hsl(${hue}, 50%, 50%)`; ctx.lineWidth = 0.8;
      ctx.ellipse(-size*0.2, -size*0.1, size*0.3, size*0.2, 0, 0, 2*Math.PI);
      ctx.stroke();
      ctx.restore();
    }

    function drawRipple(ctx, x, y, size, hue) {
      ctx.save();
      ctx.translate(x, y);
      ctx.strokeStyle = `hsl(${hue}, 50%, 55%)`;
      ctx.lineWidth = size * 0.15;
      ctx.globalAlpha = 0.7;
      for (let i=1; i<=4; i++) {
        ctx.beginPath();
        ctx.ellipse(0, 0, size * i * 0.5, size * i * 0.4, 0, 0, 2*Math.PI);
        ctx.stroke();
      }
      ctx.globalAlpha = 1.0;
      ctx.beginPath();
      ctx.fillStyle = `hsl(${hue}, 60%, 45%)`;
      ctx.arc(0, 0, size*0.3, 0, 2*Math.PI);
      ctx.fill();
      ctx.restore();
    }

    function drawMoss(ctx, x, y, size, hue) {
      ctx.save();
      ctx.translate(x, y);
      for (let i=0; i<8; i++) {
        const angle = (i / 8) * Math.PI * 2;
        const dist = size * 0.5;
        const mx = Math.cos(angle) * dist;
        const my = Math.sin(angle) * dist;
        const grad = ctx.createRadialGradient(mx-size*0.1, my-size*0.1, 1, mx, my, size*0.4);
        grad.addColorStop(0, `hsl(${hue}, 80%, 65%)`);
        grad.addColorStop(1, `hsl(${hue}, 70%, 35%)`);
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.ellipse(mx, my, size*0.35, size*0.25, angle, 0, 2*Math.PI);
        ctx.fill();
      }
      ctx.beginPath();
      ctx.fillStyle = `hsl(${hue}, 60%, 45%)`;
      ctx.arc(0, 0, size*0.2, 0, 2*Math.PI);
      ctx.fill();
      ctx.restore();
    }

    function drawOrganicSpace(ctx) {
      const grad = ctx.createRadialGradient(CX-20, CY-15, 10, CX, CY, R);
      grad.addColorStop(0, '#2a4a2a');
      grad.addColorStop(0.6, '#1a3a1a');
      grad.addColorStop(1, '#0a1a0a');
      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);
      
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[3].start, SECTORS[3].end);
      ctx.closePath();
      ctx.clip();
      
      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);
      
      ctx.fillStyle = '#3a5a3a';
      ctx.globalAlpha = 0.15;
      for (let i=0; i<40; i++) {
        ctx.beginPath();
        ctx.ellipse(CX+R*0.1 + Math.random()*R*0.8, CY-R*0.1 + Math.random()*R*0.7, 12, 6, 0, 0, 2*Math.PI);
        ctx.fill();
      }
      ctx.globalAlpha = 1.0;
      
      for (let i = 0; i < 32; i++) {
        const angle = SECTORS[3].start + Math.random() * (SECTORS[3].end - SECTORS[3].start);
        const dist = R * 0.15 + Math.random() * (R * 0.75);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        
        const shapeType = Math.floor(Math.random() * 8);
        const sizeBase = 12 + Math.random() * 25;
        const hue = 80 + Math.floor(Math.random() * 60);
        
        switch (shapeType) {
          case 0: drawBlob(ctx, px, py, sizeBase, `hsl(${hue}, 70%, 60%)`, `hsl(${hue}, 80%, 30%)`); break;
          case 1: drawLeaf(ctx, px, py, sizeBase, hue); break;
          case 2: drawSpiral(ctx, px, py, sizeBase*0.8, hue); break;
          case 3: drawAmoeba(ctx, px, py, sizeBase, hue); break;
          case 4: drawVine(ctx, px, py, sizeBase*1.2, hue); break;
          case 5: drawSpore(ctx, px, py, sizeBase*0.6, hue); break;
          case 6: drawRipple(ctx, px, py, sizeBase*0.9, hue); break;
          case 7: drawMoss(ctx, px, py, sizeBase*0.7, hue); break;
        }
      }
      
      for (let i = 0; i < 15; i++) {
        const angle = SECTORS[3].start + Math.random() * (SECTORS[3].end - SECTORS[3].start);
        const dist = R * 0.1 + Math.random() * (R * 0.8);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        drawSpore(ctx, px, py, 5 + Math.random()*10, 70 + Math.random()*50);
      }
      
      ctx.font = "bold 28px 'Fredericka the Great', cursive";
      ctx.fillStyle = '#c7e0b0';
      ctx.shadowColor = '#1a3a1a'; ctx.shadowBlur = 12;
      ctx.fillText("wild", CX+R*0.3, CY-R*0.3);
      ctx.shadowBlur = 0;
      
      ctx.restore();
    }
    // ========== セクション4: マキシマルカオス空間 ==========
    function drawChaosCircle(ctx, x, y, size, color, alpha) {
      ctx.save();
      ctx.translate(x, y);
      ctx.globalAlpha = alpha;
      const grad = ctx.createRadialGradient(-size*0.2, -size*0.2, 2, 0, 0, size);
      grad.addColorStop(0, color);
      grad.addColorStop(1, `hsl(${color.match(/hsl\((\d+)/)[1]}, 70%, 35%)`);
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(0, 0, size, 0, 2*Math.PI);
      ctx.fill();
      ctx.strokeStyle = '#fff'; ctx.lineWidth = 1.5; ctx.stroke();
      ctx.restore();
    }

    function drawChaosSquare(ctx, x, y, size, color, alpha) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(Math.random() * Math.PI);
      ctx.globalAlpha = alpha;
      ctx.fillStyle = color;
      ctx.fillRect(-size, -size, size*2, size*2);
      ctx.strokeStyle = '#000'; ctx.lineWidth = 2; ctx.strokeRect(-size, -size, size*2, size*2);
      ctx.restore();
    }

    function drawChaosPolygon(ctx, x, y, size, sides, color, alpha, filled=true) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(Math.random() * Math.PI);
      ctx.globalAlpha = alpha;
      ctx.beginPath();
      for (let i=0; i<sides; i++) {
        const angle = (i / sides) * Math.PI * 2 - Math.PI/2;
        const px = Math.cos(angle) * size;
        const py = Math.sin(angle) * size;
        if (i===0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.closePath();
      if (filled) { ctx.fillStyle = color; ctx.fill(); }
      ctx.strokeStyle = filled ? '#fff' : '#000'; ctx.lineWidth = filled ? 1.5 : 2.5;
      ctx.stroke();
      ctx.restore();
    }

    function drawChaosCurve(ctx, x, y, size, color, alpha) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(Math.random() * Math.PI);
      ctx.globalAlpha = alpha;
      ctx.beginPath();
      ctx.moveTo(-size*1.2, size*0.5);
      ctx.bezierCurveTo(-size*0.5, -size*1.2, size*0.5, size*1.2, size*1.2, -size*0.5);
      ctx.strokeStyle = color; ctx.lineWidth = size*0.3; ctx.lineCap = 'round';
      ctx.stroke();
      ctx.restore();
    }

    function drawChaosStar(ctx, x, y, size, color, alpha) {
      ctx.save();
      ctx.translate(x, y);
      ctx.globalAlpha = alpha;
      ctx.fillStyle = color;
      const spikes = 5;
      const outerR = size;
      const innerR = size*0.4;
      ctx.beginPath();
      for (let i=0; i<spikes*2; i++) {
        const radius = i%2===0 ? outerR : innerR;
        const angle = (i * Math.PI/spikes) - Math.PI/2;
        const px = Math.cos(angle) * radius;
        const py = Math.sin(angle) * radius;
        if (i===0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.closePath();
      ctx.fill();
      ctx.strokeStyle = '#fff'; ctx.lineWidth = 1; ctx.stroke();
      ctx.restore();
    }

    function drawChaosRing(ctx, x, y, size, color, alpha) {
      ctx.save();
      ctx.translate(x, y);
      ctx.globalAlpha = alpha;
      ctx.beginPath();
      ctx.arc(0, 0, size, 0, 2*Math.PI);
      ctx.strokeStyle = color; ctx.lineWidth = size*0.35;
      ctx.stroke();
      ctx.beginPath();
      ctx.arc(0, 0, size*0.3, 0, 2*Math.PI);
      ctx.fillStyle = color; ctx.fill();
      ctx.restore();
    }

    function drawChaosCross(ctx, x, y, size, color, alpha) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(Math.random() * Math.PI);
      ctx.globalAlpha = alpha;
      ctx.fillStyle = color;
      ctx.fillRect(-size*0.2, -size, size*0.4, size*2);
      ctx.fillRect(-size, -size*0.2, size*2, size*0.4);
      ctx.strokeStyle = '#000'; ctx.lineWidth = 1.5;
      ctx.strokeRect(-size*0.2, -size, size*0.4, size*2);
      ctx.strokeRect(-size, -size*0.2, size*2, size*0.4);
      ctx.restore();
    }

    function drawChaosGlyph(ctx, x, y, size, color, alpha) {
      ctx.save();
      ctx.translate(x, y);
      ctx.globalAlpha = alpha;
      ctx.font = `bold ${size*2}px 'Bangers', cursive`;
      ctx.fillStyle = color;
      ctx.shadowColor = '#000'; ctx.shadowBlur = 6;
      const glyphs = ['!', '@', '#', '$', '%', '&', '?', '※', '∞', '◈', '◆', '◉'];
      ctx.fillText(glyphs[Math.floor(Math.random()*glyphs.length)], -size*0.7, size*0.7);
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawChaosDot(ctx, x, y, size, color, alpha) {
      ctx.save();
      ctx.translate(x, y);
      ctx.globalAlpha = alpha;
      ctx.fillStyle = color;
      ctx.shadowColor = color; ctx.shadowBlur = 10;
      ctx.beginPath();
      ctx.arc(0, 0, size*0.4, 0, 2*Math.PI);
      ctx.fill();
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawMaximalChaosSpace(ctx) {
      const grad = ctx.createRadialGradient(CX-20, CY-20, 10, CX, CY, R);
      grad.addColorStop(0, '#1a1c23');
      grad.addColorStop(0.5, '#0f0f15');
      grad.addColorStop(1, '#050508');
      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[4].start, SECTORS[4].end);
      ctx.closePath();
      ctx.clip();

      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      ctx.globalAlpha = 0.15;
      for (let i=0; i<60; i++) {
        ctx.fillStyle = `hsl(${Math.random()*360}, 80%, 60%)`;
        ctx.beginPath();
        ctx.arc(CX-R*0.1 + Math.random()*R*1.2, CY-R*0.1 + Math.random()*R*1.2, 3+Math.random()*12, 0, 2*Math.PI);
        ctx.fill();
      }
      ctx.globalAlpha = 1.0;

      const shapeFuncs = [drawChaosCircle, drawChaosSquare, drawChaosPolygon, drawChaosCurve, 
                          drawChaosStar, drawChaosRing, drawChaosCross, drawChaosGlyph, drawChaosDot];

      for (let i=0; i<35; i++) {
        const angle = SECTORS[4].start + Math.random() * (SECTORS[4].end - SECTORS[4].start);
        const dist = R * 0.15 + Math.random() * (R * 0.75);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        const shapeType = Math.floor(Math.random() * shapeFuncs.length);
        const size = 8 + Math.random() * 35;
        const hue = Math.floor(Math.random() * 360);
        const sat = 70 + Math.floor(Math.random() * 30);
        const light = 50 + Math.floor(Math.random() * 30);
        const color = `hsl(${hue}, ${sat}%, ${light}%)`;
        const alpha = 0.4 + Math.random() * 0.5;

        const func = shapeFuncs[shapeType];
        if (shapeType === 2) {
          func(ctx, px, py, size, 3+Math.floor(Math.random()*6), color, alpha, Math.random()>0.3);
        } else {
          func(ctx, px, py, size, color, alpha);
        }
      }

      for (let i=0; i<25; i++) {
        const angle = SECTORS[4].start + Math.random() * (SECTORS[4].end - SECTORS[4].start);
        const dist = R * 0.1 + Math.random() * (R * 0.8);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        const size = 5 + Math.random() * 15;
        const hue = Math.floor(Math.random() * 360);
        const color = `hsl(${hue}, 90%, 65%)`;
        const alpha = 0.5 + Math.random() * 0.4;

        if (Math.random() > 0.5) drawChaosDot(ctx, px, py, size, color, alpha);
        else drawChaosGlyph(ctx, px, py, size*0.8, color, alpha);
      }

      ctx.font = "42px 'Bangers', cursive";
      ctx.fillStyle = '#fff';
      ctx.shadowColor = '#000'; ctx.shadowBlur = 20;
      ctx.globalAlpha = 0.9;
      ctx.fillText("MAX", CX+R*0.2, CY-R*0.15);
      ctx.font = "italic 28px 'Special Elite', monospace";
      ctx.fillStyle = '#ff0';
      ctx.fillText("CHAOS", CX+R*0.3, CY+R*0.25);
      ctx.shadowBlur = 0;
      ctx.globalAlpha = 1.0;

      ctx.restore();
    }
	    // ========== セクション5: サイバーパンク空間 ==========
    function drawNeonLine(ctx, x1, y1, x2, y2, color, width) {
      ctx.save();
      ctx.shadowColor = color;
      ctx.shadowBlur = 15;
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.strokeStyle = color;
      ctx.lineWidth = width;
      ctx.stroke();
      ctx.shadowBlur = 8;
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = width * 0.4;
      ctx.stroke();
      ctx.restore();
    }

    function drawPerspectiveGrid(ctx, vpX, vpY, count, color, alpha) {
      ctx.save();
      ctx.globalAlpha = alpha;
      ctx.strokeStyle = color;
      ctx.lineWidth = 1.2;
      ctx.shadowColor = color;
      ctx.shadowBlur = 6;
      
      for (let i = 0; i < count; i++) {
        const t = i / (count - 1);
        const startX = vpX + (CX - R - vpX) * t * 2;
        const startY = vpY + (CY + R * 0.8 - vpY) * t;
        ctx.beginPath();
        ctx.moveTo(vpX, vpY);
        ctx.lineTo(startX, startY);
        ctx.stroke();
        
        ctx.beginPath();
        ctx.moveTo(vpX, vpY);
        ctx.lineTo(startX + R * 1.5, startY);
        ctx.stroke();
      }
      
      for (let i = 0; i < 8; i++) {
        const y = vpY + i * 25;
        ctx.beginPath();
        ctx.moveTo(vpX - R * 1.5, y);
        ctx.lineTo(vpX + R * 1.5, y);
        ctx.strokeStyle = color;
        ctx.globalAlpha = alpha * (1 - i/12);
        ctx.stroke();
      }
      
      ctx.restore();
    }

    function drawGlitchRect(ctx, x, y, w, h, color, offsetCount) {
      ctx.save();
      ctx.fillStyle = color;
      ctx.shadowColor = color;
      ctx.shadowBlur = 8;
      
      for (let i = 0; i < offsetCount; i++) {
        const offsetX = (Math.random() - 0.5) * w * 0.8;
        const offsetY = (Math.random() - 0.5) * h * 0.3;
        const hue = (i === 0) ? 180 : (i === 1 ? 300 : 60);
        ctx.fillStyle = `hsla(${hue}, 100%, 60%, ${0.3 + i*0.1})`;
        ctx.fillRect(x + offsetX, y + offsetY, w * (0.8 + Math.random()*0.4), h * 0.3);
      }
      
      ctx.fillStyle = color;
      ctx.globalAlpha = 0.6;
      ctx.fillRect(x, y, w, h * 0.15);
      ctx.restore();
    }

    function drawHoloRing(ctx, x, y, radius, color, alpha) {
      ctx.save();
      ctx.translate(x, y);
      ctx.shadowColor = color;
      ctx.shadowBlur = 18;
      ctx.globalAlpha = alpha;
      
      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2 * Math.PI);
      ctx.strokeStyle = color;
      ctx.lineWidth = 3;
      ctx.stroke();
      
      ctx.shadowBlur = 10;
      ctx.beginPath();
      ctx.arc(0, 0, radius * 0.3, 0, 2 * Math.PI);
      ctx.fillStyle = color;
      ctx.globalAlpha = alpha * 0.5;
      ctx.fill();
      
      ctx.restore();
    }

    function drawHUDCross(ctx, x, y, size, color, alpha) {
      ctx.save();
      ctx.translate(x, y);
      ctx.shadowColor = color;
      ctx.shadowBlur = 12;
      ctx.globalAlpha = alpha;
      
      ctx.strokeStyle = color;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(-size, 0);
      ctx.lineTo(-size*0.3, 0);
      ctx.moveTo(size*0.3, 0);
      ctx.lineTo(size, 0);
      ctx.moveTo(0, -size);
      ctx.lineTo(0, -size*0.3);
      ctx.moveTo(0, size*0.3);
      ctx.lineTo(0, size);
      ctx.stroke();
      
      ctx.beginPath();
      ctx.arc(0, 0, size*0.5, 0, 2 * Math.PI);
      ctx.strokeStyle = color;
      ctx.lineWidth = 1.5;
      ctx.stroke();
      
      ctx.restore();
    }

    function drawDataNode(ctx, x, y, size, color) {
      ctx.save();
      ctx.translate(x, y);
      ctx.shadowColor = color;
      ctx.shadowBlur = 15;
      
      const grad = ctx.createRadialGradient(-size*0.2, -size*0.2, 1, 0, 0, size);
      grad.addColorStop(0, '#ffffff');
      grad.addColorStop(0.5, color);
      grad.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(0, 0, size, 0, 2 * Math.PI);
      ctx.fill();
      
      ctx.restore();
    }

    function drawScanLine(ctx, x, y, width, color, alpha) {
      ctx.save();
      ctx.shadowColor = color;
      ctx.shadowBlur = 8;
      ctx.globalAlpha = alpha;
      
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x + width, y);
      ctx.strokeStyle = color;
      ctx.lineWidth = 2;
      ctx.stroke();
      
      for (let i = 0; i < 3; i++) {
        ctx.beginPath();
        ctx.moveTo(x + i * 20, y - 2);
        ctx.lineTo(x + i * 20 + 8, y + 2);
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1;
        ctx.stroke();
      }
      
      ctx.restore();
    }

    function drawDataFlow(ctx, x1, y1, x2, y2, color, segments) {
      ctx.save();
      ctx.shadowColor = color;
      ctx.shadowBlur = 8;
      
      ctx.beginPath();
      ctx.setLineDash([5, 10]);
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.strokeStyle = color;
      ctx.lineWidth = 2;
      ctx.stroke();
      
      ctx.setLineDash([]);
      
      for (let i = 0; i < segments; i++) {
        const t = i / (segments - 1);
        const px = x1 + (x2 - x1) * t;
        const py = y1 + (y2 - y1) * t;
        drawDataNode(ctx, px, py, 3, color);
      }
      
      ctx.restore();
    }

    function drawCyberpunkSpace(ctx) {
      const grad = ctx.createRadialGradient(CX-15, CY-10, 10, CX, CY, R);
      grad.addColorStop(0, '#0b0e14');
      grad.addColorStop(0.6, '#06080a');
      grad.addColorStop(1, '#000000');
      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[5].start, SECTORS[5].end);
      ctx.closePath();
      ctx.clip();

      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      const vpAngle = SECTORS[5].start + (SECTORS[5].end - SECTORS[5].start) * 0.5;
      const vpDist = R * 0.35;
      const vpX = CX + Math.cos(vpAngle) * vpDist;
      const vpY = CY + Math.sin(vpAngle) * vpDist;
      
      drawPerspectiveGrid(ctx, vpX, vpY, 12, '#00ffff', 0.4);
      drawPerspectiveGrid(ctx, vpX + 20, vpY - 15, 8, '#ff44cc', 0.25);

      const colors = ['#00ffff', '#ff44cc', '#ffff00', '#00ff88', '#ff00ff'];
      
      for (let i = 0; i < 32; i++) {
        const angle = SECTORS[5].start + Math.random() * (SECTORS[5].end - SECTORS[5].start);
        const dist = R * 0.1 + Math.random() * (R * 0.75);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        
        const shapeType = Math.floor(Math.random() * 6);
        const color = colors[Math.floor(Math.random() * colors.length)];
        const alpha = 0.3 + Math.random() * 0.5;
        
        switch (shapeType) {
          case 0:
            const px2 = px + (Math.random() - 0.5) * 60;
            const py2 = py + (Math.random() - 0.5) * 60;
            drawNeonLine(ctx, px, py, px2, py2, color, 1.5 + Math.random() * 3);
            break;
          case 1:
            drawGlitchRect(ctx, px, py, 20 + Math.random() * 40, 15 + Math.random() * 25, color, 3);
            break;
          case 2:
            drawHoloRing(ctx, px, py, 10 + Math.random() * 25, color, alpha);
            break;
          case 3:
            drawHUDCross(ctx, px, py, 8 + Math.random() * 18, color, alpha);
            break;
          case 4:
            drawDataNode(ctx, px, py, 4 + Math.random() * 10, color);
            break;
          case 5:
            drawScanLine(ctx, px - 25, py, 50 + Math.random() * 40, color, alpha);
            break;
        }
      }

      for (let i = 0; i < 6; i++) {
        const angle1 = SECTORS[5].start + Math.random() * (SECTORS[5].end - SECTORS[5].start);
        const dist1 = R * 0.2 + Math.random() * (R * 0.5);
        const angle2 = angle1 + (Math.random() - 0.5) * 0.5;
        const dist2 = dist1 + (Math.random() - 0.5) * R * 0.3;
        const px1 = CX + Math.cos(angle1) * dist1;
        const py1 = CY + Math.sin(angle1) * dist1;
        const px2 = CX + Math.cos(angle2) * dist2;
        const py2 = CY + Math.sin(angle2) * dist2;
        drawDataFlow(ctx, px1, py1, px2, py2, colors[i % colors.length], 5);
      }

      for (let i = 0; i < 20; i++) {
        const angle = SECTORS[5].start + Math.random() * (SECTORS[5].end - SECTORS[5].start);
        const dist = R * 0.05 + Math.random() * (R * 0.8);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        drawDataNode(ctx, px, py, 2 + Math.random() * 5, colors[Math.floor(Math.random() * colors.length)]);
      }

      ctx.font = "28px 'Monoton', cursive";
      ctx.fillStyle = '#00ffff';
      ctx.shadowColor = '#ff44cc';
      ctx.shadowBlur = 20;
      ctx.globalAlpha = 0.9;
      ctx.fillText("//CYBER", CX+R*0.15, CY-R*0.25);
      ctx.font = "18px 'Special Elite', monospace";
      ctx.fillStyle = '#ff44cc';
      ctx.fillText("NEON_GRID", CX+R*0.2, CY-R*0.05);
      ctx.shadowBlur = 0;
      ctx.globalAlpha = 1.0;

      ctx.restore();
    }
	    // ========== セクション6: 炎のフィールド空間 ==========
    function drawFlameTongue(ctx, x, y, width, height, hueBase) {
      ctx.save();
      ctx.translate(x, y);
      const tilt = (Math.random() - 0.5) * 0.4;
      ctx.rotate(tilt);
      
      const grad = ctx.createLinearGradient(0, height*0.3, 0, -height*0.8);
      grad.addColorStop(0, `hsl(${hueBase}, 100%, 50%)`);
      grad.addColorStop(0.4, `hsl(${hueBase + 15}, 100%, 55%)`);
      grad.addColorStop(0.7, `hsl(${hueBase + 30}, 95%, 60%)`);
      grad.addColorStop(1, `hsl(${hueBase + 45}, 90%, 70%)`);
      
      ctx.fillStyle = grad;
      ctx.shadowColor = `hsl(${hueBase}, 100%, 60%)`;
      ctx.shadowBlur = 20;
      
      ctx.beginPath();
      ctx.moveTo(-width/2, height*0.4);
      ctx.lineTo(0, -height*0.8);
      ctx.lineTo(width/2, height*0.4);
      ctx.closePath();
      ctx.fill();
      
      const grad2 = ctx.createLinearGradient(0, height*0.2, 0, -height*0.5);
      grad2.addColorStop(0, `hsl(${hueBase + 20}, 100%, 70%)`);
      grad2.addColorStop(1, `hsl(${hueBase + 40}, 100%, 80%)`);
      ctx.fillStyle = grad2;
      ctx.globalAlpha = 0.6;
      ctx.beginPath();
      ctx.moveTo(-width/3, height*0.2);
      ctx.lineTo(0, -height*0.5);
      ctx.lineTo(width/3, height*0.2);
      ctx.closePath();
      ctx.fill();
      
      ctx.restore();
    }

    function drawSpark(ctx, x, y, size, hue) {
      ctx.save();
      ctx.translate(x, y);
      
      const grad = ctx.createRadialGradient(-size*0.2, -size*0.2, 1, 0, 0, size);
      grad.addColorStop(0, `hsl(${hue + 30}, 100%, 80%)`);
      grad.addColorStop(0.5, `hsl(${hue}, 100%, 60%)`);
      grad.addColorStop(1, `hsl(${hue - 10}, 90%, 40%)`);
      
      ctx.fillStyle = grad;
      ctx.shadowColor = `hsl(${hue}, 100%, 70%)`;
      ctx.shadowBlur = 12;
      ctx.beginPath();
      ctx.arc(0, 0, size, 0, 2 * Math.PI);
      ctx.fill();
      
      ctx.restore();
    }

    function drawFlameBase(ctx, x, y, width, height, hueBase) {
      ctx.save();
      ctx.translate(x, y);
      
      const grad = ctx.createLinearGradient(0, 0, 0, -height);
      grad.addColorStop(0, `hsl(${hueBase - 10}, 100%, 35%)`);
      grad.addColorStop(0.5, `hsl(${hueBase}, 100%, 45%)`);
      grad.addColorStop(1, `hsl(${hueBase + 20}, 100%, 55%)`);
      
      ctx.fillStyle = grad;
      ctx.shadowColor = `hsl(${hueBase}, 100%, 50%)`;
      ctx.shadowBlur = 25;
      
      ctx.beginPath();
      ctx.ellipse(0, 0, width, height*0.3, 0, 0, 2 * Math.PI);
      ctx.fill();
      
      ctx.restore();
    }

    function drawFlameCurve(ctx, x, y, size, hueBase) {
      ctx.save();
      ctx.translate(x, y);
      
      ctx.beginPath();
      ctx.moveTo(0, size*0.3);
      
      const cp1x = -size*0.4;
      const cp1y = -size*0.1;
      const cp2x = size*0.3;
      const cp2y = -size*0.5;
      const endX = 0;
      const endY = -size*0.9;
      
      ctx.bezierCurveTo(cp1x, cp1y, cp2x, cp2y, endX, endY);
      
      const grad = ctx.createLinearGradient(0, size*0.3, 0, -size*0.9);
      grad.addColorStop(0, `hsl(${hueBase}, 100%, 50%)`);
      grad.addColorStop(1, `hsl(${hueBase + 40}, 100%, 70%)`);
      
      ctx.strokeStyle = grad;
      ctx.lineWidth = size * 0.4;
      ctx.lineCap = 'round';
      ctx.shadowColor = `hsl(${hueBase}, 100%, 60%)`;
      ctx.shadowBlur = 18;
      ctx.stroke();
      
      ctx.restore();
    }

    function drawFlameGlow(ctx, x, y, size, hue) {
      ctx.save();
      ctx.translate(x, y);
      
      ctx.beginPath();
      ctx.arc(0, 0, size, 0, 2 * Math.PI);
      
      const grad = ctx.createRadialGradient(-size*0.2, -size*0.2, 2, 0, 0, size);
      grad.addColorStop(0, `hsla(${hue + 30}, 100%, 70%, 0.8)`);
      grad.addColorStop(1, `hsla(${hue}, 90%, 40%, 0)`);
      
      ctx.fillStyle = grad;
      ctx.shadowColor = `hsl(${hue}, 100%, 60%)`;
      ctx.shadowBlur = 20;
      ctx.fill();
      
      ctx.restore();
    }

    function drawFireFieldSpace(ctx) {
      const grad = ctx.createLinearGradient(CX, CY-R, CX, CY+R);
      grad.addColorStop(0, '#3d0a0a');
      grad.addColorStop(0.5, '#6b1414');
      grad.addColorStop(1, '#1a0505');
      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[6].start, SECTORS[6].end);
      ctx.closePath();
      ctx.clip();

      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      ctx.globalAlpha = 0.3;
      for (let i = 0; i < 8; i++) {
        const angle = SECTORS[6].start + (i / 8) * (SECTORS[6].end - SECTORS[6].start);
        const dist = R * 0.3;
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        drawFlameGlow(ctx, px, py, R * 0.25, 0);
      }
      ctx.globalAlpha = 1.0;

      for (let i = 0; i < 5; i++) {
        const angle = SECTORS[6].start + Math.random() * (SECTORS[6].end - SECTORS[6].start);
        const dist = R * 0.1 + Math.random() * R * 0.35;
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist + R * 0.15;
        drawFlameBase(ctx, px, py, 25 + Math.random() * 35, 15 + Math.random() * 20, 5 + Math.random() * 15);
      }

      for (let i = 0; i < 35; i++) {
        const angle = SECTORS[6].start + Math.random() * (SECTORS[6].end - SECTORS[6].start);
        const dist = R * 0.1 + Math.random() * (R * 0.7);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        
        const shapeType = Math.floor(Math.random() * 4);
        const hueBase = 0 + Math.random() * 30;
        
        switch (shapeType) {
          case 0:
            drawFlameTongue(ctx, px, py, 12 + Math.random() * 25, 20 + Math.random() * 40, hueBase);
            break;
          case 1:
            drawSpark(ctx, px, py, 3 + Math.random() * 10, hueBase);
            break;
          case 2:
            drawFlameCurve(ctx, px, py, 15 + Math.random() * 30, hueBase);
            break;
          case 3:
            drawFlameGlow(ctx, px, py, 8 + Math.random() * 18, hueBase);
            break;
        }
      }

      for (let i = 0; i < 25; i++) {
        const angle = SECTORS[6].start + Math.random() * (SECTORS[6].end - SECTORS[6].start);
        const dist = R * 0.05 + Math.random() * (R * 0.75);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        drawSpark(ctx, px, py, 2 + Math.random() * 6, 10 + Math.random() * 40);
      }

      for (let i = 0; i < 8; i++) {
        const angle = SECTORS[6].start + Math.random() * (SECTORS[6].end - SECTORS[6].start);
        const dist = R * 0.2 + Math.random() * R * 0.4;
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist - R * 0.1;
        drawFlameTongue(ctx, px, py, 18 + Math.random() * 30, 30 + Math.random() * 50, 15 + Math.random() * 20);
      }

      ctx.font = "bold 34px 'Ewert', cursive";
      ctx.fillStyle = '#ffd700';
      ctx.shadowColor = '#ff4500';
      ctx.shadowBlur = 25;
      ctx.globalAlpha = 0.9;
      ctx.fillText("FIRE", CX+R*0.2, CY-R*0.2);
      ctx.font = "20px 'Special Elite', monospace";
      ctx.fillStyle = '#ffaa00';
      ctx.fillText("INFERNO", CX+R*0.25, CY+R*0.1);
      ctx.shadowBlur = 0;
      ctx.globalAlpha = 1.0;

      ctx.restore();
    }
	    // ========== セクション7: 光と闇のミニマリスト空間 ==========
    function drawMinimalCircle(ctx, x, y, radius, color, shadowColor=null, blur=0) {
      ctx.save();
      ctx.translate(x, y);
      ctx.shadowColor = shadowColor || color;
      ctx.shadowBlur = blur;
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2*Math.PI);
      ctx.fill();
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawMinimalRect(ctx, x, y, w, h, color, shadowColor=null, blur=0, rotate=0) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(rotate);
      ctx.shadowColor = shadowColor || color;
      ctx.shadowBlur = blur;
      ctx.fillStyle = color;
      ctx.fillRect(-w/2, -h/2, w, h);
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawMinimalLine(ctx, x1, y1, x2, y2, color, width, blur=0) {
      ctx.save();
      ctx.shadowColor = color;
      ctx.shadowBlur = blur;
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.strokeStyle = color;
      ctx.lineWidth = width;
      ctx.stroke();
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawMinimalTriangle(ctx, x, y, size, color, shadowColor=null, blur=0, rotate=0) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(rotate);
      ctx.shadowColor = shadowColor || color;
      ctx.shadowBlur = blur;
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.moveTo(0, -size);
      ctx.lineTo(size, size);
      ctx.lineTo(-size, size);
      ctx.closePath();
      ctx.fill();
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawMinimalCross(ctx, x, y, size, color, shadowColor=null, blur=0, rotate=0) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(rotate);
      ctx.shadowColor = shadowColor || color;
      ctx.shadowBlur = blur;
      ctx.fillStyle = color;
      ctx.fillRect(-size*0.15, -size, size*0.3, size*2);
      ctx.fillRect(-size, -size*0.15, size*2, size*0.3);
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawMinimalArc(ctx, x, y, radius, color, startAngle, endAngle, width, blur=0) {
      ctx.save();
      ctx.translate(x, y);
      ctx.shadowColor = color;
      ctx.shadowBlur = blur;
      ctx.beginPath();
      ctx.arc(0, 0, radius, startAngle, endAngle);
      ctx.strokeStyle = color;
      ctx.lineWidth = width;
      ctx.stroke();
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawMinimalDashedLine(ctx, x1, y1, x2, y2, color, width, dash, blur=0) {
      ctx.save();
      ctx.shadowColor = color;
      ctx.shadowBlur = blur;
      ctx.beginPath();
      ctx.setLineDash(dash);
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.strokeStyle = color;
      ctx.lineWidth = width;
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawMinimalDiagonal(ctx, x, y, size, color, width, blur=0) {
      ctx.save();
      ctx.translate(x, y);
      ctx.shadowColor = color;
      ctx.shadowBlur = blur;
      ctx.beginPath();
      ctx.moveTo(-size, -size);
      ctx.lineTo(size, size);
      ctx.strokeStyle = color;
      ctx.lineWidth = width;
      ctx.stroke();
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawMinimalistSpace(ctx) {
      ctx.fillStyle = '#e8e4db';
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[7].start, SECTORS[7].end);
      ctx.closePath();
      ctx.clip();

      ctx.fillStyle = '#e8e4db';
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      ctx.globalAlpha = 0.05;
      for (let i=0; i<20; i++) {
        drawMinimalLine(ctx, CX-R, CY-R + i*30, CX+R, CY-R + i*40, '#000', 0.5, 0);
      }
      ctx.globalAlpha = 1.0;

      const colors = ['#000000', '#ffffff', '#4a4a4a', '#8a8a8a'];

      for (let i=0; i<32; i++) {
        const angle = SECTORS[7].start + Math.random() * (SECTORS[7].end - SECTORS[7].start);
        const dist = R * 0.15 + Math.random() * (R * 0.7);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        
        const shapeType = Math.floor(Math.random() * 8);
        const color = colors[Math.floor(Math.random() * colors.length)];
        const blur = (color === '#ffffff') ? 12 : 6;
        const size = 8 + Math.random() * 30;

        switch (shapeType) {
          case 0: drawMinimalCircle(ctx, px, py, size*0.6, color, color, blur); break;
          case 1: drawMinimalRect(ctx, px, py, size, size*0.7, color, color, blur, Math.random()*Math.PI); break;
          case 2: {
            const px2 = px + (Math.random()-0.5)*50;
            const py2 = py + (Math.random()-0.5)*50;
            drawMinimalLine(ctx, px, py, px2, py2, color, 2+Math.random()*4, blur);
            break;
          }
          case 3: drawMinimalTriangle(ctx, px, py, size*0.7, color, color, blur, Math.random()*Math.PI); break;
          case 4: drawMinimalCross(ctx, px, py, size*0.6, color, color, blur, Math.random()*Math.PI); break;
          case 5: drawMinimalArc(ctx, px, py, size*0.7, color, 0, Math.PI*1.5, 3, blur); break;
          case 6: {
            const px2 = px + (Math.random()-0.5)*60;
            const py2 = py + (Math.random()-0.5)*60;
            drawMinimalDashedLine(ctx, px, py, px2, py2, color, 2, [5, 8], blur);
            break;
          }
          case 7: drawMinimalDiagonal(ctx, px, py, size*0.8, color, 2.5, blur); break;
        }
      }

      for (let i=0; i<20; i++) {
        const angle = SECTORS[7].start + Math.random() * (SECTORS[7].end - SECTORS[7].start);
        const dist = R * 0.1 + Math.random() * (R * 0.75);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        const color = (i%2===0) ? '#000' : '#fff';
        const blur = (color === '#fff') ? 10 : 4;
        if (i%3===0) drawMinimalCircle(ctx, px, py, 4+Math.random()*10, color, color, blur);
        else if (i%3===1) drawMinimalRect(ctx, px, py, 8+Math.random()*15, 6+Math.random()*12, color, color, blur, Math.random()*Math.PI);
        else drawMinimalLine(ctx, px, py, px+(Math.random()-0.5)*30, py+(Math.random()-0.5)*30, color, 1.5, blur);
      }

      for (let i=0; i<4; i++) {
        const angle = SECTORS[7].start + 0.1 + i * 0.2;
        const dist = R * 0.3;
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        drawMinimalLine(ctx, px, py, px+30, py-20, '#000', 4, 0);
      }

      ctx.font = "22px 'Cormorant Garamond', serif";
      ctx.fillStyle = '#1a1a1a';
      ctx.shadowColor = '#aaa'; ctx.shadowBlur = 6;
      ctx.fillText("·light·", CX+R*0.3, CY-R*0.2);
      ctx.fillStyle = '#ffffff';
      ctx.shadowColor = '#000'; ctx.shadowBlur = 10;
      ctx.fillText("dark", CX+R*0.45, CY+R*0.1);
      ctx.shadowBlur = 0;
      ctx.strokeStyle = '#333'; ctx.lineWidth = 1; ctx.strokeRect(CX+R*0.2, CY+R*0.25, 60, 2);

      ctx.restore();
    }
	    // ========== セクション8: バブルファンタジー空間 ==========
    function drawBubble(ctx, x, y, radius, hue) {
      ctx.save();
      ctx.translate(x, y);

      const grad = ctx.createRadialGradient(
        -radius*0.25, -radius*0.25, radius*0.1,
        0, 0, radius
      );
      grad.addColorStop(0, `hsla(${hue}, 70%, 85%, 0.9)`);
      grad.addColorStop(0.4, `hsla(${hue}, 60%, 70%, 0.7)`);
      grad.addColorStop(0.8, `hsla(${hue}, 50%, 55%, 0.5)`);
      grad.addColorStop(1, `hsla(${hue}, 40%, 40%, 0.2)`);

      ctx.shadowColor = `hsla(${hue}, 80%, 70%, 0.8)`;
      ctx.shadowBlur = radius * 0.8;

      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2 * Math.PI);
      ctx.fillStyle = grad;
      ctx.fill();

      ctx.shadowBlur = 0;
      ctx.strokeStyle = `hsla(${hue}, 60%, 80%, 0.4)`;
      ctx.lineWidth = 1.5;
      ctx.stroke();

      ctx.beginPath();
      ctx.ellipse(-radius*0.3, -radius*0.3, radius*0.25, radius*0.15, 0, 0, 2*Math.PI);
      ctx.fillStyle = `hsla(0, 0%, 100%, 0.6)`;
      ctx.shadowBlur = radius * 0.3;
      ctx.shadowColor = 'white';
      ctx.fill();

      ctx.beginPath();
      ctx.arc(radius*0.2, radius*0.2, radius*0.08, 0, 2*Math.PI);
      ctx.fillStyle = `hsla(0, 0%, 100%, 0.3)`;
      ctx.shadowBlur = radius * 0.2;
      ctx.fill();

      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawSmallBubble(ctx, x, y, radius, hue) {
      ctx.save();
      ctx.translate(x, y);

      const grad = ctx.createRadialGradient(
        -radius*0.2, -radius*0.2, radius*0.1,
        0, 0, radius
      );
      grad.addColorStop(0, `hsla(${hue}, 75%, 90%, 0.9)`);
      grad.addColorStop(0.6, `hsla(${hue}, 65%, 70%, 0.5)`);
      grad.addColorStop(1, `hsla(${hue}, 50%, 50%, 0.1)`);

      ctx.shadowColor = `hsla(${hue}, 80%, 75%, 0.6)`;
      ctx.shadowBlur = radius * 0.6;

      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2 * Math.PI);
      ctx.fillStyle = grad;
      ctx.fill();

      ctx.beginPath();
      ctx.arc(-radius*0.25, -radius*0.25, radius*0.2, 0, 2*Math.PI);
      ctx.fillStyle = `hsla(0, 0%, 100%, 0.5)`;
      ctx.shadowBlur = radius * 0.2;
      ctx.fill();

      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawBubbleTrail(ctx, x, y, radius, hue, count) {
      for (let i=0; i<count; i++) {
        const offsetX = (i - count/2) * radius * 0.8 + (Math.random() - 0.5) * radius;
        const offsetY = -i * radius * 0.6 + (Math.random() - 0.5) * radius;
        const trailRadius = radius * (0.4 + Math.random() * 0.3);
        drawSmallBubble(ctx, x + offsetX, y + offsetY, trailRadius, hue);
      }
    }

    function drawBubbleCluster(ctx, x, y, baseRadius, hue) {
      drawBubble(ctx, x, y, baseRadius, hue);
      
      const smallCount = 3 + Math.floor(Math.random() * 4);
      for (let i=0; i<smallCount; i++) {
        const angle = (i / smallCount) * Math.PI * 2 + Math.random() * 0.5;
        const dist = baseRadius * 0.9;
        const sx = x + Math.cos(angle) * dist;
        const sy = y + Math.sin(angle) * dist;
        drawSmallBubble(ctx, sx, sy, baseRadius * 0.35, (hue + 20) % 360);
      }
    }

    function drawSparkle(ctx, x, y, size, hue) {
      ctx.save();
      ctx.translate(x, y);

      const grad = ctx.createRadialGradient(0, 0, 0, 0, 0, size);
      grad.addColorStop(0, `hsla(${hue}, 90%, 90%, 1)`);
      grad.addColorStop(0.5, `hsla(${hue}, 80%, 75%, 0.6)`);
      grad.addColorStop(1, `hsla(${hue}, 70%, 60%, 0)`);

      ctx.fillStyle = grad;
      ctx.shadowColor = `hsla(${hue}, 90%, 80%, 0.8)`;
      ctx.shadowBlur = size * 1.5;

      ctx.beginPath();
      ctx.arc(0, 0, size, 0, 2 * Math.PI);
      ctx.fill();

      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawBubbleFantasySpace(ctx) {
      const grad = ctx.createLinearGradient(CX, CY-R, CX, CY+R);
      grad.addColorStop(0, '#1a0a2e');
      grad.addColorStop(0.4, '#2d1b4e');
      grad.addColorStop(0.7, '#1e3a5f');
      grad.addColorStop(1, '#0a1628');
      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[8].start, SECTORS[8].end);
      ctx.closePath();
      ctx.clip();

      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      for (let i=0; i<15; i++) {
        const angle = SECTORS[8].start + Math.random() * (SECTORS[8].end - SECTORS[8].start);
        const dist = R * 0.1 + Math.random() * (R * 0.7);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        drawSparkle(ctx, px, py, 3 + Math.random() * 8, 40 + Math.random() * 100);
      }

      for (let i=0; i<18; i++) {
        const angle = SECTORS[8].start + Math.random() * (SECTORS[8].end - SECTORS[8].start);
        const dist = R * 0.15 + Math.random() * (R * 0.65);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        const hue = Math.floor(Math.random() * 360);
        const radius = 12 + Math.random() * 30;

        if (Math.random() > 0.5) {
          drawBubbleCluster(ctx, px, py, radius, hue);
        } else {
          drawBubble(ctx, px, py, radius, hue);
        }
      }

      for (let i=0; i<15; i++) {
        const angle = SECTORS[8].start + Math.random() * (SECTORS[8].end - SECTORS[8].start);
        const dist = R * 0.1 + Math.random() * (R * 0.7);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        const hue = Math.floor(Math.random() * 360);
        drawSmallBubble(ctx, px, py, 5 + Math.random() * 12, hue);
      }

      for (let i=0; i<5; i++) {
        const angle = SECTORS[8].start + Math.random() * (SECTORS[8].end - SECTORS[8].start);
        const dist = R * 0.2 + Math.random() * (R * 0.5);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        const hue = Math.floor(Math.random() * 360);
        drawBubbleTrail(ctx, px, py, 10 + Math.random() * 15, hue, 4 + Math.floor(Math.random() * 4));
      }

      ctx.font = "italic 28px 'Playfair Display', serif";
      ctx.fillStyle = '#e8d5f5';
      ctx.shadowColor = '#b380aa';
      ctx.shadowBlur = 20;
      ctx.fillText("bubbles", CX+R*0.15, CY-R*0.2);
      ctx.font = "18px 'Special Elite', monospace";
      ctx.fillStyle = '#c9b3e8';
      ctx.fillText("dream", CX+R*0.3, CY+R*0.1);
      ctx.shadowBlur = 0;

      ctx.restore();
    }

    // ========== セクション9: 風船の青空空間 ==========
    function drawBalloonBody(ctx, x, y, radius, hue) {
      ctx.save();
      ctx.translate(x, y);

      const grad = ctx.createRadialGradient(
        -radius*0.3, -radius*0.3, radius*0.1,
        0, 0, radius
      );
      grad.addColorStop(0, `hsla(${hue}, 85%, 75%, 1)`);
      grad.addColorStop(0.4, `hsla(${hue}, 80%, 60%, 1)`);
      grad.addColorStop(0.8, `hsla(${hue}, 75%, 45%, 1)`);
      grad.addColorStop(1, `hsla(${hue}, 70%, 35%, 1)`);

      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2 * Math.PI);
      ctx.fillStyle = grad;
      ctx.shadowColor = `hsla(${hue}, 80%, 50%, 0.5)`;
      ctx.shadowBlur = radius * 0.5;
      ctx.fill();
      
      ctx.shadowBlur = 0;
      ctx.beginPath();
      ctx.ellipse(-radius*0.3, -radius*0.3, radius*0.25, radius*0.15, 0, 0, 2*Math.PI);
      ctx.fillStyle = `hsla(0, 0%, 100%, 0.5)`;
      ctx.fill();

      ctx.restore();
    }

    function drawBalloonString(ctx, x, y, radius, tilt) {
      ctx.save();
      ctx.translate(x, y);
      
      ctx.beginPath();
      ctx.moveTo(0, radius * 0.9);
      
      const cp1x = tilt * radius * 0.3;
      const cp1y = radius * 1.8;
      const cp2x = -tilt * radius * 0.2;
      const cp2y = radius * 2.8;
      const endX = tilt * radius * 0.5;
      const endY = radius * 4.0;
      
      ctx.bezierCurveTo(cp1x, cp1y, cp2x, cp2y, endX, endY);
      ctx.strokeStyle = '#5a4a3a';
      ctx.lineWidth = 2;
      ctx.shadowColor = '#3a2a1a';
      ctx.shadowBlur = 4;
      ctx.stroke();
      
      ctx.restore();
    }

    function drawBalloonBasket(ctx, x, y, radius, tilt) {
      ctx.save();
      ctx.translate(x, y);
      
      const endX = tilt * radius * 0.5;
      const endY = radius * 4.0;
      const basketW = radius * 0.5;
      const basketH = radius * 0.3;
      
      ctx.fillStyle = '#8B5E3C';
      ctx.shadowColor = '#3a2a1a';
      ctx.shadowBlur = 6;
      ctx.beginPath();
      ctx.rect(endX - basketW/2, endY, basketW, basketH);
      ctx.fill();
      
      ctx.fillStyle = '#6B4226';
      ctx.shadowBlur = 4;
      ctx.beginPath();
      ctx.rect(endX - basketW/2 - 2, endY - 2, basketW + 4, 3);
      ctx.fill();
      
      ctx.shadowBlur = 2;
      ctx.strokeStyle = '#5a4a3a';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(-radius*0.1, radius * 0.95);
      ctx.lineTo(endX - basketW/3, endY);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(radius*0.1, radius * 0.95);
      ctx.lineTo(endX + basketW/3, endY);
      ctx.stroke();
      
      ctx.restore();
    }

    function drawFullBalloon(ctx, x, y, radius, hue, tilt) {
      drawBalloonBody(ctx, x, y, radius, hue);
      drawBalloonString(ctx, x, y, radius, tilt);
      drawBalloonBasket(ctx, x, y, radius, tilt);
    }

    function drawCloud(ctx, x, y, size) {
      ctx.save();
      ctx.translate(x, y);
      ctx.filter = 'blur(8px)';
      ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
      ctx.shadowColor = 'rgba(200, 220, 255, 0.5)';
      ctx.shadowBlur = 15;
      
      ctx.beginPath();
      ctx.arc(0, 0, size * 0.5, 0, 2 * Math.PI);
      ctx.fill();
      ctx.beginPath();
      ctx.arc(size * 0.4, -size * 0.1, size * 0.4, 0, 2 * Math.PI);
      ctx.fill();
      ctx.beginPath();
      ctx.arc(-size * 0.4, -size * 0.1, size * 0.4, 0, 2 * Math.PI);
      ctx.fill();
      ctx.beginPath();
      ctx.arc(size * 0.2, size * 0.1, size * 0.35, 0, 2 * Math.PI);
      ctx.fill();
      ctx.beginPath();
      ctx.arc(-size * 0.2, size * 0.1, size * 0.35, 0, 2 * Math.PI);
      ctx.fill();
      
      ctx.filter = 'none';
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawSmallBalloon(ctx, x, y, radius, hue, tilt) {
      drawBalloonBody(ctx, x, y, radius, hue);
      ctx.save();
      ctx.translate(x, y);
      ctx.beginPath();
      ctx.moveTo(0, radius * 0.9);
      ctx.lineTo(tilt * radius * 0.4, radius * 3.5);
      ctx.strokeStyle = '#5a4a3a';
      ctx.lineWidth = 1.5;
      ctx.stroke();
      ctx.restore();
    }

    function drawSkySparkle(ctx, x, y, size) {
      ctx.save();
      ctx.translate(x, y);
      
      const grad = ctx.createRadialGradient(0, 0, 0, 0, 0, size);
      grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
      grad.addColorStop(0.5, 'rgba(255, 255, 200, 0.6)');
      grad.addColorStop(1, 'rgba(255, 255, 255, 0)');
      
      ctx.fillStyle = grad;
      ctx.shadowColor = '#aaccff';
      ctx.shadowBlur = size * 1.5;
      ctx.beginPath();
      ctx.arc(0, 0, size, 0, 2 * Math.PI);
      ctx.fill();
      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawBalloonSkySpace(ctx) {
      const grad = ctx.createLinearGradient(CX, CY - R, CX, CY + R);
      grad.addColorStop(0, '#4A90D9');
      grad.addColorStop(0.4, '#7FBAE0');
      grad.addColorStop(0.7, '#B0D8F0');
      grad.addColorStop(1, '#E0F0FF');
      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[9].start, SECTORS[9].end);
      ctx.closePath();
      ctx.clip();

      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      for (let i=0; i<8; i++) {
        const angle = SECTORS[9].start + Math.random() * (SECTORS[9].end - SECTORS[9].start);
        const dist = R * 0.15 + Math.random() * (R * 0.6);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist - R * 0.1;
        drawCloud(ctx, px, py, 25 + Math.random() * 40);
      }

      for (let i=0; i<10; i++) {
        const angle = SECTORS[9].start + Math.random() * (SECTORS[9].end - SECTORS[9].start);
        const dist = R * 0.1 + Math.random() * (R * 0.7);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        drawSkySparkle(ctx, px, py, 3 + Math.random() * 6);
      }

      for (let i=0; i<22; i++) {
        const angle = SECTORS[9].start + Math.random() * (SECTORS[9].end - SECTORS[9].start);
        const dist = R * 0.1 + Math.random() * (R * 0.65);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist - R * 0.1;
        
        const hue = Math.floor(Math.random() * 360);
        const radius = 12 + Math.random() * 25;
        const tilt = (Math.random() - 0.5) * 0.8;
        
        drawFullBalloon(ctx, px, py, radius, hue, tilt);
      }

      for (let i=0; i<12; i++) {
        const angle = SECTORS[9].start + Math.random() * (SECTORS[9].end - SECTORS[9].start);
        const dist = R * 0.05 + Math.random() * (R * 0.7);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist - R * 0.05;
        
        const hue = Math.floor(Math.random() * 360);
        const radius = 6 + Math.random() * 10;
        const tilt = (Math.random() - 0.5) * 0.5;
        
        drawSmallBalloon(ctx, px, py, radius, hue, tilt);
      }

      for (let i=0; i<6; i++) {
        const angle = SECTORS[9].start + Math.random() * (SECTORS[9].end - SECTORS[9].start);
        const dist = R * 0.1 + Math.random() * (R * 0.4);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist - R * 0.3;
        
        const hue = Math.floor(Math.random() * 360);
        const radius = 8 + Math.random() * 15;
        const tilt = (Math.random() - 0.5) * 0.6;
        
        drawFullBalloon(ctx, px, py, radius, hue, tilt);
      }

      ctx.font = "28px 'Shrikhand', cursive";
      ctx.fillStyle = '#1e2f4b';
      ctx.shadowColor = '#aaccff';
      ctx.shadowBlur = 15;
      ctx.fillText("SKY", CX+R*0.25, CY-R*0.25);
      ctx.font = "18px 'Special Elite', monospace";
      ctx.fillStyle = '#2a4a6a';
      ctx.fillText("balloon", CX+R*0.3, CY-R*0.05);
      ctx.shadowBlur = 0;

      ctx.restore();
    }
	
	    // ========== セクション10: 三日月と星空空間 ==========
    function drawCircleStar(ctx, x, y, radius, hue) {
      ctx.save();
      ctx.translate(x, y);

      const grad = ctx.createRadialGradient(-radius*0.2, -radius*0.2, 1, 0, 0, radius);
      grad.addColorStop(0, `hsla(${hue}, 100%, 90%, 1)`);
      grad.addColorStop(0.5, `hsla(${hue}, 90%, 70%, 0.9)`);
      grad.addColorStop(1, `hsla(${hue}, 80%, 50%, 0.3)`);

      ctx.fillStyle = grad;
      ctx.shadowColor = `hsla(${hue}, 100%, 80%, 0.8)`;
      ctx.shadowBlur = radius * 2.5;

      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2 * Math.PI);
      ctx.fill();

      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawBrightStar(ctx, x, y, radius, hue) {
      ctx.save();
      ctx.translate(x, y);

      const grad = ctx.createRadialGradient(-radius*0.2, -radius*0.2, 1, 0, 0, radius);
      grad.addColorStop(0, `hsla(${hue}, 100%, 95%, 1)`);
      grad.addColorStop(0.6, `hsla(${hue}, 95%, 75%, 0.9)`);
      grad.addColorStop(1, `hsla(${hue}, 85%, 55%, 0.4)`);

      ctx.fillStyle = grad;
      ctx.shadowColor = `hsla(${hue}, 100%, 80%, 0.9)`;
      ctx.shadowBlur = radius * 3;

      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2 * Math.PI);
      ctx.fill();

      const lineLength = radius * 2.5;
      ctx.strokeStyle = `hsla(${hue}, 100%, 90%, 0.8)`;
      ctx.lineWidth = radius * 0.3;
      ctx.shadowBlur = radius * 2;

      ctx.beginPath();
      ctx.moveTo(-lineLength, 0);
      ctx.lineTo(lineLength, 0);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(0, -lineLength);
      ctx.lineTo(0, lineLength);
      ctx.stroke();

      ctx.lineWidth = radius * 0.15;
      ctx.strokeStyle = `hsla(${hue}, 100%, 85%, 0.5)`;
      ctx.save();
      ctx.rotate(45 * Math.PI/180);
      ctx.beginPath();
      ctx.moveTo(-lineLength * 0.8, 0);
      ctx.lineTo(lineLength * 0.8, 0);
      ctx.stroke();
      ctx.restore();

      ctx.save();
      ctx.rotate(-45 * Math.PI/180);
      ctx.beginPath();
      ctx.moveTo(-lineLength * 0.8, 0);
      ctx.lineTo(lineLength * 0.8, 0);
      ctx.stroke();
      ctx.restore();

      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawStarShape(ctx, x, y, outerR, hue) {
      ctx.save();
      ctx.translate(x, y);

      const innerR = outerR * 0.475;
      const spikes = 5;
      let rot = Math.PI / 2 * 3;
      const step = Math.PI / spikes;

      const grad = ctx.createRadialGradient(-outerR*0.2, -outerR*0.2, 1, 0, 0, outerR);
      grad.addColorStop(0, `hsla(${hue}, 100%, 90%, 1)`);
      grad.addColorStop(0.5, `hsla(${hue}, 90%, 70%, 0.9)`);
      grad.addColorStop(1, `hsla(${hue}, 80%, 50%, 0.5)`);

      ctx.fillStyle = grad;
      ctx.shadowColor = `hsla(${hue}, 100%, 75%, 0.8)`;
      ctx.shadowBlur = outerR * 2;

      ctx.beginPath();
      for (let i = 0; i < spikes; i++) {
        const px = Math.cos(rot) * outerR;
        const py = Math.sin(rot) * outerR;
        ctx.lineTo(px, py);
        rot += step;

        const px2 = Math.cos(rot) * innerR;
        const py2 = Math.sin(rot) * innerR;
        ctx.lineTo(px2, py2);
        rot += step;
      }
      ctx.closePath();
      ctx.fill();

      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawTinyStar(ctx, x, y, radius, hue) {
      ctx.save();
      ctx.translate(x, y);

      ctx.fillStyle = `hsla(${hue}, 100%, 85%, 0.9)`;
      ctx.shadowColor = `hsla(${hue}, 100%, 80%, 0.7)`;
      ctx.shadowBlur = radius * 2;

      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2 * Math.PI);
      ctx.fill();

      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawCrescentMoon(ctx, x, y, radius, hue) {
      ctx.save();
      ctx.translate(x, y);

      const grad = ctx.createRadialGradient(-radius*0.2, -radius*0.2, radius*0.1, 0, 0, radius);
      grad.addColorStop(0, `hsla(${hue}, 90%, 85%, 1)`);
      grad.addColorStop(0.5, `hsla(${hue}, 80%, 75%, 0.95)`);
      grad.addColorStop(1, `hsla(${hue}, 70%, 60%, 0.8)`);

      ctx.fillStyle = grad;
      ctx.shadowColor = `hsla(${hue}, 90%, 80%, 0.9)`;
      ctx.shadowBlur = radius * 1.5;

      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2 * Math.PI);
      ctx.fill();

      ctx.globalCompositeOperation = 'destination-out';
      ctx.shadowBlur = 0;
      ctx.beginPath();
      ctx.arc(radius * 0.35, -radius * 0.15, radius * 0.85, 0, 2 * Math.PI);
      ctx.fillStyle = '#000';
      ctx.fill();

      ctx.globalCompositeOperation = 'source-over';

      ctx.shadowColor = `hsla(${hue}, 100%, 85%, 0.6)`;
      ctx.shadowBlur = radius * 0.8;
      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2 * Math.PI);
      ctx.strokeStyle = `hsla(${hue}, 80%, 90%, 0.5)`;
      ctx.lineWidth = 1.5;
      ctx.stroke();

      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawBackgroundStars(ctx, count, baseHue) {
      for (let i = 0; i < count; i++) {
        const angle = SECTORS[10].start + Math.random() * (SECTORS[10].end - SECTORS[10].start);
        const dist = R * 0.05 + Math.random() * (R * 0.85);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        const hue = (baseHue + Math.random() * 60) % 360;
        const radius = 0.8 + Math.random() * 2.5;
        const alpha = 0.3 + Math.random() * 0.5;

        ctx.save();
        ctx.translate(px, py);
        ctx.fillStyle = `hsla(${hue}, 80%, 75%, ${alpha})`;
        ctx.shadowColor = `hsla(${hue}, 80%, 70%, 0.4)`;
        ctx.shadowBlur = radius * 1.5;
        ctx.beginPath();
        ctx.arc(0, 0, radius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.restore();
      }
    }

    function drawCrescentStarrySpace(ctx) {
      const grad = ctx.createLinearGradient(CX, CY - R, CX, CY + R);
      grad.addColorStop(0, '#0a0e2a');
      grad.addColorStop(0.4, '#12183a');
      grad.addColorStop(0.7, '#1a1a3a');
      grad.addColorStop(1, '#0f1525');
      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[10].start, SECTORS[10].end);
      ctx.closePath();
      ctx.clip();

      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      drawBackgroundStars(ctx, 60, 40);

      const moonAngle = SECTORS[10].start + (SECTORS[10].end - SECTORS[10].start) * 0.45;
      const moonDist = R * 0.35;
      const moonX = CX + Math.cos(moonAngle) * moonDist;
      const moonY = CY + Math.sin(moonAngle) * moonDist - R * 0.1;
      drawCrescentMoon(ctx, moonX, moonY, 35, 45);

      for (let i = 0; i < 32; i++) {
        const angle = SECTORS[10].start + Math.random() * (SECTORS[10].end - SECTORS[10].start);
        const dist = R * 0.1 + Math.random() * (R * 0.7);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        const starType = Math.floor(Math.random() * 4);
        const hue = Math.floor(Math.random() * 360);
        const size = 4 + Math.random() * 12;

        switch (starType) {
          case 0: drawCircleStar(ctx, px, py, size * 0.8, hue); break;
          case 1: drawBrightStar(ctx, px, py, size * 0.9, hue); break;
          case 2: drawStarShape(ctx, px, py, size, hue); break;
          case 3: drawTinyStar(ctx, px, py, size * 0.5, hue); break;
        }
      }

      for (let i = 0; i < 20; i++) {
        const angle = SECTORS[10].start + Math.random() * (SECTORS[10].end - SECTORS[10].start);
        const dist = R * 0.05 + Math.random() * (R * 0.75);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        const hue = Math.floor(Math.random() * 360);
        drawTinyStar(ctx, px, py, 2 + Math.random() * 5, hue);
      }

      for (let i = 0; i < 8; i++) {
        const offsetAngle = Math.random() * 2 * Math.PI;
        const offsetDist = 45 + Math.random() * 30;
        const px = moonX + Math.cos(offsetAngle) * offsetDist;
        const py = moonY + Math.sin(offsetAngle) * offsetDist;

        const hue = Math.floor(Math.random() * 360);
        if (i % 2 === 0) {
          drawBrightStar(ctx, px, py, 6 + Math.random() * 8, hue);
        } else {
          drawCircleStar(ctx, px, py, 5 + Math.random() * 7, hue);
        }
      }

      ctx.font = "26px 'Abril Fatface', cursive";
      ctx.fillStyle = '#e0e7ff';
      ctx.shadowColor = '#aaccff';
      ctx.shadowBlur = 18;
      ctx.fillText("LUNA", CX+R*0.2, CY-R*0.25);
      ctx.font = "16px 'Special Elite', monospace";
      ctx.fillStyle = '#c9d8ff';
      ctx.fillText("starry night", CX+R*0.25, CY-R*0.05);
      ctx.shadowBlur = 0;

      ctx.restore();
    }
	
	    // ========== セクション11: クロノス・ブラス空間 ==========
    function drawBrassGear(ctx, gx, gy, outerR, teethCount, hueBase) {
      ctx.save();
      ctx.translate(gx, gy);

      const innerR = outerR * 0.72;
      const midR = outerR - 8;
      const holeR = outerR * 0.18;
      const numPoints = teethCount * 2;

      ctx.beginPath();
      ctx.lineJoin = "bevel";
      for (let n = 0; n < numPoints; n++) {
        const radius = (n % 2 === 0) ? outerR : innerR;
        const theta = ((Math.PI * 2) / numPoints) * (n + 1);
        const x = radius * Math.sin(theta);
        const y = radius * Math.cos(theta);
        if (n === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.closePath();

      const grad = ctx.createLinearGradient(-outerR/2, -outerR/2, outerR/2, outerR/2);
      grad.addColorStop(0, `hsl(${hueBase}, 75%, 65%)`);
      grad.addColorStop(0.5, `hsl(${hueBase}, 80%, 45%)`);
      grad.addColorStop(1, `hsl(${hueBase + 5}, 70%, 30%)`);

      ctx.fillStyle = grad;
      ctx.shadowColor = `hsl(${hueBase}, 60%, 20%)`;
      ctx.shadowBlur = 12;
      ctx.fill();
      ctx.strokeStyle = `hsl(${hueBase}, 60%, 25%)`;
      ctx.lineWidth = 2.5;
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(0, 0, midR, 0, 2 * Math.PI);
      const bodyGrad = ctx.createRadialGradient(-midR*0.3, -midR*0.3, 2, 0, 0, midR);
      bodyGrad.addColorStop(0, `hsl(${hueBase}, 70%, 70%)`);
      bodyGrad.addColorStop(0.5, `hsl(${hueBase}, 75%, 50%)`);
      bodyGrad.addColorStop(1, `hsl(${hueBase + 10}, 70%, 35%)`);
      ctx.fillStyle = bodyGrad;
      ctx.fill();
      ctx.strokeStyle = `hsl(${hueBase}, 60%, 25%)`;
      ctx.lineWidth = 2.5;
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(0, 0, holeR, 0, 2 * Math.PI);
      ctx.fillStyle = '#1a1208';
      ctx.shadowBlur = 8;
      ctx.fill();
      ctx.strokeStyle = `hsl(${hueBase}, 70%, 45%)`;
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.shadowBlur = 4;
      ctx.fillStyle = '#1a1208';
      for (let s = 0; s < 4; s++) {
        const angle = (s * Math.PI/2) + 0.3;
        const spokeX = Math.cos(angle) * midR * 0.55;
        const spokeY = Math.sin(angle) * midR * 0.55;
        ctx.beginPath();
        ctx.arc(spokeX, spokeY, holeR * 0.7, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = `hsl(${hueBase}, 60%, 40%)`;
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }

      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawMainspring(ctx, x, y, maxR, hueBase) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(Math.random() * Math.PI * 2);

      const turns = 4.5;
      const a = 2;
      const b = maxR / (turns * 2 * Math.PI) * 1.2;

      ctx.beginPath();
      ctx.lineWidth = maxR * 0.12;
      ctx.lineCap = 'round';

      const grad = ctx.createLinearGradient(-maxR*0.3, -maxR*0.3, maxR*0.3, maxR*0.3);
      grad.addColorStop(0, `hsl(${hueBase}, 80%, 60%)`);
      grad.addColorStop(0.5, `hsl(${hueBase + 8}, 75%, 45%)`);
      grad.addColorStop(1, `hsl(${hueBase + 15}, 70%, 30%)`);

      ctx.strokeStyle = grad;
      ctx.shadowColor = `hsl(${hueBase}, 60%, 20%)`;
      ctx.shadowBlur = 10;

      let theta = 0;
      let first = true;
      while (theta < turns * 2 * Math.PI) {
        const r = a + b * theta;
        if (r > maxR * 0.95) break;

        const px = r * Math.cos(theta);
        const py = r * Math.sin(theta);
        if (first) {
          ctx.moveTo(px, py);
          first = false;
        } else {
          ctx.lineTo(px, py);
        }
        theta += 0.08;
      }
      ctx.stroke();

      ctx.shadowBlur = 6;
      ctx.beginPath();
      ctx.arc(0, 0, maxR * 0.15, 0, 2 * Math.PI);
      const centerGrad = ctx.createRadialGradient(-2, -2, 1, 0, 0, maxR * 0.15);
      centerGrad.addColorStop(0, `hsl(${hueBase}, 85%, 70%)`);
      centerGrad.addColorStop(1, `hsl(${hueBase + 10}, 75%, 35%)`);
      ctx.fillStyle = centerGrad;
      ctx.fill();
      ctx.strokeStyle = `hsl(${hueBase}, 60%, 25%)`;
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.shadowBlur = 0;
      ctx.restore();
    }

    function drawBrassRivet(ctx, x, y, radius, hueBase) {
      ctx.save();
      ctx.translate(x, y);

      const grad = ctx.createRadialGradient(-radius*0.3, -radius*0.3, 1, 0, 0, radius);
      grad.addColorStop(0, `hsl(${hueBase}, 80%, 75%)`);
      grad.addColorStop(0.4, `hsl(${hueBase}, 75%, 55%)`);
      grad.addColorStop(1, `hsl(${hueBase + 5}, 70%, 35%)`);

      ctx.fillStyle = grad;
      ctx.shadowColor = `hsl(${hueBase}, 50%, 20%)`;
      ctx.shadowBlur = 8;
      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.strokeStyle = `hsl(${hueBase}, 60%, 30%)`;
      ctx.lineWidth = 1.5;
      ctx.stroke();

      ctx.shadowBlur = 3;
      ctx.beginPath();
      ctx.arc(0, 0, radius * 0.35, 0, 2 * Math.PI);
      ctx.fillStyle = '#1a1208';
      ctx.fill();

      ctx.restore();
    }

    function drawBrassPlate(ctx, x, y, w, h, hueBase, rotate) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(rotate);

      const grad = ctx.createLinearGradient(-w/2, -h/2, w/2, h/2);
      grad.addColorStop(0, `hsl(${hueBase}, 70%, 65%)`);
      grad.addColorStop(0.5, `hsl(${hueBase + 5}, 75%, 45%)`);
      grad.addColorStop(1, `hsl(${hueBase + 10}, 65%, 30%)`);

      ctx.fillStyle = grad;
      ctx.shadowColor = `hsl(${hueBase}, 50%, 15%)`;
      ctx.shadowBlur = 12;
      ctx.beginPath();
      ctx.rect(-w/2, -h/2, w, h);
      ctx.fill();
      ctx.strokeStyle = `hsl(${hueBase}, 60%, 25%)`;
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.shadowBlur = 4;
      ctx.strokeStyle = `hsl(${hueBase}, 50%, 40%)`;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.rect(-w/2 + 3, -h/2 + 3, w - 6, h - 6);
      ctx.stroke();

      ctx.restore();
    }

    function drawChronosDial(ctx, x, y, radius, hueBase) {
      ctx.save();
      ctx.translate(x, y);

      const grad = ctx.createRadialGradient(-radius*0.2, -radius*0.2, 2, 0, 0, radius);
      grad.addColorStop(0, `hsl(${hueBase}, 75%, 70%)`);
      grad.addColorStop(0.6, `hsl(${hueBase + 5}, 70%, 45%)`);
      grad.addColorStop(1, `hsl(${hueBase + 10}, 65%, 25%)`);

      ctx.fillStyle = grad;
      ctx.shadowColor = `hsl(${hueBase}, 50%, 15%)`;
      ctx.shadowBlur = 14;
      ctx.beginPath();
      ctx.arc(0, 0, radius, 0, 2 * Math.PI);
      ctx.fill();
      ctx.strokeStyle = `hsl(${hueBase}, 60%, 30%)`;
      ctx.lineWidth = 3;
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(0, 0, radius * 0.7, 0, 2 * Math.PI);
      ctx.strokeStyle = `hsl(${hueBase}, 50%, 35%)`;
      ctx.lineWidth = 1.5;
      ctx.stroke();

      ctx.shadowBlur = 2;
      ctx.font = `bold ${radius * 0.35}px 'Cinzel', serif`;
      ctx.fillStyle = `hsl(${hueBase}, 40%, 20%)`;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      const symbols = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII'];
      for (let i = 0; i < 12; i++) {
        const angle = (i * 30 - 90) * Math.PI/180;
        const tx = Math.cos(angle) * radius * 0.55;
        const ty = Math.sin(angle) * radius * 0.55;
        ctx.fillText(symbols[i], tx, ty);
      }

      ctx.restore();
    }

    function drawSmallBrassGear(ctx, x, y, radius, hueBase) {
      ctx.save();
      ctx.translate(x, y);

      const teeth = 6 + Math.floor(Math.random() * 4);
      const numPoints = teeth * 2;
      const innerR = radius * 0.75;

      ctx.beginPath();
      ctx.lineJoin = "bevel";
      for (let n = 0; n < numPoints; n++) {
        const r = (n % 2 === 0) ? radius : innerR;
        const theta = ((Math.PI * 2) / numPoints) * (n + 1);
        const px = r * Math.sin(theta);
        const py = r * Math.cos(theta);
        if (n === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.closePath();

      const grad = ctx.createRadialGradient(-radius*0.2, -radius*0.2, 1, 0, 0, radius);
      grad.addColorStop(0, `hsl(${hueBase}, 80%, 70%)`);
      grad.addColorStop(1, `hsl(${hueBase + 8}, 70%, 35%)`);

      ctx.fillStyle = grad;
      ctx.shadowColor = `hsl(${hueBase}, 50%, 20%)`;
      ctx.shadowBlur = 8;
      ctx.fill();
      ctx.strokeStyle = `hsl(${hueBase}, 60%, 25%)`;
      ctx.lineWidth = 1.5;
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(0, 0, radius * 0.25, 0, 2 * Math.PI);
      ctx.fillStyle = '#1a1208';
      ctx.fill();

      ctx.restore();
    }

    function drawBrassDust(ctx, x, y, count, hueBase) {
      ctx.save();
      ctx.translate(x, y);

      for (let i = 0; i < count; i++) {
        const dx = (Math.random() - 0.5) * 40;
        const dy = (Math.random() - 0.5) * 40;
        const size = 1 + Math.random() * 4;
        const alpha = 0.15 + Math.random() * 0.3;

        ctx.fillStyle = `hsla(${hueBase + Math.random()*20}, ${60 + Math.random()*30}%, ${40 + Math.random()*30}%, ${alpha})`;
        ctx.shadowColor = `hsl(${hueBase}, 50%, 30%)`;
        ctx.shadowBlur = 3;
        ctx.beginPath();
        ctx.arc(dx, dy, size, 0, 2 * Math.PI);
        ctx.fill();
      }

      ctx.restore();
    }

    function drawConnectingRod(ctx, x1, y1, x2, y2, width, hueBase) {
      ctx.save();

      const grad = ctx.createLinearGradient(x1, y1, x2, y2);
      grad.addColorStop(0, `hsl(${hueBase}, 75%, 60%)`);
      grad.addColorStop(0.5, `hsl(${hueBase + 5}, 70%, 45%)`);
      grad.addColorStop(1, `hsl(${hueBase + 10}, 65%, 30%)`);

      ctx.strokeStyle = grad;
      ctx.lineWidth = width;
      ctx.lineCap = 'round';
      ctx.shadowColor = `hsl(${hueBase}, 50%, 20%)`;
      ctx.shadowBlur = 8;

      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.stroke();

      drawBrassRivet(ctx, x1, y1, width * 0.8, hueBase);
      drawBrassRivet(ctx, x2, y2, width * 0.8, hueBase);

      ctx.restore();
    }

    function drawChronosBrassSpace(ctx) {
      const grad = ctx.createRadialGradient(CX-15, CY-10, 10, CX, CY, R);
      grad.addColorStop(0, '#2a1e12');
      grad.addColorStop(0.5, '#1a1208');
      grad.addColorStop(1, '#0a0602');
      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      ctx.save();
      ctx.beginPath();
      ctx.moveTo(CX, CY);
      ctx.arc(CX, CY, R*0.95, SECTORS[11].start, SECTORS[11].end);
      ctx.closePath();
      ctx.clip();

      ctx.fillStyle = grad;
      ctx.fillRect(CX-R, CY-R, R*2, R*2);

      for (let i = 0; i < 12; i++) {
        const angle = SECTORS[11].start + Math.random() * (SECTORS[11].end - SECTORS[11].start);
        const dist = R * 0.15 + Math.random() * (R * 0.65);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;
        drawBrassDust(ctx, px, py, 8 + Math.floor(Math.random() * 12), 38);
      }

      for (let i = 0; i < 12; i++) {
        const angle = SECTORS[11].start + Math.random() * (SECTORS[11].end - SECTORS[11].start);
        const dist = R * 0.15 + Math.random() * (R * 0.6);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        const hueBase = 35 + Math.random() * 15;
        const radius = 18 + Math.random() * 28;
        const teeth = 8 + Math.floor(Math.random() * 6);

        drawBrassGear(ctx, px, py, radius, teeth, hueBase);
      }

      for (let i = 0; i < 4; i++) {
        const angle = SECTORS[11].start + Math.random() * (SECTORS[11].end - SECTORS[11].start);
        const dist = R * 0.2 + Math.random() * (R * 0.45);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        const hueBase = 38 + Math.random() * 12;
        const maxR = 18 + Math.random() * 25;

        drawMainspring(ctx, px, py, maxR, hueBase);
      }

      for (let i = 0; i < 2; i++) {
        const angle = SECTORS[11].start + 0.2 + i * 0.3;
        const dist = R * 0.3 + i * R * 0.15;
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        drawChronosDial(ctx, px, py, 25 + i * 8, 40 + i * 5);
      }

      for (let i = 0; i < 3; i++) {
        const angle = SECTORS[11].start + Math.random() * (SECTORS[11].end - SECTORS[11].start);
        const dist = R * 0.2 + Math.random() * (R * 0.5);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        const w = 20 + Math.random() * 30;
        const h = 8 + Math.random() * 15;
        drawBrassPlate(ctx, px, py, w, h, 38 + Math.random()*10, Math.random()*Math.PI);
      }

      for (let i = 0; i < 8; i++) {
        const angle = SECTORS[11].start + Math.random() * (SECTORS[11].end - SECTORS[11].start);
        const dist = R * 0.1 + Math.random() * (R * 0.65);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        drawSmallBrassGear(ctx, px, py, 8 + Math.random() * 14, 35 + Math.random()*15);
      }

      for (let i = 0; i < 6; i++) {
        const angle = SECTORS[11].start + Math.random() * (SECTORS[11].end - SECTORS[11].start);
        const dist = R * 0.1 + Math.random() * (R * 0.7);
        const px = CX + Math.cos(angle) * dist;
        const py = CY + Math.sin(angle) * dist;

        drawBrassRivet(ctx, px, py, 4 + Math.random() * 8, 38 + Math.random()*12);
      }

      for (let i = 0; i < 3; i++) {
        const angle1 = SECTORS[11].start + Math.random() * (SECTORS[11].end - SECTORS[11].start);
        const dist1 = R * 0.15 + Math.random() * (R * 0.4);
        const angle2 = angle1 + (Math.random() - 0.5) * 0.5;
        const dist2 = dist1 + (Math.random() - 0.5) * R * 0.25;
        const px1 = CX + Math.cos(angle1) * dist1;
        const py1 = CY + Math.sin(angle1) * dist1;
        const px2 = CX + Math.cos(angle2) * dist2;
        const py2 = CY + Math.sin(angle2) * dist2;

        drawConnectingRod(ctx, px1, py1, px2, py2, 3 + Math.random() * 4, 38);
      }

      ctx.font = "bold 28px 'Cinzel', serif";
      ctx.fillStyle = '#d4af37';
      ctx.shadowColor = '#3d2e1e';
      ctx.shadowBlur = 18;
      ctx.fillText("CHRONOS", CX+R*0.15, CY-R*0.2);
      ctx.font = "18px 'Special Elite', monospace";
      ctx.fillStyle = '#c9a96e';
      ctx.fillText("BRASS·WORK", CX+R*0.2, CY-R*0.02);
      ctx.shadowBlur = 0;

      ctx.restore();
    }

    // 他のセクションの描画関数は未実装（グレー単色）のまま
    const drawers = [
      drawBrutalistSpace,                                                          // 0 ★
      drawGearEngineSpace,                                                         // 1
      drawPixelRetroSpace, // 2
      drawOrganicSpace, // 3
      drawMaximalChaosSpace, // 4
      drawCyberpunkSpace, // 5
      drawFireFieldSpace, // 6
      drawMinimalistSpace, // 7
      drawBubbleFantasySpace, // 8
      drawBalloonSkySpace, // 9
      drawCrescentStarrySpace, // 10
      drawChronosBrassSpace                                                           // 11
    ];

// 中央18頂点星を描画（オフスクリーン/メイン共通）
function draw18PointStar(targetCtx) {
  const outerR = IR * 0.9, innerR = IR * 0.45;
  const points = 18;
  const rot = Math.PI / 2;
  targetCtx.beginPath();
  for (let i = 0; i <= points * 2; i++) {
    const r = (i % 2 === 0) ? outerR : innerR;
    const angle = (i * Math.PI / points) - rot;
    const x = CX + r * Math.cos(angle);
    const y = CY + r * Math.sin(angle);
    if (i === 0) targetCtx.moveTo(x, y);
    else targetCtx.lineTo(x, y);
  }
  targetCtx.closePath();
  targetCtx.fillStyle = '#f9e0a8';
  targetCtx.shadowColor = '#d4af37';
  targetCtx.shadowBlur = 20;
  targetCtx.fill();
  targetCtx.shadowBlur = 0;
  targetCtx.strokeStyle = '#a67c45';
  targetCtx.lineWidth = 3;
  targetCtx.stroke();
}
    function drawHands(hourAngle, minAngle, secAngle, themeIdx) {
      ctx.save();
      ctx.translate(CX, CY);
      
      const style = handThemes[themeIdx % handThemes.length];
      
      // 时针
      ctx.rotate(hourAngle);
      ctx.beginPath();
      ctx.moveTo(-10, 12); ctx.lineTo(0, -R*0.42); ctx.lineTo(10, 12); ctx.closePath();
      ctx.fillStyle = style.hour; ctx.shadowColor = style.shadow; ctx.shadowBlur = 18; ctx.fill();
      ctx.strokeStyle = '#f0e6d2'; ctx.lineWidth = 2.2; ctx.stroke();
      
      // 分针
      ctx.rotate(minAngle - hourAngle);
      ctx.beginPath();
      ctx.moveTo(-8, 15); ctx.lineTo(0, -R*0.62); ctx.lineTo(8, 15); ctx.closePath();
      ctx.fillStyle = style.min; ctx.shadowBlur = 16; ctx.fill();
      ctx.strokeStyle = '#23211f'; ctx.lineWidth = 2; ctx.stroke();
      
      // 秒针
      ctx.rotate(secAngle - minAngle);
      ctx.beginPath();
      ctx.moveTo(-4, 20); ctx.lineTo(0, -R*0.78); ctx.lineTo(4, 20); ctx.closePath();
      ctx.fillStyle = style.sec; ctx.shadowBlur = 22; ctx.shadowColor = style.shadow; ctx.fill();
      ctx.strokeStyle = 'white'; ctx.lineWidth = 1.8; ctx.stroke();
      
      ctx.shadowBlur = 0;
      ctx.restore();
    }
function drawBackground() {
  bgCtx.clearRect(0, 0, SIZE, SIZE);
  
  for (let i = 0; i < 12; i++) {
    bgCtx.save();
    bgCtx.beginPath();
    bgCtx.moveTo(CX, CY);
    bgCtx.arc(CX, CY, R, SECTORS[i].start, SECTORS[i].end);
    bgCtx.closePath();
    bgCtx.clip();
    
    drawers[i](bgCtx);
    
    bgCtx.beginPath();
    bgCtx.moveTo(CX, CY);
    bgCtx.arc(CX, CY, R, SECTORS[i].start, SECTORS[i].end);
    bgCtx.closePath();
    bgCtx.strokeStyle = '#2b2824';
    bgCtx.lineWidth = 2.8;
    bgCtx.stroke();
    
    bgCtx.restore();
  }
  
  // 中心円（下地）
  bgCtx.beginPath();
  bgCtx.arc(CX, CY, IR * 1.05, 0, 2 * Math.PI);
  bgCtx.fillStyle = '#17191c';
  bgCtx.shadowColor = '#b9a577';
  bgCtx.shadowBlur = 16;
  bgCtx.fill();
  bgCtx.shadowBlur = 0;
  bgCtx.strokeStyle = '#b9a577';
  bgCtx.lineWidth = 5;
  bgCtx.stroke();
  
  // 18頂点星
  draw18PointStar(bgCtx);
  
  // 数字
  bgCtx.font = "bold 22px 'Cinzel', serif";
  bgCtx.fillStyle = '#e5d5bc';
  bgCtx.shadowColor = '#0f0f0f';
  bgCtx.shadowBlur = 6;
  for (let i = 1; i <= 12; i++) {
    let angle = (i * 30 - 90) * Math.PI / 180;
    let tx = CX + Math.cos(angle) * (R * 0.78);
    let ty = CY + Math.sin(angle) * (R * 0.78);
    bgCtx.fillText(i.toString(), tx - 12, ty + 8);
  }
  bgCtx.shadowBlur = 0;
}
function drawForeground(hourAngle, minAngle, secAngle, themeIdx) {
  // オフスクリーン背景をメインCanvasにコピー
  ctx.clearRect(0, 0, SIZE, SIZE);
  ctx.drawImage(bgCanvas, 0, 0);
  
  // 針を描画
  drawHands(hourAngle, minAngle, secAngle, themeIdx);
  
  // 中心キャップ
  ctx.beginPath();
  ctx.arc(CX, CY, 12, 0, 2 * Math.PI);
  ctx.fillStyle = '#f2e3c9';
  ctx.shadowBlur = 14;
  ctx.shadowColor = '#d4af37';
  ctx.fill();
  ctx.strokeStyle = '#5d4e37';
  ctx.lineWidth = 3;
  ctx.stroke();
  ctx.shadowBlur = 0;
    // 前景にも小さな星（輝き強調）
  draw18PointStar(ctx);
}
function updateClock(timestamp) {
  const now = new Date();
  const h = now.getHours(), m = now.getMinutes(), s = now.getSeconds(), ms = now.getMilliseconds();
  const secAngle = (s + ms / 1000) * 6 * Math.PI / 180;
  const minAngle = (m + s / 60) * 6 * Math.PI / 180;
  const hourAngle = ((h % 12) + m / 60) * 30 * Math.PI / 180;

  // 背景を1秒ごとに更新
  if (!lastBackgroundUpdate || timestamp - lastBackgroundUpdate >= BACKGROUND_INTERVAL) {
    drawBackground();
    lastBackgroundUpdate = timestamp;
    
    // 外部背景色をランダムなテーマカラーに変更
    if (enableBodyBgAutoChange) {
      const randomBgIndex = Math.floor(Math.random() * themeBgColors.length);
      document.body.style.backgroundColor = themeBgColors[randomBgIndex];
    }
    // 針テーマもランダムに変更
    currentHandTheme = Math.floor(Math.random() * handThemes.length);
  }

  drawForeground(hourAngle, minAngle, secAngle, currentHandTheme);
  
  // デジタル表示更新
  digitalEl.textContent = `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  
  requestAnimationFrame(updateClock);
}
    // ========== アニメーション初期化 ==========
    
    // 初回背景描画
    drawBackground();
    lastBackgroundUpdate = performance.now();

    // アニメーション開始
    requestAnimationFrame(updateClock);

// UIパネル背景色のRGB制御
const rInput = document.getElementById('bgR');
const gInput = document.getElementById('bgG');
const bInput = document.getElementById('bgB');
const clockContainer = document.querySelector('.clock-container');

function updateContainerBg() {
  const r = rInput.value;
  const g = gInput.value;
  const b = bInput.value;
  clockContainer.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
}

rInput.addEventListener('input', updateContainerBg);
gInput.addEventListener('input', updateContainerBg);
bInput.addEventListener('input', updateContainerBg);

// 初期値で一度設定（現在のCSS背景色 #1c1f22 → RGB(28,31,34)）
rInput.value = 178;
gInput.value = 78;
bInput.value = 230;
updateContainerBg();

// ボタンで自動変化のトグル
const toggleBtn = document.getElementById('toggleBodyBg');
toggleBtn.addEventListener('click', () => {
  enableBodyBgAutoChange = !enableBodyBgAutoChange;
  toggleBtn.textContent = enableBodyBgAutoChange ? '⏸ 背景自動変化を停止' : '▶ 背景自動変化を再開';
});
    // リサイズ時は背景を再生成
    window.addEventListener('resize', () => {
      drawBackground();
      lastBackgroundUpdate = performance.now();
    });
  })();
</script>
</body>
</html>

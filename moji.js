const { createCanvas, registerFont } = require('canvas');
const fs = require('fs');

// Windowsならメイリオフォントなどを登録できるチュー
// フォントファイルのパスは環境に合わせて変えてチュー
registerFont('C:/Windows/Fonts/meiryo.ttc', { family: 'Meiryo' });

const WIDTH = 32;
const HEIGHT = 32;
const FONT_SIZE = 28;
const OUTPUT_FILE = 'output.txt';

// moji.jsonを読み込みチュー
const mojiData = JSON.parse(fs.readFileSync('moji.json', 'utf-8'));
const mojiStr = mojiData.moji; // 例: "あいうえお"

const canvas = createCanvas(WIDTH, HEIGHT);
const ctx = canvas.getContext('2d');

let output = '';

for (const ch of mojiStr) {
    // 背景白
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, WIDTH, HEIGHT);

    // 文字を黒で描画
    ctx.fillStyle = 'black';
    ctx.font = `${FONT_SIZE}px Meiryo`;
    ctx.textBaseline = 'middle';
    ctx.textAlign = 'center';
    ctx.fillText(ch, WIDTH / 2, HEIGHT / 2);

    // 画像データ取得
    const imgData = ctx.getImageData(0, 0, WIDTH, HEIGHT);

    // 黒を1、白を0に変換
    let bits = '';
    for (let i = 0; i < imgData.data.length; i += 4) {
        const r = imgData.data[i];
        const g = imgData.data[i + 1];
        const b = imgData.data[i + 2];
        // グレースケール簡易判定
        const gray = 0.299 * r + 0.587 * g + 0.114 * b;
        bits += gray < 128 ? '1' : '0';
    }

    output += bits + '\n';
}

// output.txtに書き込み
fs.writeFileSync(OUTPUT_FILE, output);

console.log('完了チュー！');

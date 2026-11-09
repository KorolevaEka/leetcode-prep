// Сторож зацикливания для Java в браузере: CheerpJ крутит Java в главном потоке страницы, и `while(true){}`
// вешает вкладку навсегда (Java-потоки внутри тугого цикла не вытесняются, iframe того же сайта виснет вместе
// со страницей). Поэтому перед компиляцией вставляем __LCT.tick() в начало тел циклов и методов кода
// пользователя; tick() после дедлайна печатает «Таймаут…» и завершает программу.
// Тело в фигурных скобках — `{ __LCT.tick();`; без скобок (и пустое `while (x);`) — в условие:
// `while (__LCT.tick() && (x))`, `for (a; __LCT.tick() && (b); c)`. Переводы строк не добавляются,
// поэтому номера строк в ошибках javac совпадают.
// ponytail: лексер, а не парсер; если вставка всё же ломает компиляцию, java.js компилирует код без сторожа.

const TICK = "__LCT.tick()";
const KEYWORDS = new Set(("abstract assert break case catch class continue default do else enum extends final finally " +
  "for if implements import instanceof interface native new package private protected public record return static " +
  "super switch synchronized this throw throws transient try volatile while yield").split(" "));
const TYPES = new Set("boolean byte char short int long float double void var".split(" "));

function tokenize(src) {
  const toks = [];
  let i = 0;
  while (i < src.length) {
    const c = src[i];
    if (/\s/.test(c)) { i++; continue; }
    if (src.startsWith("//", i)) { const e = src.indexOf("\n", i); i = e < 0 ? src.length : e; continue; }
    if (src.startsWith("/*", i)) { const e = src.indexOf("*/", i + 2); i = e < 0 ? src.length : e + 2; continue; }
    if (src.startsWith('"""', i)) {
      let j = i + 3;
      while (j < src.length && !src.startsWith('"""', j)) j += src[j] === "\\" ? 2 : 1;
      toks.push({ t: "lit", s: i }); i = j + 3; continue;
    }
    if (c === '"' || c === "'") {
      let j = i + 1;
      while (j < src.length && src[j] !== c && src[j] !== "\n") j += src[j] === "\\" ? 2 : 1;
      toks.push({ t: "lit", s: i }); i = j + 1; continue;
    }
    const w = /^[\p{L}\p{N}_$]+/u.exec(src.slice(i, i + 200));
    if (w) { toks.push({ t: w[0], s: i, id: true }); i += w[0].length; continue; }
    toks.push({ t: c, s: i }); i++;
  }
  return toks;
}

function closing(toks, i) { // i — индекс "(", возвращает индекс парной ")"
  for (let d = 0; i < toks.length; i++) {
    if (toks[i].t === "(") d++;
    else if (toks[i].t === ")" && --d === 0) return i;
  }
  return -1;
}

export function guard(src) {
  const toks = tokenize(src), ins = [], doBraces = new Set(), doTails = new Set(), stack = [];
  const at = (pos, text) => ins.push([pos, text]);
  const afterBrace = k => at(toks[k].s + 1, ` ${TICK};`);
  const wrap = (a, b) => { at(toks[a].s, `${TICK} && (`); at(toks[b].s + toks[b].t.length, ")"); }; // токены a..b
  for (let i = 0; i < toks.length; i++) {
    const { t } = toks[i], next = toks[i + 1]?.t;
    if (t === "{") stack.push(i);
    if (t === "}" && doBraces.has(stack.pop()) && toks[i + 1]?.t === "while") doTails.add(i + 1);
    if (t === "do" && next === "{") { doBraces.add(i + 1); afterBrace(i + 1); continue; }
    if ((t === "while" || t === "for") && next === "(") {
      const j = closing(toks, i + 1);
      if (j < 0) continue;
      if (toks[j + 1]?.t === "{") { afterBrace(j + 1); continue; }
      if (t === "while") { if (!doTails.has(i) && j > i + 2) wrap(i + 2, j - 1); continue; } // хвост do {…} уже с tick
      const semis = [];
      for (let k = i + 2, d = 0; k < j; k++) {
        const x = toks[k].t;
        if (x === "(" || x === "{" || x === "[") d++;
        else if (x === ")" || x === "}" || x === "]") d--;
        else if (x === ";" && d === 0) semis.push(k);
      }
      if (semis.length !== 2) continue; // for-each конечен
      const [a, b] = semis;
      if (b === a + 1) at(toks[a].s + 1, TICK); else wrap(a + 1, b - 1);
      continue;
    }
    // метод: <тип|>|]> имя ( ... ) [throws A, B] {
    const prev = toks[i - 1];
    if (t === "(" && prev?.id && !KEYWORDS.has(prev.t) && !TYPES.has(prev.t)) {
      const pp = toks[i - 2];
      if (!pp || !(pp.t === ">" || pp.t === "]" || (pp.id && (TYPES.has(pp.t) || !KEYWORDS.has(pp.t))))) continue;
      const j = closing(toks, i);
      if (j < 0) continue;
      let k = j + 1;
      if (toks[k]?.t === "throws") while (toks[++k] && (toks[k].id || toks[k].t === "." || toks[k].t === ","));
      if (toks[k]?.t === "{") afterBrace(k);
    }
  }
  let out = src;
  for (const [pos, text] of ins.sort((x, y) => y[0] - x[0])) out = out.slice(0, pos) + text + out.slice(pos);
  return out;
}

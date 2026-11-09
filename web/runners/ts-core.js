// Компиляция TypeScript в памяти: общий для браузера и Node. `ts` и `readLib` приходят снаружи.
const OPTIONS = ts => ({
  strict: true, target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.CommonJS,
  moduleResolution: ts.ModuleResolutionKind.Node10, moduleDetection: ts.ModuleDetectionKind.Force,
  lib: ["lib.es2022.d.ts"], types: [], noEmitOnError: true, noEmit: false,
});

const norm = name => name.replace(/^\/+/, "");

// files: { "solution.ts": …, "solution.test.ts": …, "ts-harness.d.ts": … }; readLib("lib.es2022.d.ts") -> текст
export function compileAndRun(ts, files, readLib) {
  const options = OPTIONS(ts), js = {}, cache = new Map();
  const read = name => {
    name = norm(name);
    if (name in files) return files[name];
    const base = name.split("/").pop();
    if (/^lib\..*\.d\.ts$/.test(base)) return readLib(base);
    return undefined;
  };
  const host = {
    getSourceFile(name, languageVersion) {
      const text = read(name);
      if (text === undefined) return undefined;
      const key = norm(name);
      if (!cache.has(key)) cache.set(key, ts.createSourceFile(name, text, languageVersion, true));
      return cache.get(key);
    },
    getDefaultLibFileName: () => "/lib/lib.es2022.d.ts",
    getDefaultLibLocation: () => "/lib",
    writeFile: (name, text) => { js[norm(name)] = text; },
    getCurrentDirectory: () => "/",
    getCanonicalFileName: n => n,
    useCaseSensitiveFileNames: () => true,
    getNewLine: () => "\n",
    fileExists: name => read(name) !== undefined,
    readFile: read,
    directoryExists: () => true,
    getDirectories: () => [],
  };
  const roots = Object.keys(files).map(n => "/" + n);
  const program = ts.createProgram(roots, options, host);
  const diagnostics = ts.getPreEmitDiagnostics(program).filter(d => d.category === ts.DiagnosticCategory.Error).map(d => {
    const msg = `error TS${d.code}: ${ts.flattenDiagnosticMessageText(d.messageText, "\n")}`;
    if (!d.file) return msg;
    const { line, character } = d.file.getLineAndCharacterOfPosition(d.start);
    return `${norm(d.file.fileName)}(${line + 1},${character + 1}): ${msg}`;
  });
  if (!diagnostics.length) program.emit();
  return { diagnostics, js };
}

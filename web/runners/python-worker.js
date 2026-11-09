// Python + pytest в отдельном потоке: зависшее решение не вешает вкладку, его можно убить.
importScripts("https://cdn.jsdelivr.net/pyodide/v0.27.2/full/pyodide.js");

const ready = (async () => {
  const py = await loadPyodide();
  await py.loadPackage("micropip");
  await py.pyimport("micropip").install("pytest");
  py.runPython("import sys; sys.dont_write_bytecode = True");
  return py;
})();

onmessage = async ({ data: { subject, tests } }) => {
  let out = "";
  try {
    const py = await ready;
    const dec = new TextDecoder();
    const write = buf => { out += dec.decode(buf); return buf.length; };
    py.setStdout({ write });
    py.setStderr({ write });
    const dir = "/work";
    py.FS.mkdirTree(dir);
    py.FS.writeFile(`${dir}/solution.py`, subject);
    py.FS.writeFile(`${dir}/test_solution.py`, tests);
    const code = py.runPython(`
import sys, importlib, pytest
importlib.invalidate_caches()
for m in ("solution", "test_solution"):
    sys.modules.pop(m, None)
int(pytest.main(["-q", "-p", "no:cacheprovider", "--rootdir", "${dir}", "${dir}"]))
`);
    postMessage({ passed: code === 0, output: out, ...(code === 5 && { noTests: true }) });
  } catch (e) {
    postMessage({ passed: false, output: out + String(e) });
  }
};

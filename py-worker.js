// Python + pytest в отдельном потоке: зависшее решение не вешает вкладку, его можно убить.
importScripts("https://cdn.jsdelivr.net/pyodide/v0.27.2/full/pyodide.js");

const ready = (async () => {
  const py = await loadPyodide();
  await py.loadPackage("micropip");
  await py.pyimport("micropip").install("pytest");
  py.runPython("import sys; sys.dont_write_bytecode = True");
  return py;
})();

onmessage = async ({ data: { id, files } }) => {
  let out = "";
  try {
    const py = await ready;
    const dec = new TextDecoder();
    const write = buf => { out += dec.decode(buf); return buf.length; };
    py.setStdout({ write });
    py.setStderr({ write });
    const dir = "/tasks/" + id;
    py.FS.mkdirTree(dir);
    for (const [name, text] of Object.entries(files)) py.FS.writeFile(`${dir}/${name}`, text);
    const code = py.runPython(`
import sys, pytest
for m in ("solution", "test_solution"):
    sys.modules.pop(m, None)
int(pytest.main(["-q", "-p", "no:cacheprovider", "--rootdir", ${JSON.stringify(dir)}, ${JSON.stringify(dir)}]))
`);
    postMessage({ ok: code === 0, output: out });
  } catch (e) {
    postMessage({ ok: false, output: out + String(e) });
  }
};

function checkPythonONNXRuntime()
    try
        pe = pyenv;
        fprintf("Python usato da MATLAB: %s\n", string(pe.Executable));
    catch ME
        error("Python non configurato in MATLAB. Usare pyenv. Dettaglio: %s", ME.message);
    end

    try
        py.importlib.import_module("numpy");
        py.importlib.import_module("onnxruntime");
    catch ME
        error([ ...
            "Impossibile importare numpy/onnxruntime nell'ambiente Python di MATLAB." + newline + ...
            "Installare, nell'ambiente indicato da pyenv, con:" + newline + ...
            "  python -m pip install numpy onnxruntime" + newline + ...
            "Dettaglio: %s"], ME.message);
    end
end

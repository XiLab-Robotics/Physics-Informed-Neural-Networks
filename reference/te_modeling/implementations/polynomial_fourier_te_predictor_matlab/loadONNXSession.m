function sess = loadONNXSession(modelFile)
    ort = py.importlib.import_module("onnxruntime");
    sess = ort.InferenceSession(char(modelFile), ...
        pyargs("providers", py.list({"CPUExecutionProvider"})));
end

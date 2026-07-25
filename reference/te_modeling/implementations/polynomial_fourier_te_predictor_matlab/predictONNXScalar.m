function y = predictONNXScalar(sess, xRow)
    % Restituisce il primo scalare dell'output ONNX.
    % Rileva automaticamente il nome del primo ingresso e della prima uscita.
    np = py.importlib.import_module("numpy");

    inputs  = sess.get_inputs();
    outputs = sess.get_outputs();

    inputName  = char(inputs{1}.name);
    outputName = char(outputs{1}.name);

    xNp = np.array(xRow, pyargs("dtype", "float32"));
    xNp = xNp.reshape(int32(1), int32(numel(xRow)));

    yList = sess.run(py.list({outputName}), py.dict(pyargs(inputName, xNp)));
    yNp = np.asarray(yList{1}, pyargs("dtype", "float64")).reshape(int32(-1));
    yListFlat = cell(yNp.tolist());

    if isempty(yListFlat)
        error("Il modello ONNX non ha restituito valori.");
    end

    y = double(yListFlat{1});
end

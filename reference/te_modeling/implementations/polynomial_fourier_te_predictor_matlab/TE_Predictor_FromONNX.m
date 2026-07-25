close all
clear all
clc

%pyenv("Version","C:\Users\pietr\AppData\Local\Programs\Python\Python311\python.exe","ExecutionMode","OutOfProcess")

omega  = 300;     % [rpm]
torqueOut  = 1000;  % [Nm]
oilTemp     = 25;  % [°C]

ExpData=readmatrix("Experiments\300.0rpm1000.0Nm25.0deg.csv");

thetaStep_deg = 0.1;     % [deg]
theta_deg     = 0:thetaStep_deg:360;
theta_rad     = deg2rad(theta_deg);

%% Loading ONNX files

modelFiles.ampl0   = fullfile("ExtraTreesRegressor_ampl0.onnx");
modelFiles.ampl1   = fullfile("RandomForestRegressor_ampl1.onnx");
modelFiles.phase1  = fullfile("RandomForestRegressor_phase1.onnx");
modelFiles.ampl39  = fullfile("HistGradientBoostingRegressor_ampl39.onnx");
modelFiles.phase39 = fullfile("HistGradientBoostingRegressor_phase39.onnx");
modelFiles.ampl40  = fullfile("ExtraTreesRegressor_ampl40.onnx");
modelFiles.phase40 = fullfile("GradientBoostingRegressor_phase40.onnx");

% Check
checkPythonONNXRuntime();

% Sessions
sess.ampl0   = loadONNXSession(modelFiles.ampl0);
sess.ampl1   = loadONNXSession(modelFiles.ampl1);
sess.phase1  = loadONNXSession(modelFiles.phase1);
sess.ampl39  = loadONNXSession(modelFiles.ampl39);
sess.phase39 = loadONNXSession(modelFiles.phase39);
sess.ampl40  = loadONNXSession(modelFiles.ampl40);
sess.phase40 = loadONNXSession(modelFiles.phase40);

%Get data from models

x = single([omega, oilTemp, torqueOut]);

A0    = predictONNXScalar(sess.ampl0,   x);
A1    = predictONNXScalar(sess.ampl1,   x);
phi1  = predictONNXScalar(sess.phase1,  x);
A39   = predictONNXScalar(sess.ampl39,  x);
phi39 = predictONNXScalar(sess.phase39, x);
A40   = predictONNXScalar(sess.ampl40,  x);
phi40 = predictONNXScalar(sess.phase40, x);


%% TE Predictor
TE_deg = zeros(size(theta_rad));

for i = 1:numel(theta_rad)
    th = theta_rad(i);
    TE_deg(i) = A0;
    TE_deg(i) = TE_deg(i) + A1  * cos(1  * th + phi1);
    TE_deg(i) = TE_deg(i) + A39 * cos(39 * th + phi39);
    TE_deg(i) = TE_deg(i) + A40 * cos(40 * th + phi40);
end


%% Plot
plot(theta_deg, TE_deg,"-k", "LineWidth", 1.2);
hold on
plot(ExpData(:,1), ExpData(:,2),"-r", "LineWidth", 1.2);

grid on;
xlabel("\theta_{out} [deg]");
ylabel("TE [deg]");

legend ("ML", "Exp");


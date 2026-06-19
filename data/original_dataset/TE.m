%Analisi TE
clear all
clc
close all


filenames = [
%   
"Test_25deg_Torque_PreProcessing\100rpm\100.0rpm0.0Nm25.0deg.csv";...
"Test_25deg_Torque_PreProcessing\100rpm\100.0rpm1000.0Nm25.0deg.csv";

%
];

cycletime = 0.25; %ms  --> 4000Hz
RedRatio=81;



for i = 1 : numel(filenames)

getinfo{i} = regexp(filenames{i}, '\d+(?:\.\d+)?', 'match');
temp(i)   = str2double(getinfo{i}{1});
vel(i)    = str2double(getinfo{i}{2});
torque(i) = str2double(getinfo{i}{4});

InputExp{i} = readmatrix(filenames{i});
dataValid_fw{i} = InputExp{i}(:,5);
dataValid_bw{i} = InputExp{i}(:,6);

TotPosBosch_InputSide_fw{i} = InputExp{i}(dataValid_fw{i}==1,1);
TotPosReni_InputSide_fw{i} = InputExp{i}(dataValid_fw{i}==1,2);
TotPosReni_OutputSide_fw{i} = InputExp{i}(dataValid_fw{i}==1,3);
TorqueManner_OutputSide_fw{i} = InputExp{i}(dataValid_fw{i}==1,4);
TorqueManner_InputSide_fw{i} = InputExp{i}(dataValid_fw{i}==1,7);
OilTemperature_fw{i} = InputExp{i}(dataValid_fw{i} == 1, 8);
TorqueBosch_LoadMotor_fw{i} = InputExp{i}(dataValid_fw{i} == 1,10);
AbsPosReni_OutputSide_fw{i} = InputExp{i}(dataValid_fw{i} == 1, 11);

TotPosBosch_InputSide_bw{i} = InputExp{i}(dataValid_bw{i}==1,1);
TotPosReni_InputSide_bw{i} = InputExp{i}(dataValid_bw{i}==1,2);
TotPosReni_OutputSide_bw{i} = InputExp{i}(dataValid_bw{i}==1,3);
TorqueManner_OutputSide_bw{i} = InputExp{i}(dataValid_bw{i}==1,4);
TorqueManner_InputSide_bw{i} = InputExp{i}(dataValid_bw{i}==1,7);
OilTemperature_bw{i} = InputExp{i}(dataValid_bw{i} == 1, 8);
TorqueBosch_LoadMotor_bw{i} = InputExp{i}(dataValid_bw{i} == 1,10);
AbsPosReni_OutputSide_bw{i} = InputExp{i}(dataValid_bw{i} == 1, 11);

time_fw{i} = linspace(0,length(AbsPosReni_OutputSide_fw{i})*cycletime/1000,length(AbsPosReni_OutputSide_fw{i}));
time_bw{i} = linspace(0,length(AbsPosReni_OutputSide_fw{i})*cycletime/1000,length(AbsPosReni_OutputSide_bw{i}));

TE_fw{i} = TotPosReni_OutputSide_fw{i}-TotPosReni_InputSide_fw{i}/RedRatio;
TE_bw{i} = TotPosReni_OutputSide_bw{i}-TotPosReni_InputSide_bw{i}/RedRatio;

Vel_InputSide_fw{i} = (NumDiff(TotPosReni_InputSide_fw{i},cycletime/1000))/6;
Vel_InputSide_bw{i} = (NumDiff(TotPosReni_InputSide_bw{i},cycletime/1000))/6;

[fTE_fw{i}, ComponentsTE_fw{i},PhaseTE_fw{i}]=fft_fun(TE_fw{i},cycletime);  %[Hz, deg, rad]
[fTE_bw{i}, ComponentsTE_bw{i},PhaseTE_bw{i}]=fft_fun(TE_bw{i},cycletime);

f0_(i)=vel(i)/60/RedRatio;

end

%%
figure
for i = 1 : numel(filenames)
plot(AbsPosReni_OutputSide_fw{i},TE_fw{i})
hold on
end

figure
for i = 1 : numel(filenames)
plot(fTE_fw{i}/f0_(i),ComponentsTE_fw{i})
xlim([1,300]);
ylim([0,0.003]);
hold on
end
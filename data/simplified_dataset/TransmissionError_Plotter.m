clear all;
clc;
close all;

% Import data from experiments
%Data structure
%1 -> Reducer output Position registered during forward motion (0-->360)
%2 -> Related Transmission Error (forward)
%3 -> Reducer output Position registered during forward motion (360-->0)
%4 -> RelatedTransmission Error (bacwward)

%Import file(s) --> update file names
filenames=[
"Test_25degree\100rpm\100.0rpm0.0Nm25.0deg.csv"
];

sampling_time = 0.25; % [ms]

for i=1:numel(filenames)
    InputData{i}=readmatrix(filenames{i});  
    Output_Reducer_fw{i}=InputData{i}(:,1);
    Output_Reducer_fw{i} = Output_Reducer_fw{i}(~isnan(Output_Reducer_fw{i}(:)));
    TE_fw{i}=InputData{i}(:,2);
    TE_fw{i} = TE_fw{i}(~isnan(TE_fw{i}(:)));
    Output_Reducer_bw{i}=InputData{i}(:,3);
    Output_Reducer_bw{i} = Output_Reducer_bw{i}(~isnan(Output_Reducer_bw{i}(:)));
    TE_bw{i}=InputData{i}(:,4);
    TE_bw{i} = TE_bw{i}(~isnan(TE_bw{i}(:)));
end

%Plot Transmission Error
figure;
for i=1:numel(filenames)
    plot(Output_Reducer_fw{i},TE_fw{i},'k','DisplayName','TE forward')
    hold on
    grid on
    plot(Output_Reducer_bw{i},TE_bw{i},'r','DisplayName','TE backward')
end
legend show



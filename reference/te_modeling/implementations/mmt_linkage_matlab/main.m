%% Input data
close all
clear
clc

% Load experimental TE curve
Expdata = readmatrix('TE_experimental.csv');
theta_deg = Expdata(:,1);
TE_exp_deg = Expdata(:,2);

thet_rad = deg2rad(theta_deg(:));
TE_exp_rad = deg2rad(TE_exp_deg(:));

removeMean = true;
if removeMean
    TE_exp_rad = TE_exp_rad - mean(TE_exp_rad);
end

% Nominal reducer parameters
p.geom.z1 = 22;              % sun gear, input gear teeth
p.geom.z2 = 44;              % planetary gear, spur gear teeth
p.geom.z4 = 39;              % cycloidal gear teeth
p.geom.z5 = 40;              % pin number

red_ratio = 1+(p.geom.z2/p.geom.z1)*p.geom.z5;

p.geom.alpha = deg2rad(20);  % involute pressure angle
p.geom.m = 1.5e-3;           % input stage module [m]

p.geom.lR = 111.5e-3;        % pin pitch radius
p.geom.la = 2.0e-3;          % crank eccentricity
p.geom.lH = 65e-3;           % crank distribution or output hole radius

% Equivalent virtual link scales used to convert length error into angular error
p.geom.lb1 = 0.5*p.geom.m*p.geom.z1*cos(p.geom.alpha);
p.geom.lb2 = 0.5*p.geom.m*p.geom.z2*cos(p.geom.alpha);

% Equivalent cycloid pin virtual link length
p.geom.lk = 40e-3;

% Angular orders relative to output angle
p.orders.out = 1;
p.orders.crank = 3;
p.orders.cycloid_tooth = p.geom.z4;
p.orders.pin = p.geom.z5;
p.orders.input = red_ratio;

%% Geometric errors

% Output side, order 1, output disc holes or equivalent output eccentricity
%*******%
err.EH_amp = 20e-6;  % [m]     
err.EH_phi = 0;      % [rad]
%*******%

% Crank and cycloidal support side, typically low orders or order 3
err.Ea_amp = 0;      % crank eccentricity equivalent error [m]
err.Ea_phi = 0;      % [rad]
err.Ec_amp = 0;      % cycloidal gear hole position equivalent error [m]
err.Ec_phi = 0;      % [rad]
err.Ev_amp = 0;      % cycloidal gear center equivalent error [m]
err.Ev_phi = 0;      % [rad]

% Cycloid pin stage, orders 39 and 40
%*******%
err.delta_amp = 2e-6;   % cycloidal tooth profile equivalent error (order 39) [m]
err.delta_phi = 0;   % [rad]
err.dr_amp = 1e-6;      % pin radius equivalent error (order 40) [m]
err.dr_phi = pi/2;      % [rad]
err.AP_amp = 0;      % accumulated pin pitch equivalent length error (order 40) [m]
err.AP_phi = 0;      % [rad]
%*******%

err.dlR_amp = 0;     % pin pitch radius equivalent error (order 40) [m]
err.dlR_phi = 0;     % [rad]

% Involute input stage, order 81 for RV160N
%*******%
err.Eb1_amp = 0;     % input gear pitch circle eccentricity [m]
err.Eb1_phi = 0;     % [rad]
%*******%

err.Eb2_amp = 0;     % planetary gear pitch circle eccentricity [m]
err.Eb2_phi = 0;     % [rad]
err.dtheta_b1_amp = 0; % input angle error, rad
err.dtheta_b1_phi = 0; % [rad]

% Optional constant offset
err.C0 = 0;  % [rad]

%% TE Modeling (MMT formulation)
out = mmt_linkage_TE(thet_rad, p, err);
TE_model = out.TE;

if removeMean
    TE_model = TE_model - mean(TE_model);
end

%% Plots
res = TE_exp_rad - TE_model;

% TEs comparisons
figure
plot(theta_deg, rad2deg(TE_exp_rad), 'k', 'LineWidth', 1.2)
hold on
plot(theta_deg, rad2deg(TE_model), 'r', 'LineWidth', 1.2)
grid on
xlabel('\theta_{out} [deg]')
ylabel('TE [deg]')
legend('Experimental', 'MMT equivalent linkage model')

% TE source terms plot
% figure
% plot(theta_deg, rad2deg(out.f1), 'LineWidth', 1.1)
% hold on
% plot(theta_deg, rad2deg(out.f2mean), 'LineWidth', 1.1)
% plot(theta_deg, rad2deg(out.f3), 'LineWidth', 1.1)
% plot(theta_deg, rad2deg(out.f4mean), 'LineWidth', 1.1)
% grid on
% xlabel('\theta_{out} [deg]')
% ylabel('Subsystem equivalent errors [deg]')
% legend('f1, involute stage', 'f2, crank input side', 'f3, cycloid pin stage', 'f4, crank output side')
% 
% Spectrum
% plot_spectrum(theta_deg, TE_exp_rad, TE_model)


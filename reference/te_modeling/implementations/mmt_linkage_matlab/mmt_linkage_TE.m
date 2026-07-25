function out = mmt_linkage_TE(theta_rad, p, err)

% Main diagnostic mapping:
% EH                  -> f4, order 1
% Ea, Ec, Ev          -> f2 and f4, order 3 or order 39 depending on source
% delta               -> f3, order 39
% dr, dlR, AP         -> f3, order 40
% Eb1, Eb2, dtheta_b1 -> f1, order 81

theta_rad = theta_rad(:);
N = numel(theta_rad);

f1 = zeros(N,1);
f2mean = zeros(N,1);
f3 = zeros(N,1);
f4mean = zeros(N,1);

% Orders
n1 = p.orders.out;
n3 = p.orders.crank;
n39 = p.orders.cycloid_tooth;
n40 = p.orders.pin;
n81 = p.orders.input;

% Link scales
z1 = p.geom.z1;
z2 = p.geom.z2;
z4 = p.geom.z4;
lb2 = p.geom.lb2;
lH = p.geom.lH;
la = p.geom.la;
lk = p.geom.lk;
lR = p.geom.lR;

% f4, output side, order 1
f4mean = (err.EH_amp/lH) .* cos(n1*theta_rad + err.EH_phi);

% f2 and f4, crank related equivalent errors, order 3
f2mean = (err.Ea_amp/la) .* cos(n3*theta_rad + err.Ea_phi);
f2mean = f2mean + (err.Ec_amp/la) .* cos(n3*theta_rad + err.Ec_phi);

f4mean = f4mean + (err.Ea_amp/lH) .* cos(n3*theta_rad + err.Ea_phi);
f4mean = f4mean + (err.Ec_amp/lH) .* cos(n3*theta_rad + err.Ec_phi);

% Cycloidal center equivalent error, order 39
f3 = (err.Ev_amp/lk) .* cos(n39*theta_rad + err.Ev_phi);

% f3, cycloid pin stage, order 39 and 40
f3 = f3 + (err.delta_amp/lk) .* cos(n39*theta_rad + err.delta_phi);
f3 = f3 + (err.dr_amp/lk)    .* cos(n40*theta_rad + err.dr_phi);
f3 = f3 - (err.dlR_amp/lk)   .* cos(n40*theta_rad + err.dlR_phi);

% Accumulated pin pitch error, AP/lR is an angular error of pin location
f3 = f3 + (lR/lk) .* (err.AP_amp/lR) .* sin(n40*theta_rad + err.AP_phi);

% f1, involute input stage, order 81
f1 = (err.Eb1_amp/lb2) .* cos(n81*theta_rad + err.Eb1_phi);
f1 = f1 + (err.Eb2_amp/lb2) .* cos(n81*theta_rad + err.Eb2_phi);
f1 = f1 + err.dtheta_b1_amp .* cos(n81*theta_rad + err.dtheta_b1_phi);

% TE function (Eq. 30)

Derr = 1 + (z1 + z2)/(z2*z4);

TE = ( -(1/z4).*f1 -(1/z4).*f2mean + f3 + f4mean ) ./ Derr;

TE = TE + err.C0;

out.TE = TE;
out.f1 = f1;
out.f2mean = f2mean;
out.f3 = f3;
out.f4mean = f4mean;
out.Derr = Derr;
end

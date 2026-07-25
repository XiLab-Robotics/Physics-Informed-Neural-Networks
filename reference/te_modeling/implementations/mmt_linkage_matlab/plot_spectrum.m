function plot_spectrum(theta_deg, TE_exp, TE_model)

theta = deg2rad(theta_deg(:));
N = numel(theta);

theta_u = linspace(0, 2*pi, N+1).';
theta_u(end) = [];

TEe = interp1(theta, TE_exp(:), theta_u, 'linear', 'extrap');
TEm = interp1(theta, TE_model(:), theta_u, 'linear', 'extrap');

TEe = TEe - mean(TEe);
TEm = TEm - mean(TEm);

Ye = fft(TEe)/N;
Ym = fft(TEm)/N;

ord = (0:N-1).';
amp_e = 2*abs(Ye);
amp_m = 2*abs(Ym);

maxOrd = 250;
idx = ord <= maxOrd;

figure
stem(ord(idx), rad2deg(amp_e(idx)), 'k', 'filled')
hold on
stem(ord(idx), rad2deg(amp_m(idx)), 'r')
grid on
xlabel('Order [cycles/output rev]')
ylabel('Amplitude [deg]')
legend('Experimental', 'Model')
xlim([0 maxOrd])
end

function [y1 y2 y3]=fft_fun(x,cycletime)

fs = 1000/cycletime;       % sample frequency [Hz]              

xf = fft(x);
n = length(x);             

P2 = abs(xf/n);
P1 = P2(1:n/2+1);
P1(2:end-1)=2*P1(2:end-1);
f = fs*(0:(n/2))/n;



xf(abs(xf) < 1e-6) = 0;
theta = angle(xf);

y1=f';
y2=P1;
y3=theta(1:n/2+1);
end

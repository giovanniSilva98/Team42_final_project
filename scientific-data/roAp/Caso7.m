% Caso 7 : roAp
% Luminosità dell'utente --> Ricavi Mv
% Una volta che abbiamo Mv: S=S+Mv
% Periodo: rotazione 8,5 gg, pulsazione 10 min

% L'input è Mv
Mv=;
P=10*60;
T_rot=8.5*24*3600;
w=2*pi/(T_rot);
t=linspace(0,T_rot,200);

S=0.5*sin(w*t);
S=(S+Mv)
plot(t,S);
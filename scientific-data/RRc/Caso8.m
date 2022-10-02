% Caso 8 : RRC
% Luminosità dell'utente --> Ricavi Mv
% Una volta che abbiamo Mv: S=S+Mv
% Periodo: pulsazione 0.3 gg, rotazione 40gg

% L'input è Mv
Mv=;
Mv=abs(Mv);
P=0.3*86400;
T_rot=40*24*3600;
w=2*pi/(T_rot);
t=linspace(0,T_rot,200);

S=0.5*sin(w*t);
S=(S+Mv)
plot(t,S);
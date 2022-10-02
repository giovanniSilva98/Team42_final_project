% Caso 9 : Miras
% Luminosità dell'utente --> Ricavi Mv
% Una volta che abbiamo Mv: S=S+Mv
% Periodo: pulsazione formula, rotazione 100gg

% L'input è Mv
Mv=;

P=100*86400;
T_rot=(-Mv+2.06)/2.54;
w=2*pi/(T_rot);
t=linspace(0,T_rot,200);

S=0.5*sin(w*t);
S=(S+Mv)
plot(t,S);
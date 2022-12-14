% Caso 6 - delta scuti
% Luminosit√† dell'utente --> Ricavi Mv
% Una volta che abbiamo Mv: S=S+Mv
% Periodo: tra 0.02 e 0.3 gg

% L'input √® Mv
Mv=;

P0=0.02 + (0.3-0.02).*rand(1,1);
P=P0*24*60*60;
T_rot=6.4*86400;
w=2*pi/(T_rot);
t=linspace(0,T_rot,200);

S=0.5*sin(w*t);
S=(S+Mv)
plot(t,S);
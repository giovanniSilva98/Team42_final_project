% Caso 10 : ACV
% Luminosità dell'utente --> Ricavi Mv
% Una volta che abbiamo Mv: S=S+Mv
% Periodo: 5.5 gg 

% L'input è Mv
Mv=;

P=0.3*86400;
T_rot=5.5*86400;
w=2*pi/(T_rot);
t=linspace(0,T_rot,200);

f=rand(1,1);
S=-0.5.*cos(2.*w.*t).*(1-f).*cos(w.*t)./(1+f./2);
S=(S+Mv)
plot(t,S);
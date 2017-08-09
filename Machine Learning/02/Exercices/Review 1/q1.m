clear all; clc;

% dataset matrix
A = [89,7921,96;72,5184,74;94,8836,87;69,4761,78];
% midterm exam (x1) average
u1 = mean(A(:,1));
% midterm exam (x1) range
r1 = range(A(:,1));

x31 = (A(3,1)-u1)/r1
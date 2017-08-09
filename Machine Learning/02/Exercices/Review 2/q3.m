clearvars, clc;
A = rand(10);
x = rand(10, 1);

v = zeros(10, 1);
for i = 1:10
    for j = 1:10
        v(i) = v(i) + A(i,j) * x(j);
    end
end

w1 = A * x;
% w2 = Ax;
w3 = x' * A;
w4 = sum(A * x);

v

w1
% w2
% w3
% w4
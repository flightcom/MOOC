clear all, clc;
v = rand(7,1);
w = rand(7,1);

z = 0;
for i = 1:7
    z = z + v(i) * w(i);
end

z

z1 = sum (v .* w)
z2 = w' * v
% z3 = v * w'
% z4 = w * v'
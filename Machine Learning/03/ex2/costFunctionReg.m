function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta


% Cost
sum = 0;
h = sigmoid(theta' * X');

for i=1:m
    sum = sum + ( -y(i) * log(h(i)) - (1 - y(i)) * log(1 - h(i)) );
end

suml = 0;
for j=2:size(theta)
    suml = suml + theta(j) ^ 2;
end

J = (1/m) * sum + (lambda / (2 * m)) * suml;


% Gradient
for j=1:size(grad)
    sum = 0;
    for i=1:m
        sum = sum + ( h(i) - y(i) ) * X(i,j);
    end
    
    grad(j) = (1/m) * sum;

    if (j > 1)
        grad(j) = grad(j) + (lambda / m) * theta(j);
    end
end


% =============================================================

end

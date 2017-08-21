def answer_four():
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import Lasso, LinearRegression
    from sklearn.metrics.regression import r2_score

    # Your code here

    ## Adding Polynomial Features
    poly = PolynomialFeatures(degree=12)
    X_train_poly = poly.fit_transform(X_train.reshape(-1, 1))
    X_test_poly = poly.fit_transform(X_test.reshape(-1, 1))
    
    ## Non-regularized LinearRegression model
    lin = LinearRegression().fit(X_train_poly, y_train)

    ## Lasso Regression Model
    linlasso = Lasso(alpha=0.01, max_iter = 100000).fit(X_train_poly, y_train)

    ## Predict values
    y_pred = lin.predict(X_test_poly)
    y_pred_lasso = linlasso.predict(X_test_poly)

    ## R2
    r2_score_lin = r2_score(y_test, y_pred)
    r2_score_linlasso = r2_score(y_test, y_pred_lasso)

    return (r2_score_lin, r2_score_linlasso)




['odor_n',
 'stalk-root_c',
 'stalk-surface-below-ring_y',
 'spore-print-color_r',
 'odor_l']
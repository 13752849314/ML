# Logistic回归 start at 2022/7/12

$$
h_\theta(x)=g(\theta^Tx)

$$

where

$$
g(z)=\frac{1}{1+e^{-z}}\dots (Sigmoid函数)

$$

$$
J(\theta)=\frac{1}{m}\sum_{i=1}^m{Cost(h_\theta(x_i),y_i)}

$$

$$
Cost(h_\theta(x))=
\begin{cases}
    -log(h_\theta(x)) & if \quad y=1\\
    -log(1-h_\theta(x)) & if \quad y=0
\end{cases}

$$

最后$J(\theta)$可写为：

$$
J(\theta)=-\frac{1}{m}[\sum_{i=1}^my_ilog(h_\theta(x_i))+(1-y_i)log(1-h_\theta(x_i))]

$$

## 梯度下降法

$$
\begin{align*}
    \theta_j:&=\theta_j-\alpha\sum_{i=1}^m(h_\theta(x_i)-y_i)x_i^j
\end{align*}

$$

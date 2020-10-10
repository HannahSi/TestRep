n = 17
sum_x = 2182.4
sum_y = 189
sum_xy = 2761.2
sum_x2 = 3058.2
sum_y2 = 2982

mean_x = sum_x / n
mean_y = sum_y / n
beta_1 = ((sum_xy - mean_y * sum_x - mean_x * sum_y + n * mean_x * mean_y)
            / (sum_x2 - 2 * mean_x * sum_x + n * mean_x**2))
beta_1

beta_0 = mean_y - beta_1 * mean_x
beta_0

sse = sum_y2 - 2 * beta_0 * sum_y - 2 * beta_1 * sum_xy + n * beta_0**2 + 2 * beta_0 * beta_1 * sum_x + \
    beta_1 **2 * sum_x2
sse

sst = sum_y2 - 2 * mean_y * sum_y + n * mean_y**2
sst

1 - sse/sst

##################

x1 = 6.1
x2 = 5.4
y1 = 2.6
y2 = 1.8
sum_x = sum_x - x1 - x2
sum_y = sum_y - y1 - y2
sum_xy = sum_xy - x1 * y1 - x2 * y2
sum_x2 = sum_x2 - x1**2 - x2 **2
sum_y2 = sum_y2 - y1 **2 - y2 **2
n = 15

mean_x = sum_x / n
mean_y = sum_y / n
beta_1 = ((sum_xy - mean_y * sum_x - mean_x * sum_y + n * mean_x * mean_y)
            / (sum_x2 - 2 * mean_x * sum_x + n * mean_x**2))
beta_1

beta_0 = mean_y - beta_1 * mean_x
beta_0

sse = sum_y2 - 2 * beta_0 * sum_y - 2 * beta_1 * sum_xy + n * beta_0**2 + 2 * beta_0 * beta_1 * sum_x + \
    beta_1 **2 * sum_x2
sse

sst = sum_y2 - 2 * mean_y * sum_y + n * mean_y**2
sst

1 - sse/sst

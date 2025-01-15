import cv2
import numpy as np

# 读取输入图像
input_image_path = 'example.png'  # 请替换为您的图像路径
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# 获取图像尺寸
height, width = image.shape

# 设置高斯分布的参数
center_x_1, center_y_1 = 272, 462  # 高斯中心的坐标
sigma_x_1 = 80 # X方向的标准差
sigma_y_1 = 20  # Y方向的标准差

theta_1 = np.radians(25)  # 高斯分布旋转角度（以度数表示，这里是30度）


# 设置高斯分布的参数
center_x_2, center_y_2 = 799, 359  # 高斯中心的坐标
sigma_x_2 = 20 # X方向的标准差
sigma_y_2 = 20  # Y方向的标准差

theta_2 = np.radians(15)  # 高斯分布旋转角度（以度数表示，这里是30度）


# 设置高斯分布的参数
center_x_3, center_y_3 = 709, 502  # 高斯中心的坐标
sigma_x_3 = 10 # X方向的标准差
sigma_y_3 = 20  # Y方向的标准差

theta_3 = np.radians(-20)  # 高斯分布旋转角度（以度数表示，这里是30度）

# 创建一个与输入图像相同尺寸的空白图像用于绘制高斯
gaussian_image = np.zeros((height, width), dtype=np.float32)



# 设置高斯分布的参数
center_x_4, center_y_4 = 746, 371  # 高斯中心的坐标
sigma_x_4 = 100 # X方向的标准差
sigma_y_4 = 20  # Y方向的标准差

theta_4 = np.radians(-80)  # 高斯分布旋转角度（以度数表示，这里是30度）

# 创建一个与输入图像相同尺寸的空白图像用于绘制高斯
gaussian_image = np.zeros((height, width), dtype=np.float32)

# 生成旋转的椭圆形2D高斯分布
for i in range(height):
    for j in range(width):
        # 将坐标转换为以中心为原点的坐标系
        x = j - center_x_1
        y = i - center_y_1

        # 旋转坐标系
        x_rot = x * np.cos(theta_1) + y * np.sin(theta_1)
        y_rot = -x * np.sin(theta_1) + y * np.cos(theta_1)

        # 计算旋转后椭圆形高斯分布的值
        gaussian_image[i, j] += np.exp(-((x_rot ** 2) / (2 * sigma_x_1 ** 2) + (y_rot ** 2) / (2 * sigma_y_1 ** 2)))

# 生成旋转的椭圆形2D高斯分布
for i in range(height):
    for j in range(width):
        # 将坐标转换为以中心为原点的坐标系
        x = j - center_x_2
        y = i - center_y_2

        # 旋转坐标系
        x_rot = x * np.cos(theta_2) + y * np.sin(theta_2)
        y_rot = -x * np.sin(theta_2) + y * np.cos(theta_2)

        # 计算旋转后椭圆形高斯分布的值
        gaussian_image[i, j] += np.exp(-((x_rot ** 2) / (2 * sigma_x_2 ** 2) + (y_rot ** 2) / (2 * sigma_y_2 ** 2)))

# 生成旋转的椭圆形2D高斯分布
for i in range(height):
    for j in range(width):
        # 将坐标转换为以中心为原点的坐标系
        x = j - center_x_3
        y = i - center_y_3

        # 旋转坐标系
        x_rot = x * np.cos(theta_3) + y * np.sin(theta_3)
        y_rot = -x * np.sin(theta_3) + y * np.cos(theta_3)

        # 计算旋转后椭圆形高斯分布的值
        gaussian_image[i, j] += np.exp(-((x_rot ** 2) / (2 * sigma_x_3 ** 2) + (y_rot ** 2) / (2 * sigma_y_3 ** 2)))

# 生成旋转的椭圆形2D高斯分布
for i in range(height):
    for j in range(width):
        # 将坐标转换为以中心为原点的坐标系
        x = j - center_x_4
        y = i - center_y_4

        # 旋转坐标系
        x_rot = x * np.cos(theta_4) + y * np.sin(theta_4)
        y_rot = -x * np.sin(theta_4) + y * np.cos(theta_4)

        # 计算旋转后椭圆形高斯分布的值
        gaussian_image[i, j] += np.exp(-((x_rot ** 2) / (2 * sigma_x_4 ** 2) + (y_rot ** 2) / (2 * sigma_y_4 ** 2)))


# 将高斯图像归一化到0-255
gaussian_image = cv2.normalize(gaussian_image, None, 0, 255, cv2.NORM_MINMAX)

# 转换为8位图像
gaussian_image = gaussian_image.astype(np.uint8)

colored_gaussian = cv2.applyColorMap(gaussian_image, cv2.COLORMAP_JET)  # 选择一种颜色映射，如“JET”或“HOT”

# 将彩色高斯图像与输入图像叠加（需要将输入图像转换为三通道）
input_image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
output_image = cv2.addWeighted(input_image_color, 0.7, colored_gaussian, 0.3, 0)  # 调整权重以控制叠加效果


# 保存结果图像
# cv2.imwrite('original_image.png', input_image_color)
output_image_path = 'output_example_gs.png'  # 指定保存路径
cv2.imwrite(output_image_path, output_image)

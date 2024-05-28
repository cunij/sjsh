import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
theta = np.linspace(0, 2 * np.pi, 100)  # 0에서 2π까지 100개의 값을 생성
r = np.abs(np.sin(theta))  # r 값은 sin 함수의 절대값
colors = theta  # 색은 theta 값에 따라 설정

# 플롯 생성
plt.figure()
ax = plt.subplot(111, projection='polar')  # 극좌표계를 사용
c = ax.scatter(theta, r, c=colors, cmap='hsv', alpha=0.75)  # 극좌표계에 산포도 플롯 생성

# 색상 막대 추가
plt.colorbar(c, ax=ax, label='Phase')

# 제목 추가
ax.set_title("Polar Plot Colored by Phase")

# 플롯 표시
plt.show()

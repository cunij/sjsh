import matplotlib.pyplot as plt
import numpy as np

def draw_lines(interval=10, angles=[0, 90]):
    # 그래프 초기화
    fig, ax = plt.subplots(figsize=(10, 10))

    # 두 각도에 대해 선 그리기
    for angle in angles:
        # 각도를 라디안 단위로 변환
        angle_rad = np.deg2rad(angle)

        # 선의 간격과 각도에 따라 선의 위치를 계산
        positions = np.arange(-100, 100, interval)

        # 각도에 따른 회전 변환 행렬
        cos_angle = np.cos(angle_rad)
        sin_angle = np.sin(angle_rad)

        for pos in positions:
            # x축에 대한 회전 적용 (단일 방향 선)
            x_start, y_start = pos * cos_angle - 100 * sin_angle, pos * sin_angle + 100 * cos_angle
            x_end, y_end = pos * cos_angle + 100 * sin_angle, pos * sin_angle - 100 * cos_angle
            ax.plot([x_start, x_end], [y_start, y_end], 'k-', linewidth=0.5)

    # 축 설정
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_aspect('equal')

    plt.grid(False)
    plt.show()

# 예시: 20 간격으로 각도 30도와 60도의 선 그리기
draw_lines(interval=2, angles=[0,5])

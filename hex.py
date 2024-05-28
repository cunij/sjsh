import matplotlib.pyplot as plt
import numpy as np

def hexagon(x_center, y_center, size):
    """Generate the vertices of a hexagon centered at (x_center, y_center) with a given size."""
    angles = np.linspace(0, 2 * np.pi, 7)
    x_hex = x_center + size * np.cos(angles)
    y_hex = y_center + size * np.sin(angles)
    return x_hex, y_hex

def draw_hex_tiling(center_x=0, center_y=0, interval=10, size=5, angles=[0, 90], linewidth=0.5):
    # 그래프 초기화
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # 두 각도에 대해 벌집 모양 육각형 타일 그리기
    for angle in angles:
        # 각도를 라디안 단위로 변환
        angle_rad = np.deg2rad(angle)
        
        # 회전 변환 행렬
        cos_angle = np.cos(angle_rad)
        sin_angle = np.sin(angle_rad)
        
        # 육각형의 높이 계산
        hex_height = np.sqrt(3) * size
        
        # 화면을 채우기 위해 더 넓은 범위를 설정
        for i in range(-50, 51):
            for j in range(-50, 51):
                # 벌집 구조의 좌표 계산
                x = i * 1.5 * size
                y = j * hex_height + (i % 2) * hex_height / 2
                
                # 중심에서의 상대 위치 계산
                x_rel = x - center_x
                y_rel = y - center_y
                
                # 회전 적용
                x_rot = x_rel * cos_angle - y_rel * sin_angle
                y_rot = x_rel * sin_angle + y_rel * cos_angle
                
                # 회전된 좌표를 중심으로 복원
                x_final = x_rot + center_x
                y_final = y_rot + center_y
                
                # 육각형 생성 및 플로팅
                x_hex, y_hex = hexagon(x_final, y_final, size)
                ax.plot(x_hex, y_hex, 'k-', linewidth=linewidth)
    
    # 축 설정
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_aspect('equal')
    
    plt.grid(False)
    plt.show()

# 예시: 중심을 (0, 0)으로 하고, 20 간격으로 각도 30도와 60도의 벌집 모양 육각형 그리기, 선 굵기 1.0
draw_hex_tiling(center_x=0, center_y=0, interval=2, size=2, angles=[0,30], linewidth=1.0)

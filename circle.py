import turtle

def draw_concentric_circles(radius, gap, center_distance):
    # 터틀 설정
    t = turtle.Turtle()
    t.speed(0)  # 최고 속도

    # 첫 번째 도형 그리기
    current_radius = radius
    for _ in range(20):
        t.circle(current_radius)
        current_radius += gap

    # 두 번째 도형 그리기
    current_radius = radius
    t.penup()
    t.goto(center_distance, 0)  # 중심 간의 간격만큼 이동
    t.pendown()
    for _ in range(20):
        t.circle(current_radius)
        current_radius += gap

    # 그리기 종료
    turtle.done()

def main():
    # 중심 간의 간격 입력 받기
    center_distance = float(input("두 도형의 중심 간의 간격을 입력하세요: "))

    # 반지름 및 간격 설정
    radius = 10
    gap = 10

    # 두 도형 그리기
    draw_concentric_circles(radius, gap, center_distance)

main()

from math import sin, cos, tan, radians

def calculusAngle(degree):
    radian = radians(degree)
    print(
        f"{radian} radian, le sinus={sin(radian)}, le cosinus={cos(radian)} et la tangente={tan(radian)}"
    )

calculusAngle(0)
calculusAngle(30)
calculusAngle(45)
calculusAngle(60)
calculusAngle(90)

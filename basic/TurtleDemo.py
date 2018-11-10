from turtle import forward, right, circle, done

steps = 0
angle = 50
while steps < 100:
    circle(angle)
    steps += 1
    angle += 1

done()

#Created by
#Ronald Armistead-Tyler

#SAS Formulas:
#{Law of Cosines}
#a^2 = b^2 + C^2 - 2bc * cos(A)
#{Law of Sines}
#B =  arcsin(sin(A) * b / a)

from math import sqrt, sin, cos, degrees, radians, asin

angleA = radians(float(input("Angle A: ")))
sideB = float(input("Side B: "))
sideC = float(input("Side C: "))

sideA = sqrt(pow(sideB, 2) + pow(sideC, 2) - 2 * sideB * sideC * cos(angleA))
angleB = degrees(asin(sin(angleA) * sideB / sideA))
angleC = degrees(asin(sin(angleA) * sideC / sideA))

print("\n\nSide A:", round(sideA, 3))
print("Angle B:", str(round(angleB, 3)) + "°")
print("Angle C:", str(round(angleC, 3)) + "°")
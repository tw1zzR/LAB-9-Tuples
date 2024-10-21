import math

x1 = int(input("Введіть перше число кортежу X: "))
y1 = int(input("Введіть друге число кортежу X: "))
z1 = int(input("Введіть третє число кортежу X: "))
x = (x1,y1,z1)

x2 = int(input("\nВведіть перше число кортежу Y: "))
y2 = int(input("Введіть друге число кортежу Y: "))
z2 = int(input("Введіть третє число кортежу Y: "))
y = (x2,y2,z2)

diff_XY_x = x2-x1
diff_XY_y = y2-y1
diff_XY_z = z2-z1

range_XY = math.sqrt(math.pow(diff_XY_x,2)+math.pow(diff_XY_y,2)+math.pow(diff_XY_z,2))
print(f"\nВідстань між точками XY: {round(range_XY,2)}.")

diff_YX_x = x1-x2
diff_YX_y = y1-y2
diff_YX_z = z1-z2

range_YX = math.sqrt(math.pow(diff_YX_x,2)+math.pow(diff_YX_y,2)+math.pow(diff_YX_z,2))
print(f"\nВідстань між точками YX: {round(range_YX,2)}.")

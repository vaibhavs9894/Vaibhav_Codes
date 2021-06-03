from sample_classes import Equation
# from PIL import Image

eq = Equation()

output = eq.area(12,13)
print('area =>',output)

output = eq.cube(30)
print('cube =>',output)

print('sphere volume =>',eq.sphere_vol(8))

# im = Image.open(r'C:\Users\xaidi\OneDrive\Pictures\img.png')
# im.show()


side_a = float(input('enter a'))
side_b = float(input('enter b'))
side_c = float(input('enter c'))

half_perimeter = (side_a + side_b + side_c) / 2
print(half_perimeter)


triangle_area = (half_perimeter * (half_perimeter - side_a) *
                 (half_perimeter - side_b)